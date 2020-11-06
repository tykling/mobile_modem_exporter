"""mobile_modem_exporter v0.1.0 module.

Source code available at https://github.com/tykling/mobile_modem_exporter/
Can be installed from PyPi https://pypi.org/project/mobile_modem_exporter/
Read more at https://mobile-modem-exporter.readthedocs.io/en/latest/
"""
import argparse
import logging
import time
import typing

from pipeserial.pipeserial import PipeSerial  # type: ignore
from prometheus_client import Info  # type: ignore
from prometheus_client import CollectorRegistry, Gauge, write_to_textfile

__version__ = "0.1.0"
logger = logging.getLogger("mobile_modem_exporter.%s" % __name__)


def parse_ati(output: typing.List[str]) -> typing.Tuple[str, str, str]:
    """Parse the output of the ATI command.

    Args:
        output: The output of the ATI command

    Returns: A tuple of (manufacturer, model, revision)
    """
    i = 0
    for line in output:
        line = line.strip()
        if not line:
            # skip empty lines
            continue
        if line == "ATI":
            # skip the command itself
            continue
        if line[0] == "^":
            # skip unsolicited output from the modem
            continue

        # line 1 is manufacturer, line 2 is model, line 3 is revision
        i += 1
        if i == 1:
            manufacturer = str(line.replace("Manufacturer: ", ""))
        elif i == 2:
            model = str(line.replace("Model: ", ""))
        elif i == 3:
            revision = str(line.replace("Revision: ", ""))
            # this was the last interesting line of ATI output
            return manufacturer, model, revision

    logger.error("The parse_ati() function was unable to parse ATI output")
    logger.debug("Unparseable ATI output:")
    logger.debug(output)
    raise ValueError("Unable to parse ATI output")


def parse_atgsn(output: typing.List[str]) -> str:
    """Parse the output of the AT+GSN command.

    Args:
        output: The output of the AT+GSN command

    Returns: A string with the serial number
    """
    for line in output:
        line = line.strip()
        if not line:
            # skip empty lines
            continue
        if line == "AT+GSN":
            # skip the command itself
            continue
        if line[0] == "^":
            # skip unsolicited output from the modem
            continue
        # this should be the serial number
        return line
    logger.error("The parse_atgsn() function was unable to parse AT+GSN output")
    logger.debug("Unparseable AT+GSN output:")
    logger.debug(output)
    raise ValueError("Unable to parse AT+GSN output")


def parse_atcsq(output: typing.List[str]) -> typing.Tuple[int, int]:
    """Parse the output of the AT+CSQ command.

    Args:
        output: The output of the AT+CSQ command

    Returns: A tuple of (rssi, ber)
    """
    for line in output:
        line = line.strip()
        if not line:
            # skip empty lines
            continue
        if line == "AT+GSN":
            # skip the command itself
            continue
        if line[0] == "^":
            # skip unsolicited output from the modem
            continue
        # +CSQ: 31,99
        if line[0:4] == "+CSQ":
            rssi, ber = line[6:].split(",")
            return int(rssi), int(ber)

    logger.error("The parse_atcsq() function was unable to parse AT+CSQ output")
    logger.debug("Unparseable AT+CSQ output:")
    logger.debug(output)
    raise ValueError("Unable to parse AT+CSQ output")


def main() -> None:
    """Get args, initialise prom client and pipeserial objects, and start the loop.

    Args: None
    Returns: None
    """
    # get argparse object and parse args
    parser = get_parser()
    args = parser.parse_args()

    # define the log format used for stdout depending on the requested loglevel
    if args.loglevel == "DEBUG":
        console_logformat = "%(asctime)s %(levelname)s mobile_modem_exporter.%(funcName)s():%(lineno)i:  %(message)s"
    else:
        console_logformat = (
            "%(asctime)s %(levelname)s mobile_modem_exporter %(message)s"
        )

    # configure the log format used for console
    logging.basicConfig(
        level=getattr(logging, str(args.loglevel)),
        format=console_logformat,
        datefmt="%Y-%m-%d %H:%M:%S %z",
    )

    logger.debug("Initialising serial ports and Prometheus objects...")
    registry = CollectorRegistry()
    # mobile_modem_up
    up = Gauge(
        "mobile_modem_up",
        "This metric is always 1 if the mobile_modem scrape worked, 0 if there was a problem getting info from one or more modems.",
        registry=registry,
    )

    # mobile_modem_build_info
    build_info = Info(
        "mobile_modem_build",
        "Information about the mobile_modem_exporter itself.",
        registry=registry,
    )
    build_info.info(
        {"version": __version__, "pipeserial_version": PipeSerial.__version__}
    )

    # mobile_modem_info
    modem_info = Info(
        "mobile_modem",
        "Information about the mobile modem being monitored, including device path, manufacturer, model, revision and serial number.",
        ["device"],
        registry=registry,
    )

    # mobile_modem_atcsq_rssi
    modem_rssi = Gauge(
        "mobile_modem_atcsq_rssi",
        "RSSI for the mobile modem as returned by AT+CSQ",
        ["device"],
        registry=registry,
    )

    # mobile_modem_ber
    modem_ber = Gauge(
        "mobile_modem_atcsq_ber",
        "BER for the mobile modem as returned by AT+CSQ",
        ["device"],
        registry=registry,
    )

    # initialise pipeserial objects
    devices = []
    logger.info("Initialising serial ports...")
    for device in args.SERIALDEVICE:
        logger.debug(f"Opening serial port {device} and getting modem info...")
        pipe = PipeSerial(serialport=device)
        pipe.open()
        devices.append(pipe)

        # get serial device info
        output = pipe.run("ATI", ["OK"])
        manufacturer, model, revision = parse_ati(output)

        # get serial device serial number
        output = pipe.run("AT+GSN", ["OK"])
        serial = parse_atgsn(output)

        # set mobile_modem_info for this device
        modem_info.labels(device=device).info(
            {
                "manufacturer": manufacturer,
                "model": model,
                "revision": revision,
                "serial": serial,
            }
        )

    # init done, start loop
    logger.info(
        f"Entering main loop, writing metrics for modems {args.SERIALDEVICE} to {args.PROMPATH}, sleeping {args.sleep} seconds between runs..."
    )
    while True:
        # start out optimistic!
        up.set(1)
        for device in devices:
            logger.debug(f"Getting CSQ from device: {device.ser.name}")
            output = device.run("AT+CSQ", ["OK"])
            try:
                rssi, ber = parse_atcsq(output)
            except Exception:
                logger.exception("Got an exception while parsing AT+CSQ output")
                # set up to 0 for this scrape
                up.set(0)
                continue
            logger.debug(f"parsed AT+CSQ output to rssi {rssi} and BER {ber}")
            modem_rssi.labels(device=device.ser.name).set(rssi)
            modem_ber.labels(device=device.ser.name).set(ber)

        # output metrics to textfile exporter path
        write_to_textfile(args.PROMPATH, registry)
        logger.debug(f"Sleeping {args.sleep} seconds before next run...")
        time.sleep(args.sleep)


def get_parser() -> argparse.ArgumentParser:
    """Create and return the argparse object.

    Args: None
    Returns: The argparse object
    """
    parser = argparse.ArgumentParser(
        description=f"mobile_modem_exporter version {__version__}. Exports signal quality information for mobile modems. See the manpage or ReadTheDocs for more info."
    )

    parser.add_argument(
        "PROMPATH",
        type=str,
        help="The path to the prometheus node_exporter textfile collector file to write output to.",
    )

    parser.add_argument(
        "SERIALDEVICE",
        nargs="+",
        type=str,
        help="The path to a serial device to get signal quality from. Can be specified multiple times.",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_const",
        dest="loglevel",
        const="DEBUG",
        help="Debug mode. Equal to setting --log-level=DEBUG.",
        default=argparse.SUPPRESS,
    )

    parser.add_argument(
        "-l",
        "--log-level",
        dest="loglevel",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level. One of DEBUG, INFO, WARNING, ERROR, CRITICAL. Defaults to INFO.",
        default="INFO",
    )

    parser.add_argument(
        "-s",
        "--sleep",
        type=int,
        nargs="?",
        help="Sleep this many seconds between runs, default: %(default)s",
        default=10,
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_const",
        dest="loglevel",
        const="WARNING",
        help="Quiet mode. No output at all if no errors are encountered. Equal to setting --log-level=WARNING.",
        default=argparse.SUPPRESS,
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s version {__version__}",
        help="Show mobile_modem_exporter version and exit.",
    )

    return parser


def init() -> None:
    """Call the main() function if being invoked as a script. This is here just as a testable way of calling main()."""
    if __name__ == "__main__":
        main()


# call init(), which then calls main() when needed
init()

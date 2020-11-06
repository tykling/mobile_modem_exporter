Usage
=====

Until I get something better written here are the argparse usage instructions::

   usage: mobile_modem_exporter.py [-h] [-d]
                                   [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                                   [-s [SLEEP]] [-q] [-v]
                                   PROMPATH SERIALDEVICE [SERIALDEVICE ...]

   mobile_modem_exporter version 0.1.0-dev. Exports signal quality information
   for mobile modems. See the manpage or ReadTheDocs for more info.

   positional arguments:
     PROMPATH              The path to the prometheus node_exporter textfile
                           collector file to write output to.
     SERIALDEVICE          The path to a serial device to get signal quality
                           from. Can be specified multiple times.

   optional arguments:
     -h, --help            show this help message and exit
     -d, --debug           Debug mode. Equal to setting --log-level=DEBUG.
     -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                           Logging level. One of DEBUG, INFO, WARNING, ERROR,
                           CRITICAL. Defaults to INFO.
     -s [SLEEP], --sleep [SLEEP]
                           Sleep this many seconds between runs, default: 10
     -q, --quiet           Quiet mode. No output at all if no errors are
                           encountered. Equal to setting --log-level=WARNING.
     -v, --version         Show mobile_modem_exporter version and exit.

Read on for examples.

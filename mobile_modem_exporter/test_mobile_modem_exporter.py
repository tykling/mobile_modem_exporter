"""The mobile_modem_exporter testsuite."""
from mobile_modem_exporter import parse_atcsq, parse_atgsn, parse_ati


def test_parse_ati() -> None:
    """Testing the parse_ati functionality."""
    data = """ATI
Manufacturer: Huawei Technologies Co., Ltd.
Model: ME909s-120
Revision: 11.617.15.00.00
IMEI: 864172044791624
+GCAP: +CGSM,+DS,+ES

OK""".split(
        "\n"
    )
    manufacturer, model, revision = parse_ati(data)
    assert manufacturer == "Huawei Technologies Co., Ltd."
    assert model == "ME909s-120"
    assert revision == "11.617.15.00.00"


def test_parse_atgsn() -> None:
    """Testing the parse_atgsn functionality."""
    data = """AT+GSN
864172044791624

OK""".split(
        "\n"
    )
    serial = parse_atgsn(data)
    assert serial == "864172044791624"


def test_parse_atcsq() -> None:
    """Testing the parse_atcsq functionality."""
    data = """AT+CSQ
+CSQ: 21,99

OK""".split(
        "\n"
    )
    rssi, ber = parse_atcsq(data)
    assert rssi == 21
    assert ber == 99

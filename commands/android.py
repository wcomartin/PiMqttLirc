from . import send_once


def toggle_power():
    send_once("MS8_PRO_L", "KEY_POWER")

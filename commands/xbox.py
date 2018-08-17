from . import send_once


def toggle_power():
    send_once("Xbox360", "KEY_POWER")

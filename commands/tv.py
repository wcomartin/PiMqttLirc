from . import send_once


def toggle_power():
    send_once("Sharp_LCDTV-845-039-40B0", "KEY_POWER")
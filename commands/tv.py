from . import send_once


def toggle_power(client, msg):
    send_once("Sharp_LCDTV-845-039-40B0", "KEY_POWER")
    client.publish("IR1/TV/POWER/STATE", msg.payload)

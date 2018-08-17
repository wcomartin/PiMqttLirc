from . import send_once


def toggle_power(client, msg):
    send_once("Xbox360", "KEY_POWER")
    client.publish("IR1/XBOX/POWER/STATE", msg.payload)

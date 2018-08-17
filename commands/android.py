from . import send_once


def toggle_power(client, msg):
    send_once("MS8_PRO_L", "KEY_POWER")
    client.publish("IR1/ANDROID/POWER/STATE", msg.payload)

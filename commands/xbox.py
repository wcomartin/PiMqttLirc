from . import send_once
import mqtt_topics


def toggle_power(client, msg):
    send_once("Xbox360", "KEY_POWER")
    client.publish(mqtt_topics.XBOX_POWER_STATE, msg.payload)

from . import send_once
import mqtt_topics


def toggle_power(client, msg):
    send_once("Sharp_LCDTV-845-039-40B0", "KEY_POWER")
    client.publish(mqtt_topics.TV_POWER_STATE, msg.payload)

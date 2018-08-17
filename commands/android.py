from . import send_once
import mqtt_topics


def toggle_power(client, msg):
    send_once("MS8_PRO_L", "KEY_POWER")
    client.publish(mqtt_topics.ANDROID_POWER_STATE, msg.payload)

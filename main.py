import paho.mqtt.client as mqtt

import mqtt_topics

from commands import tv
from commands import android
from commands import xbox


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(mqtt_topics.TV_POWER)
    client.subscribe(mqtt_topics.ANDROID_POWER)
    client.subscribe(mqtt_topics.XBOX_POWER)


def on_message(client, userdata, msg):
    print(msg.topic)

    if msg.topic == mqtt_topics.TV_POWER:
        tv.toggle_power(client, msg)

    if msg.topic == mqtt_topics.ANDROID_POWER:
        android.toggle_power(client, msg)

    if msg.topic == mqtt_topics.XBOX_POWER:
        xbox.toggle_power(client, msg)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.10", 1883, 60)
client.loop_forever()

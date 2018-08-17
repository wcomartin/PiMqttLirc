import paho.mqtt.client as mqtt

from commands import tv
from commands import android
from commands import xbox


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("IR1/TV/POWER")
    client.subscribe("IR1/ANDROID/POWER")
    client.subscribe("IR1/XBOX/POWER")


def on_message(client, userdata, msg):
    print(msg.topic)

    if msg.topic == "IR1/TV/POWER":
        tv.toggle_power()
        client.publish("IR1/TV/POWER/STATE", msg.payload)

    if msg.topic == "IR1/ANDROID/POWER":
        android.toggle_power()
        client.publish("IR1/ANDROID/POWER/STATE", msg.payload)

    if msg.topic == "IR1/XBOX/POWER":
        xbox.toggle_power()
        client.publish("IR1/XBOX/POWER/STATE", msg.payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.10", 1883, 60)
client.loop_forever()

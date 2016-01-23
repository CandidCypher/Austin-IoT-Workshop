import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with Result code " +str(rc))
    client.subscribe("hello/world")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1833, 60)

client.loop_forever()

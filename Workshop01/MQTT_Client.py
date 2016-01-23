import paho.mqtt.client as mqtt
import time

# Define Event Callbacks


def on_connect(client, userdata, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print("Connection failed. rc = "+str(rc))


def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mide "+str(mid)+" recieved.")


def on_message(client, userdata, msg):
    bytesObject = msg.payload
    messageString = bytesObject.decode('UTF-8')
    print("Message recieved on topic " + msg.topic
          + " and payload " + msg.payload.decode('UTF-8'))


mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Establish Connection
mqttclient.connect("localhost", 1883, 60)

# Start Subscription
mqttclient.subscribe("hello/world")

# Publish a Message
mqttclient.publish("hello/world", "Hello World Message!")

# Loop; exit on error
rc = 0
while rc == 0:
    rc = mqttclient.loop()
    mqttclient.publish("hello/world", "This is my message")
    time.sleep(5)

import paho.mqtt.client as mqtt

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
    print("Message recieved on topic " + msg.topic + " with QoS " + str(msg.qos)
          + " and payload " + msg.payload)


mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Establish Connection
mqtt.connect("localhost", 1883, 60)

mqtt.loop_forever()

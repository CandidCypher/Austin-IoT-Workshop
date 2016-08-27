/*
 * Simple MQTT Publisher for the NodeMCU using a Hall Effect Sensor
 * to detect when a door is opened.
 */
#include "MQTT/MQTT.h"

// This is where we will set up the pub/sub info
const char* broker = "";
const char * pubTopic = "/DoorSensors";
const char * subTopic = "/color";

// Here is where we create the instance of the MQTT client
MQTT client(broker, 1883, callback);

// Next we declare the pins we will use.
const int door_pin = 3;

//Next we will declare our functions to be used in main

void callback(char* topic, byte* payload, unsigned int length) {
    char p[length + 1];
    memcpy(p, payload, length);
    p[length] = NULL;
    String message(p);

    if (message.equals("RED"))
        RGB.color(255, 0, 0);
    else if (message.equals("GREEN"))
        RGB.color(0, 255, 0);
    else if (message.equals("BLUE"))
        RGB.color(0, 0, 255);
    else
        RGB.color(255, 255, 255);
    //delay(1000);
}


void setup()
{
  RGB.control(true);
  // Connection to our Message Broker
  client.connect("SkyScreamPhoton")

  pinMode(door_pin, INPUT);

  if (client.isConnected())
  {
  client.publish(pubTopic, "Joining System: ")
  client.subscribe(subTopic);
  }
}


void loop()
{
  if(!client.isConnected())
  {
    client.connect("SkyScreamPhoton");
  }

  client.loop();

  if(digitalRead(door_pin)==LOW)
  {
    client.publish(pubTopic, "Door Open!");
    RGB.color(255, 0, 0);
  }
  else
  {
    RGB.color(0, 0, 255);
  }

  else
  {
    digitalWrite(LED, LOW);
  }
}

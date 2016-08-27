/* Simple MQTT Publisher for the NodeMCU using a Hall Effect Sensor
 * to detect when a door is opened.
 */
 
#include "MQTT/MQTT.h"


char * server =  "10.11.17.140";
char *pubTopic = "/Doors";
char *subTopic = "/color";

// Here we will create an instance of a MQTT client
MQTT client(server, 1883, callback);


const int door_pin = 3;


// Definition of the function to be called when a message is sent to Photon

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
  client.connect("SkyScreamPhoton");

  pinMode(door_pin, INPUT);

  if (client.isConnected())
  {
  client.publish(pubTopic, "Joining System: ");
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

}


/*
This is a basic example of using MQTT to communicate to an MQTT
Mosquitto Server and control hardware

Author: Cameron Owens
Date: July 14, 2016

*/


// Here we will include the MQTT library available to the Photon
// This is the same process as in Python using the import method

#include "MQTT/MQTT.h"

const char * broker =  "";
char *pubTopic = "/helloworld";
char *subTopic = "/color";
// Here we will create an instance of a MQTT client
MQTT client(broker, 1883, callback);


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



void setup() {
    RGB.control(true);
    // connect to the server with a node name
    client.connect("SkyScreamPhoton");

    // publish/subscribe
    if (client.isConnected()) {
        client.publish( pubTopic, "Joining System:");
        client.subscribe(subTopic);
    }
}

void loop() {
    if (!client.isConnected())
    {
        client.connect("SkyScreamPhoton");
    }
        client.loop();
}

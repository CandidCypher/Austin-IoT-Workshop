/*
 * LightSensorMqttDemo
 *
 * A simple m2m.io platform demo for Arduino.
 */

#include <PubSubClient.h>
#include <ESP8266WiFi.h>

const char* ssid = "Cybertron";
const char* password = "Bu22K!ll";

const char* broker = "192.168.0.107";
String msgString = "";
const int moistureSensor = A0;
const int LED = 13;

char msgBuffer[100];
int sensorVal = 0;

WiFiClient espClient;
PubSubClient client(espClient);


///////////////////////////////
// Setup WiFi Functin
///////////////////////////////

void setup_wifi()
{
  delay(10);
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while(WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connection to ");
  Serial.print(ssid);
  Serial.println("Device IP address :");
  Serial.println(WiFi.localIP());
}


/////////////////////////////////
// Reconnect WiFi Connection
/////////////////////////////////

void reconnect()
{
  while(!client.connected())
  {
    Serial.print("Attempting MQTT connection .....");
    if(client.connect("ESP8266Client"))
    {
      // Joining Message
      client.publish("Plants/", "FlowerPot");
    }
    else
    {
      Serial.print("Connection failed: rc = ");
      Serial.print(client.state());
      Serial.println("trying again in 5 seconds");
      delay(5000);
    }
  }
}

void setup()
{
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  pinMode(moistureSensor, INPUT);
  setup_wifi();
  client.setServer(broker, 1883);
}

void loop()
{
  if(!client.connected())
  {
    reconnect();
  }
  sensorVal = analogRead(moistureSensor);
  msgString = "Moisture: " + String(sensorVal);
  msgString.toCharArray(msgBuffer, msgString.length()+1); 
  client.publish("Plants/", msgBuffer);
  delay(100000);
  
}


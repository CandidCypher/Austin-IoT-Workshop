/*
 * Simple MQTT Publisher for the NodeMCU
 */
#include <PubSubClient.h>
# include <ESP8266WiFi.h>

const char* ssid = "Cybertron";
const char* password = "Bu22K!ll";

const char* broker = "192.168.0.106";

const int door_pin = 15;

const int LED = 13;

WiFiClient espClient;
PubSubClient client(espClient);
char msg[50];

void setup_wifi()
{
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("Hello/", "hello world");
      // ... and resubscribe
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() 
{
  Serial.begin(115200);
  pinMode(door_pin, INPUT);
  pinMode(LED, OUTPUT);
  setup_wifi();
  client.setServer(broker, 1883);
}


void loop() 
{
  if(!client.connected())
  {
    reconnect();
  }

  client.loop();

  if(digitalRead(door_pin)==LOW)
  {
    digitalWrite(LED, HIGH);
    snprintf (msg, 75, "Door Alarm");
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("Hello/", msg);
  }

  else
  {
    digitalWrite(LED, LOW);
  }
}

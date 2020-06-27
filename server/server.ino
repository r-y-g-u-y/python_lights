#include "led.h"
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "BateLAN";
const char* password = "7536131077";




WiFiUDP Udp;

unsigned int localUdpPort = 42424;  // local port to listen on
char incomingPacket[32];  // buffer for incoming packets
char  replyPacket[] = "ACK"; //to be included

s_light currentCmd; //current command struct


void parse_command(s_light *command)
{
  switch(command->command)
  {
    case CMD_OFF:
      break;
    case CMD_SOLID:
      break;
    case CMD_GRADIENT:
      break; 
  }
}

void handle_led_solid(s_light *command)
{
}



void setup()
{
  Serial.begin(115200);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}

void loop()
{
  
  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    int len = Udp.read(incomingPacket, 32);
    Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
    Serial.printf("UDP packet contents: %s\n", incomingPacket);

    init_light_struct(incomingPacket, &currentCmd);
    parse_command(&currentCmd);
    delay(1000);
  }
}

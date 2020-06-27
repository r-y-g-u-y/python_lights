#include <NeoPixelAnimator.h>
#include <NeoPixelBrightnessBus.h>
#include <NeoPixelBus.h>
#include <NeoPixelSegmentBus.h>

#include "led.h"
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "BateLAN";
const char* password = "7536131077";

const uint16_t PixelCount = 32;
const uint8_t PixelPin = 2;

NeoPixelBus<NeoGrbFeature, Neo800KbpsMethod> strip(PixelCount, PixelPin);
RgbColor off(0);


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
      handle_led_off();
      break;
    case CMD_SOLID:
      handle_led_solid(command);
      break;
    case CMD_GRADIENT:
      handle_led_gradient(command);
      break; 
  }
}

void handle_led_solid(s_light *command)
{
  RgbColor color1(command->red_1, command->green_1, command->blue_1);
  for (int i=0; i<PixelCount; i++)
  {
    strip.SetPixelColor(i, color1);
  }
}

void handle_led_off()
{
  for (int i=0; i<PixelCount; i++)
  {
    strip.SetPixelColor(i, off);
  }
  strip.show()
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
  delay(200);
  strip.Begin();
  strip.Show();
  delay(200);
  Serial.println("LED Strip now running");
  
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

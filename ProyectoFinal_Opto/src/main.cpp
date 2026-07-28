#include <Arduino.h>
#include <Wire.h>
#include <HCSR04.h>
#include <Ticker.h>

Ticker timer_Ultrasonic;

void setup(){

  Serial.begin(115200);

  Serial.println("Serial test");

  // Declaración de pines
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);

  digitalWrite(triggerPin, LOW);

  timer_Ultrasonic.attach(0.1, timerInterrupt);
}

void loop(){

  Distance_Ultrasonic();

}


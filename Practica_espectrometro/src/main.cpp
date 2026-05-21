#include <Arduino.h>
#include "28BYJ_48.h"

void setup() {

  // Initialize Serial communication
  Serial.begin(115200);

  //declarar pines como salida
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);

}

void loop() {

  for (int i = 0; i < stepsPerRev; i++)
  {
    clockwise();
    delayMicroseconds(motorSpeed);

    Serial.print("Clockwise step: ");
    Serial.println(i + 1);
  }
  
  for (int i = 0; i < stepsPerRev; i++)
  {
    anticlockwise();
    delayMicroseconds(motorSpeed);

    Serial.print("Counter clockwise step: ");
    Serial.println(i + 1);    
  }
  delay(1000);
}

#include <Arduino.h>
#include "28BYJ_48.h"
#include "GY_2561.h"
#include <Wire.h>

/* I2C comm*/
#define I2C_SDA1 8
#define I2C_SCL1 9

TwoWire I2C_ONE = TwoWire(0);

Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, GY_2561_ADDR);

void setup() {

  // Initialize Serial communication
  Serial.begin(115200);

  //declarar pines como salida
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);

  I2C_ONE.begin(I2C_SDA1, I2C_SCL1, 50000);  // I2C Bus 1

  delay(10);

  if(!tsl.begin(&I2C_ONE))
  {
    /* There was a problem detecting the TSL2561 ... check your connections */
    Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

}

void loop() {

  /*for (int i = 0; i < stepsPerRev; i++)
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
  delay(1000);*/


  /* Get a new sensor event */ 
  sensors_event_t event;
  tsl.getEvent(&event);
 
  /* Display the results (light is measured in lux) */
  if (event.light)
  {
    Serial.println(event.light);
  }
  else
  {
    /* If event.light = 0 lux the sensor is probably saturated
       and no reliable data could be generated! */
    Serial.println("Sensor overload");
  }
  delay(250);
}






#ifndef _HCSR04_H_
#define _HCSR04_H_

#include <Arduino.h>

//definicion de pins
const int echoPin = 4;     // DI
const int triggerPin = 5;  // DO
const int IRsensorPin = 1; // DI

#define TRIGGER_TIME 10 // us

extern volatile bool measureFlag; // Bandera para indicar que se debe medir la distancia
extern float echoTimeResponse; // Tiempo que se demora en recibir la señal echo
extern float distance_US; // Distancia calculada por el sensor ultrasónico
extern float distance_IR; // Distancia calculada por el sensor infrarrojo
extern volatile bool stopFlagIR;

void Distance_Ultrasonic(void);
void Distance_IR(void);
void timerInterrupt(void);
void IRAM_ATTR stopIRint();

#endif
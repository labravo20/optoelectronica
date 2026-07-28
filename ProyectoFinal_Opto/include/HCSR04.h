#ifndef _HCSR04_H_
#define _HCSR04_H_

#include <Arduino.h>

//definicion de pins
const int echoPin = 4;    // In1
const int triggerPin = 5;    // In2

#define TRIGGER_TIME 10 // us

extern volatile bool measureFlag; // Bandera para indicar que se debe medir la distancia
extern float echoTimeResponse; // Tiempo que se demora en recibir la señal echo
extern float distance; // Distancia calculada

void Distance_Ultrasonic(void);
void timerInterrupt(void);

#endif
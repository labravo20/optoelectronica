#include <Arduino.h>
#ifndef _28BYJ_48_H_

//definicion de pins
const int motorPin1 = 4;    // In1
const int motorPin2 = 5;    // In2
const int motorPin3 = 6;   // In3
const int motorPin4 = 7;   // In4
                   
//definicion variables
extern int motorSpeed;   //variable para fijar la velocidad
extern int stepCounter;     // contador para los pasos
extern int stepsPerRev;  // pasos para una vuelta completa

//secuencia media fase
extern int numSteps;
const int stepsLookup[8] = { B1000, B1100, B0100, B0110, B0010, B0011, B0001, B1001 };

void setOutput(int step);

void clockwise(void);

void anticlockwise(void);

#endif
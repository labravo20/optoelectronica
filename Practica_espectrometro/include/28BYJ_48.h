#ifndef _28BYJ_48_H_
#define _28BYJ_48_H_

#include <Arduino.h>

//definicion de pins
const int motorPin1 = 4;    // In1
const int motorPin2 = 5;    // In2
const int motorPin3 = 6;   // In3
const int motorPin4 = 7;   // In4

const int finalCarreraInt = 16;
const int finalCarreraExt = 17;

extern volatile bool stopFlagExt;
extern volatile bool stopFlagInt;

#define ANTICLOCKWISE 0
#define CLOCKWISE 1

#define DATA_COLLECT 0

                   
//definicion variables
extern int motorSpeed;   //variable para fijar la velocidad
extern int stepCounter;     // contador para los pasos
extern int stepsPerRev;  // pasos para una vuelta completa

extern bool habilitado; // variable para habilitar o deshabilitar el movimiento del motor
extern bool FCint;  // variable para indicar si se ha activado el final de carrera interno
extern bool FCext;  // variable para indicar si se ha activado el final de carrera externo

//secuencia media fase
extern int numSteps;
const int stepsLookup[8] = { B1000, B1100, B0100, B0110, B0010, B0011, B0001, B1001 };

void setOutput(int step);

void clockwise(void);

void anticlockwise(void);

void moveMotor(int steps, bool direction);

void stopMotor(void);

void stopISRext(void);

void stopISRint(void);

void UserStopMotor(void);

#endif
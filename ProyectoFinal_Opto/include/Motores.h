#ifndef _MOTORES_H_
#define _MOTORES_H_

#include <Arduino.h>


//definicion de pins
// Motores izq
#define M_FRONT_IZQ_1 6 // 1 indica rotación en una polaridad - 2 en la polaridad contraria 
#define M_BACK_IZQ_2 9

// Motores der
#define M_FRONT_DER_1 43
#define M_BACK_DER_2 20

#define PIN_SERVO 44


void moveStop(void);      
void moveForward(void); 
void moveBackward(void); 
void turnRight(void); 
void turnLeft(void);    


#endif
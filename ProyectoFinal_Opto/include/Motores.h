#ifndef _MOTORES_H_
#define _MOTORES_H_

#include <Arduino.h>


//definicion de pins
// Motores izq
#define PIN_M_FRONT_IZQ_1 6 // 1 indica rotación en una polaridad - 2 en la polaridad contraria (M1)
#define PIN_M_BACK_IZQ_2 9  // (M3)

// Motores der
#define PIN_M_FRONT_DER_1 43 // (M2)
#define PIN_M_BACK_DER_2 20 // (M4)

#define PIN_SERVO 44

// PWM parameters
#define PWM_FREQ     50    // 50 Hz 
#define PWM_RES      12       // Resolución de 8 bits (0-255)

// PWM channels for H-bridge DRV8833 control
#define PWM_CHANNEL_M1  0  // PWM channel for M1
#define PWM_CHANNEL_M2  1  // PWM channel for M2
#define PWM_CHANNEL_M3  2  // PWM channel for M3
#define PWM_CHANNEL_M4  3  // PWM channel for M4
#define PWM_CHANNEL_SERVO 4 // PWM channel for Servo

#define SERVO_0_DEGREE 205
#define SERVO_45_DEGREE 256
#define SERVO_90_DEGREE 307
#define SERVO_135_DEGREE 358
#define SERVO_180_DEGREE 410




void moveStop(void);      
void moveForward(void); 
void moveBackward(void); 
void turnRight(void); 
void turnLeft(void); 
void servoMoveToangle(uint16_t angle); 
void pinMotorsSetup(void); 


#endif

/* 

20 ms -> duty 100% -> 255
2 ms -> duty 10% -> 180 grados -> 25.5
1.5 ms -> duty 7.5% -> 90 grados -> 19.125
1 ms -> duty 5% -> 0 grados -> 12.75



*/
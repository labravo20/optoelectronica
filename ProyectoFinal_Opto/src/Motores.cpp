#include "Motores.h"

void moveStop()       // Move Stop Function for Motor Driver.
{
  digitalWrite(PIN_M_FRONT_DER_1, LOW);
  digitalWrite(PIN_M_BACK_DER_2, LOW);
  digitalWrite(PIN_M_FRONT_IZQ_1, LOW);
  digitalWrite(PIN_M_BACK_IZQ_2, LOW);
}

void moveForward()    // Move Forward Function for Motor Driver.
{
    digitalWrite(PIN_M_FRONT_DER_1, HIGH);
    digitalWrite(PIN_M_BACK_DER_2, LOW);
    digitalWrite(PIN_M_FRONT_IZQ_1, HIGH);
    digitalWrite(PIN_M_BACK_IZQ_2, LOW);
}

void moveBackward()   // Move Backward Function for Motor Driver.
{
  digitalWrite(PIN_M_FRONT_DER_1, LOW);
  digitalWrite(PIN_M_BACK_DER_2, HIGH);
  digitalWrite(PIN_M_FRONT_IZQ_1, LOW);
  digitalWrite(PIN_M_BACK_IZQ_2, HIGH);
}

void turnRight()      // Turn Right Function for Motor Driver.
{
  digitalWrite(PIN_M_FRONT_DER_1, LOW);
  digitalWrite(PIN_M_BACK_DER_2, HIGH);
  digitalWrite(PIN_M_FRONT_IZQ_1, HIGH);
  digitalWrite(PIN_M_BACK_IZQ_2, LOW);
}

void turnLeft()       // Turn Left Function for Motor Driver.
{
  digitalWrite(PIN_M_FRONT_DER_1, HIGH);
  digitalWrite(PIN_M_BACK_DER_2, LOW);
  digitalWrite(PIN_M_FRONT_IZQ_1, LOW);
  digitalWrite(PIN_M_BACK_IZQ_2, HIGH);
}

void servoMoveToangle(uint16_t angle){
  
  switch (angle)
  {
  case 0:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_90_DEGREE);  
    break;

  case 45:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_45_DEGREE);
    break;
  
  case 90:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_0_DEGREE);
    break;

  case 135: 
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_N45_DEGREE);
    break;

  case 180:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_N90_DEGREE);
    break;

  default:
    break;
  }

}

void pinMotorsSetup(){

  // PWM H-bridge 1 set up
  pinMode(PIN_M_FRONT_IZQ_1, OUTPUT);
  pinMode(PIN_M_BACK_IZQ_2, OUTPUT);

  // PWM H-bridge 2 set up
  pinMode(PIN_M_BACK_DER_2, OUTPUT);
  pinMode(PIN_M_FRONT_DER_1, OUTPUT);

  // PWM Servo set up
  ledcSetup(PWM_CHANNEL_SERVO, PWM_FREQ, PWM_RES);
  ledcAttachPin(PIN_SERVO, PWM_CHANNEL_SERVO);

  ledcWrite(PWM_CHANNEL_SERVO, SERVO_0_DEGREE); 

} 




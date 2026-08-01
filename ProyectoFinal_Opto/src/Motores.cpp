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


    ledcWrite(PWM_CHANNEL_M1, 205);
  delay(2000);
  ledcWrite(PWM_CHANNEL_M1, 256);
  delay(2000);
  ledcWrite(PWM_CHANNEL_M1, 307);
  delay(2000);
  ledcWrite(PWM_CHANNEL_M1, 358);
  delay(2000);
  
  switch (angle)
  {
  case 0:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_0_DEGREE);  
    break;

  case 45:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_45_DEGREE);
    break;
  
  case 90:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_90_DEGREE);
    break;

  case 135: 
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_135_DEGREE);
    break;

  case 180:
    ledcWrite(PWM_CHANNEL_SERVO, SERVO_180_DEGREE);
    break;

  default:
    break;
  }

}

void pinMotorsSetup(){

  /*// PWM H-bridge 1 set up
  ledcSetup(PWM_CHANNEL_M1, PWM_FREQ, PWM_RES);
  ledcAttachPin(PIN_M_FRONT_IZQ_1, PWM_CHANNEL_M1);
  */
  ledcSetup(PWM_CHANNEL_M2, PWM_FREQ, PWM_RES);
  ledcAttachPin(PIN_M_FRONT_DER_1, PWM_CHANNEL_M2);

  // PWM H-bridge 2 set up
  ledcSetup(PWM_CHANNEL_M3, PWM_FREQ, PWM_RES);
  ledcAttachPin(PIN_M_BACK_IZQ_2, PWM_CHANNEL_M3);

  ledcSetup(PWM_CHANNEL_M4, PWM_FREQ, PWM_RES);
  ledcAttachPin(PIN_M_BACK_DER_2, PWM_CHANNEL_M4);

  // PWM Servo set up
  ledcSetup(PWM_CHANNEL_M1, PWM_FREQ, PWM_RES);
  ledcAttachPin(PIN_M_FRONT_IZQ_1, PWM_CHANNEL_M1);

  ledcWrite(PWM_CHANNEL_SERVO, SERVO_0_DEGREE); 

  Serial.println("Motores y servo configurados correctamente");

} 




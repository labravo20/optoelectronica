#include "Motores.h"

void moveStop()       // Move Stop Function for Motor Driver.
{
  digitalWrite(M_FRONT_DER_1, LOW);
  digitalWrite(M_BACK_DER_2, LOW);
  digitalWrite(M_FRONT_IZQ_1, LOW);
  digitalWrite(M_BACK_IZQ_2, LOW);
}

void moveForward()    // Move Forward Function for Motor Driver.
{
    digitalWrite(M_FRONT_DER_1, HIGH);
    digitalWrite(M_BACK_DER_2, LOW);
    digitalWrite(M_FRONT_IZQ_1, HIGH);
    digitalWrite(M_BACK_IZQ_2, LOW);
}

void moveBackward()   // Move Backward Function for Motor Driver.
{
  digitalWrite(M_FRONT_DER_1, LOW);
  digitalWrite(M_BACK_DER_2, HIGH);
  digitalWrite(M_FRONT_IZQ_1, LOW);
  digitalWrite(M_BACK_IZQ_2, HIGH);
}

void turnRight()      // Turn Right Function for Motor Driver.
{
  digitalWrite(M_FRONT_DER_1, LOW);
  digitalWrite(M_BACK_DER_2, HIGH);
  digitalWrite(M_FRONT_IZQ_1, HIGH);
  digitalWrite(M_BACK_IZQ_2, LOW);
}

void turnLeft()       // Turn Left Function for Motor Driver.
{
  digitalWrite(M_FRONT_DER_1, HIGH);
  digitalWrite(M_BACK_DER_2, LOW);
  digitalWrite(M_FRONT_IZQ_1, LOW);
  digitalWrite(M_BACK_IZQ_2, HIGH);
}
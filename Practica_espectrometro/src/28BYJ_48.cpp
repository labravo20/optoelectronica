#include "28BYJ_48.h"

volatile bool stopFlagExt = false;
volatile bool stopFlagInt = false;

//definicion variables
int motorSpeed = 1200;   //variable para fijar la velocidad
int stepCounter = 0;     // contador para los pasos
int stepsPerRev = 4076;  // pasos para una vuelta completa

//secuencia media fase
int numSteps = 8;

bool habilitado = 1;
bool FCint = 0;
bool FCext = 0;

void setOutput(int step)
{
  digitalWrite(motorPin1, bitRead(stepsLookup[step], 0));
  digitalWrite(motorPin2, bitRead(stepsLookup[step], 1));
  digitalWrite(motorPin3, bitRead(stepsLookup[step], 2));
  digitalWrite(motorPin4, bitRead(stepsLookup[step], 3));
}

void clockwise()
{
  stepCounter++;
  if (stepCounter >= numSteps) stepCounter = 0;
  
  setOutput(stepCounter);
}

void anticlockwise()
{
  stepCounter--;
  if (stepCounter < 0) stepCounter = numSteps - 1;
  setOutput(stepCounter);
}


void moveMotor(int steps, bool direction)
{
  //Serial.println("Moving motor ");

  for (int i = 0; i < steps; i++)
  {

   if(FCext || FCint){
     //Serial.println("Motor movement disabled");
     break;
   }

    if (direction) clockwise();
    else anticlockwise();
    
    delayMicroseconds(motorSpeed);
  }
}


void stopMotor()
{
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  
  Serial.println("Motor stopped");
}

void IRAM_ATTR stopISRext() {
  stopFlagExt = true;
  FCext = 1;
}

void IRAM_ATTR stopISRint() {
  stopFlagInt = true;
  FCint = 1;
}


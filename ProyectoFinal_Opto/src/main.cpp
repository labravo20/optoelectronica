#include <Arduino.h>
#include <Wire.h>
#include <HCSR04.h>
#include "Motores.h"
#include <Ticker.h>

Ticker timer_Ultrasonic;

void setup(){
  
  Serial.begin(9600);

  // Declaración de pines
  // Sensor ultrasonido
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);

  digitalWrite(triggerPin, LOW);

  // Sensor infrarrojo
  pinMode(IRsensorPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(IRsensorPin), stopIRint, FALLING);

  pinMode(PIN_M_FRONT_IZQ_1, OUTPUT);
  pinMode(PIN_M_BACK_IZQ_2, OUTPUT);

  digitalWrite(PIN_M_FRONT_IZQ_1, LOW);
  digitalWrite(PIN_M_BACK_IZQ_2, LOW);

  //timer_Ultrasonic.attach(0.1, timerInterrupt);

  //pinMotorsSetup();

  // PWM Servo set up
  //ledcSetup(PWM_CHANNEL_M1, PWM_FREQ, PWM_RES);
  //ledcAttachPin(PIN_M_FRONT_IZQ_1, PWM_CHANNEL_M1);

  //ledcWrite(PWM_CHANNEL_M1, 0); 

}

void loop(){

  //Distance_Ultrasonic();

 /*if(stopFlagIR){
    Serial.println("Objeto detectado por sensor IR");
  stopFlagIR = false; // Bajamos la bandera
  }*/


  /*ledcWrite(PWM_CHANNEL_M1, 205);
  delay(2000);
  ledcWrite(PWM_CHANNEL_M1, 256);
  delay(2000);
  ledcWrite(PWM_CHANNEL_M1, 307);
  delay(2000);
  ledcWrite(PWM_CHANNEL_M1, 358);
  delay(2000);*/


  moveForward();
  delay(2000);


 /* servoMoveToangle(0);
  Serial.println("Servo en 0°");
  delay(1000);
  Serial.println("Servo en 45°");
  servoMoveToangle(45);
  delay(1000);
  servoMoveToangle(90);
  Serial.println("Servo en 90°");
  delay(1000);
  servoMoveToangle(135);
  Serial.println("Servo en 135°");
  delay(1000);
  servoMoveToangle(180);
  Serial.println("Servo en 180°");
  delay(1000);

*/
}

/*
-> Probar la polaridad con los puente H
-> Comprar sensor IR que de datos de distancia
*/


  // funcion que detiene los motores DC

  // Rutina de mapeo con US y motor servo 
    // Funcion lectura en posicion por defecto
    // funcion rotacion a la izq 45°
    // funcion lectura en posicion 
    // rotacion
    // lectura ...

    // Servo rotacion 180° a la der a posicion inicial

    // salida de la rutina es un arreglo de 5 datos. [valor_distancia, angulo]

  // Funcion que recibe el arreglo y determina cual es la mayor distancia y el angulo correspondiente.

  // Rutina de rotacion del servo a la posicion del angulo de la mayor distancia.

    // Funcion que calcula la diff entre la posicion del servo y el angulo de la mayor distancia. Retorna el angulo objetivo.

    // Funcion que toma el angulo objetivo y (en funcion de la tabla) define la activacion de los motores DC

    // Funcion que, una vez en el angulo objetivo, activa los motores DC para continuar el recorrido

  // 03200000000000000000000000000000000000000000000000000....................000000000000000000000000000000000000000000


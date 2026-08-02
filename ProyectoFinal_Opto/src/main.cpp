#include <Arduino.h>
#include <Wire.h>
#include <HCSR04.h>
#include "Motores.h"
#include <Ticker.h>

Ticker timer_Ultrasonic;
  void Rutina_Mapeo(void);

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

  //timer_Ultrasonic.attach(0.1, timerInterrupt);

  pinMotorsSetup();

}

void loop(){

Serial.println("Probando probando");

moveForward();

Rutina_Mapeo();



//digitalWrite(PIN_M_FRONT_DER_1, LOW);

delay(5000);

//digitalWrite(PIN_M_FRONT_DER_1, LOW);

moveBackward();

delay(5000);

turnLeft();

delay(5000);  

turnRight();

delay(5000);




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

  void Rutina_Mapeo(){

  if(stopFlagIR){

    moveStop();

    moveBackward();
    delay(500);

    servoMoveToangle(0);
    distance_measured_0 = Distance_Ultrasonic();
    Serial.println(distance_measured_0);

    servoMoveToangle(45);
    distance_measured_45 = Distance_Ultrasonic();
    Serial.println(distance_measured_45);
    
    servoMoveToangle(90);
    distance_measured_90 = Distance_Ultrasonic();
    Serial.println(distance_measured_90);

    servoMoveToangle(135);
    distance_measured_135 = Distance_Ultrasonic();
    Serial.println(distance_measured_135);

    servoMoveToangle(180);
    distance_measured_180 = Distance_Ultrasonic();
    Serial.println(distance_measured_180);

    servoMoveToangle(0);
    delay(600);

    
    
    stopFlagIR = false; // Bajamos la bandera

    }

  }

  
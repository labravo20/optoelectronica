#include <Arduino.h>
#include <Wire.h>
#include <HCSR04.h>
#include <Ticker.h>

Ticker timer_Ultrasonic;

void setup(){
  
  Serial.begin(9600);

  Serial.println("Serial test");

  // Declaración de pines
  // Sensor ultrasonido
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
/*

Estos motores funcionan con una señal PWM, con un pulso de trabajo entre 1 ms y 2 ms y con un periodo de 20 ms (50 Hz).

*/
  digitalWrite(triggerPin, LOW);

  // Sensor infrarrojo
  pinMode(IRsensorPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(IRsensorPin), stopIRint, FALLING);


  //timer_Ultrasonic.attach(0.1, timerInterrupt);

}

void loop(){

  Distance_Ultrasonic();

  delay(50);

 if(stopFlagIR){
  
  Serial.println("Objeto detectado por sensor IR");

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

  // 

  stopFlagIR = false; // Bajamos la bandera

  }



}

/*
-> Probar la polaridad con los puente H
-> Comprar sensor IR que de datos de distancia
*/
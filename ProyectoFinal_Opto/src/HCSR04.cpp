#include "HCSR04.h"

float echoTimeResponse = 0; // Tiempo que se demora en recibir la señal echo
float distance_US = 0; // Distancia calculada por el sensor ultrasónico
float distance_IR = 0; // Distancia calculada por el sensor infrarrojo
float Voltage_IR = 0;
volatile bool stopFlagIR = false;

volatile bool measureFlag = false;

void timerInterrupt() {
  measureFlag = true; // Levanta la bandera
}

void Distance_Ultrasonic(){

    if(measureFlag){

    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(TRIGGER_TIME);  //Enviamos un pulso de 10us
    digitalWrite(triggerPin, LOW);
    
    echoTimeResponse = pulseIn(echoPin, HIGH); // Obtenemos el ancho del pulso recibido

    distance_US = echoTimeResponse/59;  //escalamos el tiempo a una distancia en cm
    
    //Serial.print("Distancia: ");
    Serial.println(distance_US);      //Enviamos serialmente el valor de la distancia
    //Serial.print("cm");
    //Serial.println();

    measureFlag = false; // Bajamos la bandera  
    }

}

void IRAM_ATTR stopIRint() {
  stopFlagIR = true;
}


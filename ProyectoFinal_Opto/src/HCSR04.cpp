#include "HCSR04.h"

float echoTimeResponse = 0; // Tiempo que se demora en recibir la señal echo
float distance_US = 0; // Distancia calculada por el sensor ultrasónico
float distance_IR = 0; // Distancia calculada por el sensor infrarrojo
float Voltage_IR = 0;
float distance_measured_0 = 0;
float distance_measured_45 = 0;
float distance_measured_90 = 0;
float distance_measured_135 = 0;
float distance_measured_180 = 0;

volatile bool stopFlagIR = false;

volatile bool measureFlag = false;

void timerInterrupt() {
  measureFlag = true; // Levanta la bandera
}

 float Distance_Ultrasonic(){
   
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(TRIGGER_TIME);  //Enviamos un pulso de 10us
    digitalWrite(triggerPin, LOW);
    
    echoTimeResponse = pulseIn(echoPin, HIGH); // Obtenemos el ancho del pulso recibido

    distance_US = echoTimeResponse/59;  //escalamos el tiempo a una distancia en cm
    
    //Serial.println(distance_US);      //Enviamos serialmente el valor de la distancia

    delay(600); // Esperamos 100ms antes de la siguiente medición
    
    return distance_US;
}

void IRAM_ATTR stopIRint() {
  stopFlagIR = true;
}


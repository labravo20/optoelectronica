#include <Arduino.h>
#include "28BYJ_48.h"
#include "GY_2561.h"
#include <Wire.h>

/* I2C comm*/
#define I2C_SDA1 8
#define I2C_SCL1 9
int vuelta = 0;
int steps = 0;
char command;
bool flagInicio;


void Get_data_LuxSensor ();
void StartMotorOperation(bool direction);
void Routine_dataCollection();
void System_Control();
void InitialCondition();

TwoWire I2C_ONE = TwoWire(0);

Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, GY_2561_ADDR);

void setup() {

  // Initialize Serial communication
  Serial.begin(115200);

  //declarar pines como salida
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);

  pinMode(finalCarreraInt, INPUT_PULLDOWN);
  pinMode(finalCarreraExt, INPUT_PULLDOWN);


  attachInterrupt(digitalPinToInterrupt(finalCarreraInt), stopISRint, RISING);

  attachInterrupt(digitalPinToInterrupt(finalCarreraExt), stopISRext, RISING);

  InitialCondition();


  I2C_ONE.begin(I2C_SDA1, I2C_SCL1, 50000);  // I2C Bus 1

  delay(10);

  if(!tsl.begin(&I2C_ONE))
  {
    Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

}

void loop() {

 //moveMotor(stepsPerRev, CLOCKWISE);

  if (Serial.available() > 0) {
    command = Serial.read();

  }

  if(command == 'S') { // Start signal

    Routine_dataCollection();

  }

System_Control();


delay(100);


}


 void Get_data_LuxSensor ()
 {
  /* Get a new sensor event */ 
  sensors_event_t event;
  tsl.getEvent(&event);
 
  /* Display the results (light is measured in lux) */
  if (event.light)
    {
      Serial.println(event.light);
    }
  else
    {
      Serial.println("Sensor saturated");
    }
  
 }

void ModeOperation()  // Inicia el movimiento del motor en una dirección (por definir)
{
  if (Serial.available() > 0) {
    command = Serial.read();

  }



  if(command == 'S') { // Start signal

    Routine_dataCollection();

  }

  /* Hace dos barridos: FCint-FCext toma datos, vuelve a FCint, FCint-FCext toma datos, vuelve a FCext*/
  else if(command == 'P') { //Presicion

    // ---
    return;
  }

  /* Hace dos barridos: Toma datos tanto en ida como en vuelta*/
  else if(command ==  'H'){ // Histeresis 

    // ---
    return;

  }

  else{

    Serial.print("Comando desconocido");
  }

  
}
 

void Routine_dataCollection()
{
  if(flagInicio){

    FCext = 0;
    FCint = 0;
    
    moveMotor(stepsPerRev/2, CLOCKWISE); // Se acerca a la región de interés

    //Serial.print("Flag inicio desactivado" );
    flagInicio = 0; // Se inicia la toma de datos
    Serial.println(flagInicio);    
  }

  if(flagInicio == 0){

    moveMotor(1, CLOCKWISE); // se mueve un paso

    //delay(1); // Tiempo de estabilizacion

    Get_data_LuxSensor();  // Toma de dato
  }

}


void System_Control()
{

  if(stopFlagInt){
    detachInterrupt(digitalPinToInterrupt(finalCarreraInt));
    stopFlagInt = false;    
    //Serial.println("Interrupción FC interno");    
    stopMotor();
    delay(10);
    attachInterrupt(digitalPinToInterrupt(finalCarreraInt), stopISRint, RISING);    
  }

  if(stopFlagExt){
    detachInterrupt(digitalPinToInterrupt(finalCarreraExt));
    stopFlagExt = false;
    FCext = 0;      
    //Serial.println("Interrupción FC externo");    
    stopMotor();
    delay(10);
    attachInterrupt(digitalPinToInterrupt(finalCarreraExt), stopISRext, RISING);    
  }

}

void InitialCondition(){

  if (digitalRead(finalCarreraExt) == HIGH) { // Posicion inicial del barrido
    Serial.println("Condición inicial OKE");
    FCext = 1; // El final de carrera está presionado
  }
  else { //Posicion final del barrido
    Serial.println("No está en posición inicial - Se moverá a la posición inicial");    
    FCint = 0; // El final de carrera está presionado    
    moveMotor(stepsPerRev*3, ANTICLOCKWISE); // Vuelve a la posición inicial del barrido
    Serial.println("Condición inicial OKE");    
  } 

  flagInicio = 1; // Se ha alcanzado la posición inicial, se puede iniciar el proceso de toma de datos
  Serial.print("Flag inicio activado" ); 
  Serial.println(flagInicio);
}
// Que se mueva desde un punto intermedio y toque el final de carrera y se detenga


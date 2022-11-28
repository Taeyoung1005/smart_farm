#include "EmonLib.h"

EnergyMonitor emon1;
int relay1 = 2; //줄어듬
int relay2 = 3; //늘어남
double W;
double MA;
int i = 0;

void extendActuator() {
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, LOW);
}

void retractActuator() {
    digitalWrite(relay1, LOW);
    digitalWrite(relay2, HIGH);
}

void stopActuator() {
    digitalWrite(relay1, LOW);
    digitalWrite(relay2, LOW);
}

void setup()
{
  Serial.begin(9600);
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  emon1.current(A4, 111.1);
}

void loop()
{ 
  //0:줄어듬, 1:늘어남, 2:정지 
  double Irms = emon1.calcIrms(1480);
  W = Irms*220.0;
  MA = Irms*1000;
  char serial_data = Serial.read();
  if(serial_data == '1'){
    retractActuator();
  }
  else if(serial_data == '0'){
    extendActuator();
  }
  else if(serial_data == '2'){
    stopActuator();  
  }
  if (i > 5){
    Serial.println(MA); 
  }
  i++;
}

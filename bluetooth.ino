#include <SoftwareSerial.h>

SoftwareSerial bluetooth(0, 1);
 
void setup(){
  Serial.begin(115200);
  bluetooth.begin(115200);
  Serial.println("bluetooth test");
}
 
void loop(){
  if (Serial.available()) {
    Serial.println(Serial.readStringUntil('\n'));
  }
}

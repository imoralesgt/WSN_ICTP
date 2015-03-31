/*
  Measuring battery voltage
*/

void setup() {
  Serial.begin(9600);
  analogReference(INTERNAL1V5); //Set 1.5V internal reference as Vref+
}

uint16_t sensorValue;

void loop() {
  sensorValue = analogRead(11); //Channel 11 is Vdd/2
  //Serial.println(sensorValue);
  //delay(250);
}

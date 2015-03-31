#include <Enrf24.h>    //NRF24L01 Radio
#include <string.h>    //Strcmp and other string functions
#include <SPI.h>       //Hardware SPI
#include <Wire.h>      //Hardware I2C
#include <BMP085_t.h>  //Pressure and Temperature Sensor
#include <BH1750.h>    //Light sensor
#include <dht11.h>     //Humidity sensor
#include <RTCplus.h>   //Real time clock

#define SENSOR_COUNT 4

//const byte IRQ_PIN      = P2_2; //NRF24L01+ IRQ Pin
const byte CS_PIN      = P2_2; //NRF24L01+ CS Pin
const byte CE_PIN       = P2_0; //NRF24L01+ CE Pin
//const byte CS_PIN       = P2_1; //NRF24L01+ CS Pin
const byte IRQ_PIN       = P2_1; //NRF24L01+ IRQ Pin
const byte HUM_PIN      = P1_4; //DHT11 Data Pin
const byte LED1         = P1_0; //RED LED Pin
const byte ADDR_PINS[3] = {P2_3, P2_4, P2_5};

//const uint16_t RADIO_SPEED = 250000;
const uint16_t RADIO_SPEED = 1000000;

Enrf24 radio(CE_PIN, CS_PIN, IRQ_PIN);  // P2.0=CE, P2.1=CSN, P2.2=IRQ
BMP085<0> PSensor;
BH1750 lightMeter;
dht11 humSensor;
RealTimeClock rtc;

uint8_t rxaddr[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0x01 };
const uint8_t txaddr[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0x00 };
unsigned int TIME_OUT = 10; //Timeout before enabling RX radio
unsigned int now, start;
int32_t sensorData[SENSOR_COUNT]; //Temp, Pres, Lux, Hum


const char *str_on = "ON";
const char *str_off = "OFF";

const char *STR_RQST_DATA = "DATA";
const char *STR_SET_TIMEOUT = "TIMEOUT";


//Prototypes
void dump_radio_status_to_serialport(uint8_t);
void wakeUp();
void dco1MHz();
void dco16MHz();
byte validateTimeOut();
unsigned int timeMinutes();
void radioInit();
void sensorsInit();
void enableRx();
void setLocalAddress(void);

void setup() {
  
  byte j;
  
  for(j=0; j<3; j++){
    pinMode(ADDR_PINS[j], INPUT_PULLUP);
  }
  
  setLocalAddress();
  
  pinMode(PUSH2, INPUT_PULLUP);
  delay(100);
  if(!digitalRead(PUSH2)){
    delay(25);
    if(!digitalRead(PUSH2)){
      TIME_OUT = 1;
    }
  }

  Serial.begin(9600);
  radioInit();
  
  //dump_radio_status_to_serialport(radio.radioState());
  
  pinMode(P1_0, OUTPUT);
  digitalWrite(P1_0, LOW);
  
  enableRx();  // Start listening
  rtc.begin();
  now = timeMinutes();
}

void loop() {
  unsigned int tOut;
  char inbuf[33];
  
  dco16MHz();
  
  radioInit();
  enableRx(); //Start listening

  while (!radio.available(true))
    ;  
  if (radio.read(inbuf)) { //If some data was received
    delay(10);
    tOut = splitBufferToTimeOut(inbuf);
    Serial.println(tOut);
    if (tOut > 0){ 
      TIME_OUT = tOut;
    //if (!strcmp(inbuf, STR_RQST_DATA)){
      //delay(10);
      //Serial.println(inbuf);
      //if (!strcmp(inbuf, STR_RQST_DATA)){ //If header is a DATA Request
         sensorsInit();
         digitalWrite(P1_0, LOW);
              
         humSensor.read(HUM_PIN);
         
         uint16_t hum = humSensor.humidity;
         //int temp = humSensor.temperature*10;
         int16_t temp = PSensor.temperature;
         //temp += PSensor.temperature;
         //temp /= 2;
         //int hum = humSensor.temperature;
         
         uint16_t lux = lightMeter.readLightLevel();
         
         radioInit(); //Init radio as Tx
         radio.setTXaddress((void*)txaddr);
  
         //Temp, Pres, Lux, Hum       
         //sensorData[0] = PSensor.temperature;       //Celsius
         sensorData[0] = temp;       //Celsius
         sensorData[1] = (PSensor.pressure+50)/100; //hPa
         sensorData[2] = lux;                       //Luxes
         sensorData[3] = hum;                       //%HR
  
         
         /*
         Radio data will be sent as:
         MY_ID,TEMP,PRESS,LUX,HUM,HASH
         
         MY_ID <= UNIQUE NODE ID
         TEMP  <= TEMPERATURE*10 (FIXED POINT)
         PRESS <= ATM. PRESSURE (hPa)
         LUX   <= LIGHT METER MEASUREMENT
         HUM   <= RELATIVE HUMIDITY
         */
         
         //long sum = rxaddr[4];
         int i;
         radio.print(rxaddr[4]); //Send my Address
         radio.print(",");
         //radio.print(sensorData[0]/10); //Send temperature
         //radio.print(".");
         //radio.print(sensorData[0]%10); //Send one-digit decimal temperature
         for (i = 0; i < SENSOR_COUNT; i++){ //Send sensor data, excepting temperature
           //sum += sensorData[i];
           radio.print(sensorData[i]);
           radio.print(","); //Comma-separated values
         }
         //byte hash = (sum%256); //Simple hash used as checksum
         //radio.print(hash);
         //radio.print(",");
         radio.flush(); //Send the data that has been put in the radio's output buffer
         digitalWrite(P1_0, LOW); //Data sent, turn LED OFF.
     /*           
      //}else if(!strcmp(inbuf, STR_SET_TIMEOUT)){
      //}else{
        //radioInit(); //Init radio as Tx
        //radio.setTXaddress((void*)txaddr);
  
        //radioInit();
        //enableRx(); //Start listening
        while(strcmp(STR_SET_TIMEOUT, inbuf)){
          radio.read(inbuf); 
        }
        digitalWrite(P1_0, LOW);
        //while (!radio.available(true));
        if (radio.read(inbuf)){
          Serial.println(inbuf);
          TIME_OUT = atoi(inbuf);
          Serial.println(TIME_OUT, DEC);
          //radioInit(); //Init radio as Tx
          //radio.setTXaddress((void*)txaddr);
          //radio.print("OK");
          //radio.flush();
        }
      //} */
    }
  }
  
  
  
  now = timeMinutes();
  start = now;
  while(!validateTimeOut()){ //Periodically check: is it now time to wake up?
    now = timeMinutes();
    dco1MHz(); //Set DCO's speed to 1MHz
    __bis_status_register(LPM1_bits); //Low-Power Mode 1
  } 
}

byte validateTimeOut(){ //Has already passed enough time to wake up?
   unsigned int localNow = now;
   if (start > localNow){ //Just in case an overflow exist
     localNow += 3600; 
   }
   if (localNow < (start + TIME_OUT)){
     return 0;
   }else{
     return 1;
   }
}

void setLocalAddress(void){
  byte addr;
         
  addr = (!digitalRead(ADDR_PINS[0]))   +
         (!digitalRead(ADDR_PINS[1]))*2 +
         (!digitalRead(ADDR_PINS[2]))*4;
  
  //addr = 1; //Just for debugging 
  rxaddr[4] = addr;
}

unsigned int timeMinutes(){
  return rtc.RTC_sec + rtc.RTC_min*60;
}

void wakeUp(){
  __bic_status_register(LPM0_bits); 
}

void dco1MHz(){
  BCSCTL1 = CALBC1_1MHZ;
  DCOCTL = CALDCO_1MHZ;
}

void dco16MHz(){
 BCSCTL1 = CALBC1_16MHZ;
 DCOCTL = CALDCO_16MHZ;  
}

interrupt(TIMER1_A0_VECTOR) Tic_Tac(void){
  rtc.Inc_sec();
  __bic_status_register(LPM1_bits);
};

void enableRx(){
  radio.setRXaddress(rxaddr);
  radio.enableRX();
  digitalWrite(LED1, HIGH);
}

void radioInit(){
  SPI.begin();
  SPI.setDataMode(SPI_MODE0);
  SPI.setBitOrder(MSBFIRST);
  pinMode(IRQ_PIN, INPUT_PULLUP);
  radio.begin(RADIO_SPEED);
}

void sensorsInit(){
  Wire.begin();
  lightMeter.begin();
  PSensor.begin();
  PSensor.refresh();
  PSensor.calculate();
}

unsigned int splitBufferToTimeOut(char *buffer){
  char data[5][33];
  int i = 0;
  char *token;
  char *search = ",";
  token = strtok(buffer, search);
  while(token != NULL){
    strcpy(data[i], token);
    Serial.println(data[i]);
    //data[i] = atoi(token);
    token = strtok(NULL, search);
    i++;
  }
  if(!strcmp(data[0], STR_RQST_DATA)){
    return atoi(data[1]);
  }else{
    return 0;
  }  
}


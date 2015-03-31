#include <RTCplus.h>
#include <Energia.h>

RealTimeClock rtc;
byte now;

void setup(){
  pinMode(RED_LED, OUTPUT);
  digitalWrite(RED_LED, 0);
  pinMode(PUSH2, INPUT_PULLUP);
  rtc.begin();
  now = rtc.RTC_sec;
}

void dco16MHz(){
 BCSCTL1 = CALBC1_16MHZ;
 DCOCTL = CALDCO_16MHZ;  
}

void dco8MHz(){
  BCSCTL1 = CALBC1_8MHZ;
  DCOCTL = CALDCO_8MHZ;
}

void dco1MHz(){
  BCSCTL1 = CALBC1_1MHZ;
  DCOCTL = CALDCO_1MHZ;
}

void loop(){
  if(now == rtc.RTC_sec - 5){
    dco16MHz();
    delay(1);
    now = rtc.RTC_sec;
    
    digitalWrite(RED_LED, 1);
    delay(2);
    digitalWrite(RED_LED, 0);

  }
  dco1MHz();
  __bis_status_register(LPM1_bits);
}

interrupt(TIMER1_A0_VECTOR) Tic_Tac(void){
  rtc.Inc_sec();
  __bic_status_register(LPM1_bits);
};

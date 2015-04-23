# WSN_ICTP
WSN Implemented from scratch. Revision 2 - working at ICTP

===========================================================

ToDo:
+ Node side
  - ```(DONE) Battery measurement and monitoring for each node ```
  - ```(DONE) Low-battery alerting for each node on Exosite```
  - Improve battery lifetime
    * ```(DONE) [Nothing to fix :'(] May be turning sensors off should be the best solution (radios are working great)```
    * Firmware fine-tuning and optimization
  - Design a PCB to allocate MSP430, radio and sensors (without using any Launchpad)
  - 3D-printable case


+ Gateway side
  - ```(DONE) Fix date stamping bug```
  - ```(DONE) Fix bug: data was being sent with previously stored value after a node went offline```
  - ```(DONE) ThingSpeak server @ Raspberry PI [http://angryelectron.com/how-to-install-a-thingspeak-server/]```
  - ```(DONE) Change baudrate between RPi and MSP430 from 9.6kbps to 115.2kbps```
  - ```(DONE) Read sampling period from external text file```
  - ```(DONE) Implement a customized Thingspeak server @ RaspberryPI for local data visualization and exporting capabilities```
  - ```(DONE) Implement a reliable Python class to drive local Thingspeak's client side```
  - ```(DONE) Remove CIK from SC and read it from a text file```
  - ```(DONE) Design a PCB (as a Raspberry PI Hat. Using only MSP430 uC, without any Launchpad)```
  - ```(DONE) Send PCB to a manufacturing service (Seeed, iTead, etc.)```
  - 3D-printable case
  - Highstock graphs for a nice data visualization (http://www.highcharts.com/products/highstock)

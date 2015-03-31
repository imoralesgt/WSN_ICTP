# WSN_ICTP
WSN Implemented from scratch. Revision 2 - working at ICTP

===========================================================

ToDo:
+ Node side
  - Battery measurement, monitoring and alerting for each 
  - Improve battery lifetime
    * May be turning sensors off should be the best solution (radios are working great)
    * Firmware fine-tuning and optimization
  - Design a PCB to allocate MSP430, radio and sensors (without using any Launchpad)
  - 3D-printable case


+ Gateway side
  - Remove CIK from SC and read it from a text file
  - ThingSpeak server @ Raspberry PI
  - Fix date format bug on CSV LOG file
  - Design a PCB (as a Raspberry PI Hat. Using only MSP430 uC, without any Launchpad)
  - 3D-printable case

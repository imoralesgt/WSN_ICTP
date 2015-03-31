EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:CustomDevices
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L NRF24L01+ U1
U 1 1 551A6C3B
P 2300 3350
F 0 "U1" H 2350 3400 60  0001 C CNN
F 1 "NRF24L01+" H 2300 3350 60  0001 C CNN
F 2 "" H 2300 3350 60  0001 C CNN
F 3 "" H 2300 3350 60  0000 C CNN
F 4 "U" H 2300 3050 60  0000 C CNN "Reference"
F 5 "NRF24L01+" H 2300 3650 60  0000 C CNN "Value"
F 6 "" H 2300 3350 60  0000 C CNN "Footprint"
	1    2300 3350
	1    0    0    -1  
$EndComp
$Comp
L LAUNCHPAD U2
U 1 1 551A6CC6
P 4850 3150
F 0 "U2" H 4900 3200 60  0001 C CNN
F 1 "LAUNCHPAD" H 4850 3150 60  0001 C CNN
F 2 "" H 4850 3150 60  0001 C CNN
F 3 "" H 4850 3150 60  0000 C CNN
F 4 "U" H 4850 2000 60  0000 C CNN "Reference"
F 5 "LAUNCHPAD" H 4400 4050 60  0000 C CNN "Value"
F 6 "" H 4850 3150 60  0000 C CNN "Footprint"
	1    4850 3150
	1    0    0    -1  
$EndComp
$Comp
L DIP_SW_4 U?
U 1 1 551A6F41
P 9000 3500
F 0 "U?" H 9050 3550 60  0001 C CNN
F 1 "DIP_SW_4" H 9000 3500 60  0001 C CNN
F 2 "" H 9000 3500 60  0001 C CNN
F 3 "" H 9000 3500 60  0000 C CNN
F 4 "U" H 9000 2950 60  0000 C CNN "Reference"
F 5 "DIP_SW_4" H 9000 3500 60  0000 C CNN "Value"
F 6 "" H 9000 3500 60  0000 C CNN "Footprint"
	1    9000 3500
	1    0    0    -1  
$EndComp
$Comp
L BH1750 U?
U 1 1 551A71AF
P 6550 2900
F 0 "U?" H 6600 2950 60  0001 C CNN
F 1 "BH1750" H 6550 2900 60  0001 C CNN
F 2 "" H 6550 2900 60  0001 C CNN
F 3 "" H 6550 2900 60  0000 C CNN
F 4 "U" H 6550 2900 60  0000 C CNN "Reference"
F 5 "BH1750" H 6550 3000 60  0000 C CNN "Value"
F 6 "" H 6550 2900 60  0000 C CNN "Footprint"
	1    6550 2900
	1    0    0    -1  
$EndComp
$Comp
L BMP180 U?
U 1 1 551A71CD
P 7100 2950
F 0 "U?" H 7150 3000 60  0001 C CNN
F 1 "BMP180" H 7100 2950 60  0001 C CNN
F 2 "" H 7100 2950 60  0001 C CNN
F 3 "" H 7100 2950 60  0000 C CNN
F 4 "U" H 7100 3000 60  0000 C CNN "Reference"
F 5 "BMP180" H 7100 3100 60  0000 C CNN "Value"
F 6 "" H 7100 2950 60  0000 C CNN "Footprint"
	1    7100 2950
	1    0    0    -1  
$EndComp
$Comp
L DHT11 U?
U 1 1 551A7201
P 7600 2900
F 0 "U?" H 7650 2950 60  0001 C CNN
F 1 "DHT11" H 7600 2900 60  0001 C CNN
F 2 "" H 7600 2900 60  0001 C CNN
F 3 "" H 7600 2900 60  0000 C CNN
F 4 "U" H 7600 2900 60  0000 C CNN "Reference"
F 5 "DHT11" H 7600 3000 60  0000 C CNN "Value"
F 6 "" H 7600 2900 60  0000 C CNN "Footprint"
	1    7600 2900
	1    0    0    -1  
$EndComp
NoConn ~ 6350 3150
Text Label 6450 3550 1    60   ~ 0
SDA
Text Label 6550 3550 1    60   ~ 0
SCL
Text Label 6650 3550 1    60   ~ 0
GND
Text Label 6750 3550 1    60   ~ 0
VCC
Text Label 6950 3550 1    60   ~ 0
VCC
Text Label 7050 3550 1    60   ~ 0
GND
Text Label 7150 3550 1    60   ~ 0
SCL
Text Label 7250 3550 1    60   ~ 0
SDA
Text Label 7450 3550 1    60   ~ 0
VCC
Text Label 7550 3550 1    60   ~ 0
DHT11
NoConn ~ 7650 3150
Text Label 7750 3550 1    60   ~ 0
GND
Text Label 6650 4150 1    60   ~ 0
MOSI
Text Label 7000 4150 1    60   ~ 0
SDA
Text Label 6650 4500 1    60   ~ 0
MISO
Text Label 7000 4500 1    60   ~ 0
SCL
NoConn ~ 5500 3100
NoConn ~ 5500 3000
NoConn ~ 5500 2900
NoConn ~ 5500 2800
$Comp
L CONN_01X02 P?
U 1 1 551A748F
P 2700 2100
F 0 "P?" H 2750 2150 60  0001 C CNN
F 1 "CONN_01X02" H 2700 2100 60  0001 C CNN
F 2 "" H 2700 2100 60  0001 C CNN
F 3 "" H 2700 2100 60  0000 C CNN
F 4 "P" H 2700 2250 50  0000 C CNN "Reference"
F 5 "CONN_01X02" V 2800 2100 50  0000 C CNN "Value"
F 6 "" H 2700 2100 60  0000 C CNN "Footprint"
	1    2700 2100
	0    -1   -1   0   
$EndComp
$Comp
L VCC #PWR?
U 1 1 551A74E7
P 2650 2400
F 0 "#PWR?" H 2700 2450 60  0001 C CNN
F 1 "VCC" H 2650 2400 60  0001 C CNN
F 2 "" H 2650 2400 60  0001 C CNN
F 3 "" H 2650 2400 60  0000 C CNN
F 4 "#PWR" H 2650 2250 50  0001 C CNN "Reference"
F 5 "VCC" H 2650 2550 50  0000 C CNN "Value"
F 6 "" H 2650 2400 60  0000 C CNN "Footprint"
	1    2650 2400
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR?
U 1 1 551A7505
P 2750 2400
F 0 "#PWR?" H 2800 2450 60  0001 C CNN
F 1 "GND" H 2750 2400 60  0001 C CNN
F 2 "" H 2750 2400 60  0001 C CNN
F 3 "" H 2750 2400 60  0000 C CNN
F 4 "#PWR" H 2750 2150 50  0001 C CNN "Reference"
F 5 "GND" H 2750 2250 50  0000 C CNN "Value"
F 6 "" H 2750 2400 60  0000 C CNN "Footprint"
	1    2750 2400
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG?
U 1 1 551A7542
P 2200 2250
F 0 "#FLG?" H 2250 2300 60  0001 C CNN
F 1 "PWR_FLAG" H 2200 2250 60  0001 C CNN
F 2 "" H 2200 2250 60  0001 C CNN
F 3 "" H 2200 2250 60  0000 C CNN
F 4 "#FLG" H 2200 2345 50  0001 C CNN "Reference"
F 5 "PWR_FLAG" H 2200 2430 50  0000 C CNN "Value"
F 6 "" H 2200 2250 60  0000 C CNN "Footprint"
	1    2200 2250
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG?
U 1 1 551A7560
P 3150 2250
F 0 "#FLG?" H 3200 2300 60  0001 C CNN
F 1 "PWR_FLAG" H 3150 2250 60  0001 C CNN
F 2 "" H 3150 2250 60  0001 C CNN
F 3 "" H 3150 2250 60  0000 C CNN
F 4 "#FLG" H 3150 2345 50  0001 C CNN "Reference"
F 5 "PWR_FLAG" H 3150 2430 50  0000 C CNN "Value"
F 6 "" H 3150 2250 60  0000 C CNN "Footprint"
	1    3150 2250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 551A766E
P 9350 3800
F 0 "#PWR?" H 9400 3850 60  0001 C CNN
F 1 "GND" H 9350 3800 60  0001 C CNN
F 2 "" H 9350 3800 60  0001 C CNN
F 3 "" H 9350 3800 60  0000 C CNN
F 4 "#PWR" H 9350 3550 50  0001 C CNN "Reference"
F 5 "GND" H 9350 3650 50  0000 C CNN "Value"
F 6 "" H 9350 3800 60  0000 C CNN "Footprint"
	1    9350 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 3150 6450 3550
Wire Wire Line
	6550 3150 6550 3550
Wire Wire Line
	6650 3150 6650 3550
Wire Wire Line
	6750 3150 6750 3550
Wire Wire Line
	6950 3150 6950 3550
Wire Wire Line
	7050 3150 7050 3550
Wire Wire Line
	7150 3150 7150 3550
Wire Wire Line
	7250 3150 7250 3550
Wire Wire Line
	7450 3150 7450 3550
Wire Wire Line
	7550 3150 7550 3550
Wire Wire Line
	7750 3150 7750 3550
Wire Wire Line
	6650 4150 7000 4150
Wire Wire Line
	6650 4500 7000 4500
Wire Wire Line
	2650 2300 2650 2400
Wire Wire Line
	2750 2300 2750 2400
Wire Wire Line
	3150 2250 3150 2350
Wire Wire Line
	3150 2350 2750 2350
Connection ~ 2750 2350
Wire Wire Line
	2200 2250 2200 2350
Wire Wire Line
	2200 2350 2650 2350
Connection ~ 2650 2350
Wire Wire Line
	9350 3750 9350 3800
Wire Wire Line
	8850 3750 9350 3750
Wire Wire Line
	2650 3200 3250 3200
Text Label 3250 3200 2    60   ~ 0
MISO
Wire Wire Line
	2650 3300 3250 3300
Text Label 3250 3300 2    60   ~ 0
SCLK
Wire Wire Line
	2650 3400 3250 3400
Text Label 3250 3400 2    60   ~ 0
CE
$Comp
L GND #PWR?
U 1 1 551A774D
P 3000 3600
F 0 "#PWR?" H 3050 3650 60  0001 C CNN
F 1 "GND" H 3000 3600 60  0001 C CNN
F 2 "" H 3000 3600 60  0001 C CNN
F 3 "" H 3000 3600 60  0000 C CNN
F 4 "#PWR" H 3000 3350 50  0001 C CNN "Reference"
F 5 "GND" H 3000 3450 50  0000 C CNN "Value"
F 6 "" H 3000 3600 60  0000 C CNN "Footprint"
	1    3000 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 3600 3000 3500
Wire Wire Line
	3000 3500 2650 3500
Connection ~ 8950 3750
Connection ~ 9050 3750
Connection ~ 9150 3750
Wire Wire Line
	1950 3200 1500 3200
Text Label 1500 3200 0    60   ~ 0
IRQ
Wire Wire Line
	1950 3300 1500 3300
Text Label 1500 3300 0    60   ~ 0
MOSI
Wire Wire Line
	1950 3400 1500 3400
Text Label 1500 3400 0    60   ~ 0
CS
$EndSCHEMATC

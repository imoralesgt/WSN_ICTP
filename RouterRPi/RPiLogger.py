#Wireless Sensor Network - Architecture School
#Universidad de San Carlos de Guatemala
#Eng. Ivan Rene Morales - October 2014

"""
This module is intended to be run on a Raspberry PI B+
along with an MSP430G2553 Microcontroller-based router station.

Data will be sent from uC to this server via UART (ttyAMA0), and then,
logged on a CSV file (which may be used to automate some stuff later on).
By now, RPi's job is to log and upload real-time data to the Cloud

This script will be launched as a daemon (init.d) and will notify
the uC when system is ready to start logging data.

User interface is done via a CharLCD and a couple of push-buttons.

Using Adafruit_CharLCD and RPi.GPIO libraries to implement GPIO functionality

User will be prompted to enter current date/time only once, everytime
the OS boots.

Some functionality will be also implemented in order to send sensors' data
to exosite (http://www.exosite.com) so readings coming from WSN may be plotted
and seen in real-time from anywhere around the world through fancy good-looking
gauges and displays.
"""

import serial
import time
from exosite import exosite

class GUI(object):
	def __init__(self, rPI = True):
		self.rPI = rPI
		self.PUSH_BUTTONS = (17, 27, 22, 23)
		self.RDY = 24
		self.RST = 25
		if self.rPI:
			import RPi.GPIO as GPIO
			from Adafruit_CharLCD import Adafruit_CharLCD
			self.GPIO = GPIO
			self.lcd = Adafruit_CharLCD()
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(self.RDY, GPIO.OUT)

			#self.setRDYstate(1)

			self.showIntro()

			#self.setRDYstate(0)			

			GPIO.setup(self.RST, GPIO.OUT)
			self.sendRST()
			for i in self.PUSH_BUTTONS:
				GPIO.setup(i, GPIO.IN)

	def readPushButtons(self): #Wire pull-down resistors to each Push-Button
		state = []
		for i in self.PUSH_BUTTONS:
			state.append(self.GPIO.input(i))
		time.sleep(0.150) #Debouncing delay
		for i in range(len(self.PUSH_BUTTONS)):
			state[i] = self.GPIO.input(self.PUSH_BUTTONS[i]) and state[i]
		return state

	def setRDYstate(self, state):
		self.GPIO.output(self.RDY, state)

	def setRSTstate(self, state):
		self.GPIO.output(self.RST, state)

	def sendRST(self):
		self.setRSTstate(0)
		time.sleep(0.01)
		self.setRSTstate(1)

	def lcdClear(self):
		if self.rPI:
			self.lcd.clear()

	def lcdMessage(self, msg):
		if self.rPI:
			self.lcd.message(msg)

	def showIntro(self):
		msg = 'WSN Arquitectura' + '\n' + 'Inicializando...'
		self.lcdClear()
		self.lcdMessage(msg)
		time.sleep(4)


class logger(object):

	RF_TIMEOUT = 120 #Timeout seconds between MSP430 uC
	CIK = '8f3af3df6ee1ea3340ef9897ca6c139a160859e6'

	def __init__(self, rPI = True, url = ""):
		self.url = url
		self.rPI = rPI
		self.fileName = self.getFileName()
		self.exo = exosite(self.CIK)

		if rPI:
			#self.PORT = '/dev/ttyACM0'
			self.PORT = '/dev/ttyAMA0'
			
		else:
			self.PORT = 'COM54'

		self.BAUDRATE = 9600
		self.TIMEOUT = self.RF_TIMEOUT + 10
		self.openSerial()

		self.gui = GUI(self.rPI)

		self.gui.setRDYstate(1)
		self.gui.setRDYstate(0)

		time.sleep(0.5)

		self.sendTimeOut()


	def openSerial(self):
		try:
			self.uart = serial.Serial(self.PORT, self.BAUDRATE, timeout = self.TIMEOUT)
			self.uart.flushInput()
			self.uart.flushOutput()
			return 1
		except:
			print "Error al abrir puerto serial " + self.PORT
			return None

	def readSerial(self):
		try:
			#self.uart.write('a')
			data = self.uart.readline()
			return data
		except:
			print "Error al leer puerto serial " + self.PORT
			return None

	def closeSerial(self):
		try:
			self.uart.close()
			return 1
		except:
			print "Error al cerrar puerto serial " + self.PORT
			return None


	def sendTimeOut(self):
		self.uart.write(str(self.RF_TIMEOUT) + ';')

	def cleanSerialData(self, data):
		ALLOWED_CHARACTERS = [32, 35, 44]
		ALLOWED_CHARACTERS.extend(range(48,58))
		ALLOWED_CHARACTERS.extend(range(65,91))
		ALLOWED_CHARACTERS.extend(range(97,123))

		newData = ''

		for i in data:
			if ord(i) in ALLOWED_CHARACTERS:
				newData += i
		return newData


	def fixTemperatureFormat(self, data):
		splitData = data.split(',')
		if len(splitData) > 1:
			temp = splitData[1]
			temp = int(temp)
			newTemp = temp / 10.0
			newTemp = str(newTemp)
			splitData[1] = newTemp
			newString = ''
			for dt in splitData:
				newString += dt + ','
			return newString[:-1]
		else:
			return data

	def appendData(self, data):
		try:
			archivo = open(self.fileName, 'a')
			dateTime = self.getCurrentDate() + ',' + self.getCurrentDateTime()[3]
			data = dateTime + ',' + data
			archivo.write(data)
			archivo.close()
		except:
			archivo.close()

	def uploadData(self, data):
		if(self.exo.formatAndUpdateData(data)):
			self.exo.pushData()
		else:
			'No se puede subir a Exosite!'

	def getRPi(self):
		return self.rPI

	def translateDate(self, day, month, year):
		MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
		return str(year)+str(MONTHS.index(month)+2)+str(day)

	def translateTime(self, time):
		timeSplit = time.split(':')
		time = timeSplit[0]+timeSplit[1]+timeSplit[2]
		return time

	def getCurrentDateTime(self):
		dateTime = time.ctime()
		s = dateTime.split(' ')
		c = []
		for i in s:
			if len(i):
				c.append(i)
		return c

	def getCurrentTime(self):
		return self.translateTime(self.getCurrentDateTime()[3]) #Return current time

	def getCurrentDate(self):
		dateTime = self.getCurrentDateTime()
		dateTime = self.translateDate(dateTime[2], dateTime[1], dateTime[4])
		return dateTime

	def getFileName(self):
		return '/home/pi/WSN/' + self.getCurrentDate() + '_' + self.getCurrentTime() + '.csv'		


log = logger(True)
try:
	log.gui.setRDYstate(0)
	while True:
		data = log.readSerial()
		data = log.cleanSerialData(data)
		data = log.fixTemperatureFormat(data)
		data += '\n'
		if len(data) > 3:
			log.appendData(data)
			log.uploadData(data[:-1])
			print data,
			log.gui.lcdClear()
			log.gui.lcdMessage(str(data))
		else:
			log.gui.sendRST()
			time.sleep(1)
			log.sendTimeOut()
			print "WDT RESET!"
			now = log.getCurrentTime()
			while(log.getCurrentTime() != now):
				pass
		#time.sleep(1)
#except KeyboardInterrupt or TypeError or AttributeError:
except KeyboardInterrupt:
	log.gui.setRDYstate(1)
	log.closeSerial()
	print "Adios!"


'''
To set date + time:
sudo date -s "07 NOV 2014 11:30:00"
'''

import urllib 
import httplib
import socket

#DEBUG = True
DEBUG = False

class exosite(object):

	SERVER  = 'm2.exosite.com'

	VARIABLES = ('temperatura', 'presion', 'humedad', 'luminosidad')

	def __init__(self, CIK, setOfSensorAliases = {}):
		
		self.CIK = CIK
		self.sensors = setOfSensorAliases

	def getSensors(self):
		return self.sensors

	def updateSensor(self, sensor, value):
		self.sensors[sensor] = value

	def addSensor(self, sensor, value):
		self.updateSensor(sensor, value)

	def removeSensor(self, sensor):
		if sensor in self.sensors.keys():
			del self.sensors[sensor]
			return 1
		else:
			return 0

	def clearSensors(self):
		del self.sensors
		self.sensors = {}

	def formatAndUpdateData(self, data):
		try:
			data = data.split(',')
			if DEBUG:
				print 'DATA: ' + str(data)
			if len(data) > 1:
				data = data[:-1]
				node = data[0]
				temp = float(data[1])
				pres = int(data[2])
				lux  = int(data[3])
				hum  = int(data[4])
				collectedData = [temp, pres, hum, lux]
				newData = {}
				j = 0
				for i in self.VARIABLES:
					newData[i] = collectedData[j]
					j += 1
				for i in newData:
					self.updateSensor(str(i) + str(node), newData[i])
				'''
				self.updateSensor('temperatura'+str(node),temp)
				self.updateSensor('presion'+str(node),pres)
				self.updateSensor('humedad'+str(node),hum)
				self.updateSensor('luminosidad'+str(node),lux)
				'''
				return True
			else:
				node = int(data[0].split("#")[-1]) #If "SIN RESPUESTA DE ESTACION #xxxx" was read from Serial Port
				if DEBUG:
					print 'Sin respuesta!  Nodo #' + str(node) #Just for debugging purposes
				temp = None
				pres = None
				lux = None
				hum = None
				for i in self.VARIABLES:
					self.removeSensor(i+str(node))
				'''
				self.removeSensor('temperatura'+str(node))
				self.removeSensor('presion'+str(node))
				self.removeSensor('humedad'+str(node))
				self.removeSensor('luminosidad'+str(node))
				'''
				return False
		except Exception as e:
			if DEBUG:
				print e
			return None

	def pushData(self):
		params = urllib.urlencode(self.sensors)
		conn = httplib.HTTPConnection(self.SERVER)
		conn.set_debuglevel(0)
		url = '/api:v1/stack/alias'
		headers = {'X-Exosite-CIK': self.CIK, 'content-type': 'application/x-www-form-urlencoded; charset=utf-8'} 
		try:
			conn.request("POST", url, params, headers)
			response = conn.getresponse();
			data = response.read()
			end = data.find('<')
			if -1 == end: end = len(data)
			conn.close()
		except KeyboardInterrupt:
			print 'Adios!'
			exit()
		except:
			print "Sin conexion a Internet. Almacenando localmente..."

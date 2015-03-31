import urllib 
import httplib
import socket

class exosite(object):

	SERVER  = 'm2.exosite.com'

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
			data = data.split(',')[:-1]
			if len(data) > 1:
				node = data[0]
				temp = float(data[1])
				pres = int(data[2])
				lux  = int(data[3])
				hum  = int(data[4])
				self.updateSensor('temperatura'+str(node),temp)
				self.updateSensor('presion'+str(node),pres)
				self.updateSensor('humedad'+str(node),hum)
				self.updateSensor('luminosidad'+str(node),lux)
				return True
			else:
				return False
		except:
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

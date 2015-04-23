import httplib, urllib
import os

class KeysFile(object): #Reliably access to API Keys file and return them as a list
    def __init__(self, apikeysFileName = 'thingSpeak.key'):
        self.keys = [] #API write keys for each channel will be stored here
        try:
            self.__readKeysFromFile(self.__getKeyFile(apikeysFileName))
        except IOError:
            print 'Archivo con API Keys no encontrado!'
            print 'ThingSpeak no puede ser utilizado.'

    '''
    Private methods
    '''

    def __getKeyFile(self, fName): #Run this only once. Open file operation
        fileName = str(os.path.dirname(os.path.realpath(__file__))) + '/' + fName
        keyFile = open(fileName, 'r')
        return keyFile

    def __readKeysFromFile(self, keyFile): #Run this only once after 'getKeyFile'
        for key in keyFile:
            self.__addKey(key.rstrip('\n\r')) #Add keys to self.keys through encapsulation with addKey method
        keyFile.close()

    def __addKey(self, key):
        self.keys.append(key)

    '''
    Public method
    '''

    def getKeys(self): #Return key list to wherever it's requested from
        return self.keys

class Channels(object):

    VARIABLES = ('Temperatura', 'Presion', 'Luuminosidad', 'Humedad', 'Bateria')

    def __init__(self, serverAddr = "127.0.0.1:3000"):
        self.keys = KeysFile().getKeys()
        self.serverAddr = serverAddr
        self.channelList = []
        self.__buildChannels()

    '''
    Private methods
    '''

    def __getServerAddr(self):
        return self.serverAddr

    def __getKeys(self):
        return self.keys

    def __addChannel(self, channel):
        self.channelList.append(channel)

    def __buildChannels(self):
        for k in self.__getKeys():
            self.__addChannel(channel(k, 'N/A', self.__getServerAddr()))

    def __getChannels(self):
        return self.channelList

    '''
    Public methods
    '''

    def formatAndUpdateData(self, data):
        try:
            data = data.split(',')
            if len(data) > 1:
                data = data[:-1]
                node = data[0]
                temp = float(data[1])
                pres = int(data[2])
                lux  = int(data[3])
                hum  = int(data[4])
                bat  = int(data[5])
                collectedData = [temp, pres, hum, lux, bat]
                return node, collectedData
            else:
                return None, None
        except:
            print 'No se puede subir a Thingspeak. Datos corruptos'

    def updateChannel(self, channelIndex, values, lat = None, long = None, elevation = None, status = None):
        '''
        - Channel index starts from 0, as they are stored in a list
        - Values is a list or tuple containing the data that needs to be sent
        '''
        ch = self.__getChannels()[channelIndex]
        try:
            ch.update(values)
        except httplib.socket.error:
            print 'No se puede alcanzar al servidor. Abortando...'

class TooManyFields(ValueError):
    pass

def non_null_values(**kwargs):
        return [(k,v) for (k,v) in kwargs.iteritems() if v != None]

class channel(object):

    FIELD_KEYS = ['field' + str(n) for n in xrange(1,9)] #Make a list of fields using Thingspeak's format
    HEADERS = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

    def __init__(self, writeKey, cid, server):
        """writeKey is the Write API Key.
        cid is the read_key"""
        self.writeKey = writeKey
        self.cid      = cid
        self.server   = server

    def update(self, field_vals, Lat=None, Long=None, Elevation=None, Status=None):
        if len(field_vals) > 8:
            raise TooManyFields('update can only handle 8 field values per channel')
        # this verbosity, rather than just using kwargs,
        # so that callers get a prompt error if they supply an arg `update` cannot handle
        named_args = non_null_values(Lat=Lat, Long=Long, Elevation=Elevation, Status=Status)
        params = urllib.urlencode(zip(self.FIELD_KEYS, field_vals) + [('key', self.writeKey)] + named_args)
        #conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn = httplib.HTTPConnection(self.server)
        conn.request("POST", "/update", params, self.HEADERS)
        response = conn.getresponse()
        conn.close()
        return response

    def fetch(self, format):
        #conn = httplib.HTTPConnection("anpi.thingspeak.com:80")
        conn = httplib.HTTPConnection(self.server)
        path = "/channels/{0}/feed.{1}".format(self.cid, format)
        params = urllib.urlencode([('key',self.cid)])
        conn.request("GET", path, params, self.HEADERS)
        response = conn.getresponse()
        return response


if __name__ == "__main__":
    from random import randint
    thing = Channels('192.168.88.195:3000')
    print 'Channel keys:' + str(thing.keys)
    for i in range(len(thing.keys)):
        thing.updateChannel(i,[randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)])
        print 'Updated channel ' + str(i)

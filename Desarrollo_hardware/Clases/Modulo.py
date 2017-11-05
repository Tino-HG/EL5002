import paho.mqtt.publish as publish

class claseModulo(object) :

	def __init__(self) :
		#cada modulo tiene como maximo 1 sensor y un numero "ilimitado" de actuadores
		self.isActivated = False
		self.sensorTopic = ""
		self.actuatorsTopic = ""
		self.sensor = None
		self.actuators = []

	def addSensor(self,ID) :
		#este metodo agrega un sensor al modulo, hace un broadcast en el topic "config" de MQTT
		#con un mensaje que contiene la ID del sensor que se quiere agregar. El sensor que
		#tenga la ID contenida en el mensaje luego comenzara a publicar su estado en el topic
		#self.sensorTopic

		return

	def addActuator(self,ID) :
		return

	def currentState(self) :
		return

	def activate(self) :
		self.isActivated = True

	def deactivate(self) :
		self.isActivated = False

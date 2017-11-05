import Modulo

class claseLuces(Modulo.claseModulo) :

	def __init__(self,habitacion) :
		Modulo.claseModulo.__init__(self)
		self.sensorTopic = 'sensor_luces_%s' % habitacion
		self.actuatorsTopic = 'actuators_luces_%s' % habitacion

	def lightsOn(self) :
		#este metodo envia una senal al actuador (ESP conectado a rele) para que prenda la luz
		return

	def lightsOff(self) :
		#este metodo envia una senal al actuador (ESP conectado a rele) para que apague la luz
		return


import Modulo

class claseCortinas(Modulo.claseModulo) :

	def __init__(self,habitacion):
		Modulo.claseModulo.__init__(self)
		self.sensorTopic = 'sensor_cortinas_%s' % habitacion
		self.actuatorsTopic = 'actuators_cortinas_%s' % habitacion
	
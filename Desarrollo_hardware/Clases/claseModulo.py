
class Modulo(object) :

	def __init__(self) :
		self.isActivated = False
		self.sensor = None
		self.actuators = []

	def addSensor(self,ID) :
		return

	def addActuator(self,ID) :
		return

	def currentState(self) :
		return

	def activate(self) :
		self.isActivated = True

	def deactivate(self) :
		self.isActivated = False

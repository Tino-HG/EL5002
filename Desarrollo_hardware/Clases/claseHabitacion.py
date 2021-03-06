import moduloCortinas
import moduloLuces
from threading import Thread


class Habitacion(Thread):

	def __init__(self, nombreHabitacion):
		Thread.__init__(self)
		self.nombre = nombreHabitacion
		self.cortinas = None
		self.luces = None

	def addModules(self, tipoModulo):
		if tipoModulo=='Cortinas':
			if self.cortinas==None :
				self.cortinas = moduloCortinas.Cortinas()
				print ('%s: Modulo Cortinas agregado con exito.' % self.nombre)
			else:
				print ('%s: Este modulo ya existe (%s)' % (self.nombre, tipoModulo))
		elif tipoModulo=='Luces':
			if self.luces==None :
				self.luces = moduloLuces.Luces()
				print ('%s: Modulo Luces agregado con exito.' % self.nombre)
			else:
				print ('%s: Este modulo ya existe (%s)' % (self.nombre, tipoModulo))
		else:
			print ('%s: Error en tipo de modulo en habitacion. Ingresar Cortinas o Luces' % self.nombre)

	def run(self):
   		self.cortinas.activate()
   		self.luces.activate()
   		return
    	
import moduloCortinas
import moduloLuces
from threading import Thread


class claseHabitacion(Thread):

	def __init__(self, nombreHabitacion):
		Thread.__init__(self)
		self.nombre = nombreHabitacion
		self.cortinas = None
		self.luces = None

	def addModules(self, tipoModulo):
		if tipoModulo=='Cortinas':
			if self.cortinas==None :
				self.cortinas = moduloCortinas.claseCortinas(self.nombre)
				print ('%s: Modulo Cortinas agregado con exito.' % self.nombre)
			else:
				print ('%s: Este modulo ya existe (%s)' % (self.nombre, tipoModulo))
		elif tipoModulo=='Luces':
			if self.luces==None :
				self.luces = moduloLuces.claseLuces(self.nombre)
				print ('%s: Modulo Luces agregado con exito.' % self.nombre)
			else:
				print ('%s: Este modulo ya existe (%s)' % (self.nombre, tipoModulo))
		else:
			print ('%s: Error en tipo de modulo en habitacion. Ingresar Cortinas o Luces' % self.nombre)

	def run(self):
		if self.cortinas != None :
   			self.cortinas.activate()
   		if self.luces != None :
   	   		self.luces.activate()
   		#while True:
   		#	pass
   		return
    	
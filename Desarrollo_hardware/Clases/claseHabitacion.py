import moduloCortinas
import moduloLuces
from threading import Thread


class habitacion(Thread):

    def __init__(self, nombreHabitacion):
 		Thread.__init__(self)
 		self.nombre = nombreHabitacion
 		self.cortinas = None
 		self.luces = None


 	def addModules(self, tipoModulo):
 		if tipoModulo=='Cortinas':
 			self.cortinas = moduloCortinas()
 		elif tipoModulo=='Luces':
 			self.luces = moduloCortinas()
 		else
 			print ('%s Error en tipo de modulo en habitacion %d . Ingresar Cortinas o Luces' % self.nombre)

    def run(self):
    	#Activo ambos modulos(?)
    	#cortinas.activate
    	#luces.activate
    	return
    	
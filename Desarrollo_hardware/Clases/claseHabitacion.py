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
 			if self.cortinas!=None :
 				self.cortinas = moduloCortinas()
 			else:
 				print ('Este modulo ya existe')
 		elif tipoModulo=='Luces':
 			if self.luces!=None :
 				self.luces = moduloCortinas()
 			else:
 				print ('Este modulo ya existe')
 		else:
 			print ('%s Error en tipo de modulo en habitacion %d . Ingresar Cortinas o Luces\n' % self.nombre)

    def run(self):
    	#Activo ambos modulos(?)
    	#cortinas.activate
    	#luces.activate
    	return
    	
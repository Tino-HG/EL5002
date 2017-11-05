import moduloCortinas
import moduloLuces
from threading import Thread


class Habitacion(Thread):

<<<<<<< HEAD
    def __init__(self, nombreHabitacion):
        Thread.__init__(self)
        self.nombre = nombreHabitacion
        self.cortinas = None
        self.luces = None
=======
	def __init__(self, nombreHabitacion):
		Thread.__init__(self)
		self.nombre = nombreHabitacion
		self.cortinas = None
		self.luces = None
>>>>>>> origin/master

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

<<<<<<< HEAD
    def addModules(self, tipoModulo):
        if tipoModulo=='Cortinas':
            self.cortinas = moduloCortinas()
        elif tipoModulo=='Luces':
            self.luces = moduloCortinas()
        else:
            print ('%s Error en tipo de modulo en habitacion %d . Ingresar Cortinas o Luces' % self.nombre)

    def run(self):
    	#Activo ambos modulos(?)
    	#cortinas.activate
    	#luces.activate
    	return
    	
=======
	def run(self):
   		#Activo ambos modulos(?)
   		#cortinas.activate
   		#luces.activate
   		return
    	
>>>>>>> origin/master

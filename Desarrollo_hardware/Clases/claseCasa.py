import claseHabitacion

class casa(object):

    def __init__(self):
 		self.habitaciones = []

 	def addRoom(self, nombre)
 	# 'nombre' corresponde al nombre o numeracion designada a la habitacion (arbitrario)
 		self.habitacion = claseHabitacion(nombre)
 		self.habitacion.start()
 		self.habitacion.join()
 		self.habitaciones.append(self.habitacion)

 	def showRooms(self)
 		for i in self.habitaciones
 			print (i.nombre)

 	def showModulesInRooms(self)
 		for i in self.habitaciones
 			if i.cortinas!=None && i.luces!=None :
 				x = 'Cortinas/Luces'
 			elif i.cortinas!=None :
 				x = 'Cortinas'
 			elif i.luces!=None :
 				x += 'Luces'
 			else
 				x = 'Vacia'
 			print (i.nombre + ' ' + x)

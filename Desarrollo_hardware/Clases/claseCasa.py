import claseHabitacion

class casa(object):

    def __init__(self) :
 		self.habitaciones = []

 	def addRoom(self, nombre) :
 	# 'nombre' corresponde al nombre o numeracion designada a la habitacion (arbitrario)
 		for room in self.habitaciones :
 			if nombre == room.nombre :
 				print ('Esta habitacion ya existe, intente con otro nombre\n')
 				return
 		habitacion = claseHabitacion(nombre)
 		habitacion.start()
 		habitacion.join()
 		self.habitaciones.append(nombre)

 	def addModule(self,habitacion,modulo) :
 		for room in self.habitaciones :
 			if habitacion == room.nombre :
 				room.addModules(modulo)
 				return
 		print ('Esta habitacion no existe.')


 	def showRooms(self) :
 		for i in self.habitaciones :
 			print (i.nombre)

 	def showModulesInRooms(self) :
 		for i in self.habitaciones :
 			if i.cortinas!=None && i.luces!=None :
 				x = 'Cortinas/Luces'
 			elif i.cortinas!=None :
 				x = 'Cortinas'
 			elif i.luces!=None :
 				x += 'Luces'
 			else
 				x = 'Vacia'
 			print (i.nombre + ' ' + x + '\n')

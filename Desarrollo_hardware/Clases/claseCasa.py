import claseHabitacion

class Casa(object) :

	def __init__(self) :
		print ('Entorno CASA inicializado')
		self.habitaciones=[]

	def addRoom(self, nombre) :
	# 'nombre' corresponde al nombre o numeracion designada a la habitacion (arbitrario)
		for room in self.habitaciones :
			if nombre == room.nombre :
				print ('%s: Esta habitacion ya existe, intente con otro nombre' % nombre)
				return
		habitacion = claseHabitacion.Habitacion(nombre)
		habitacion.start()
		habitacion.join()
		self.habitaciones.append(habitacion)
		print ('Habitacion %s agregada con exito.' % nombre)

 	def addModule(self,habitacion,modulo) :
		for room in self.habitaciones :
			if habitacion == room.nombre :
				room.addModules(modulo)
				return
		print ('Esta habitacion no existe (%s).' % habitacion)

	def showRooms(self):
		print('--------------------------\nLista de Habitaciones')
		for i in self.habitaciones :
			print (i.nombre)
		print('--------------------------')

	def showModulesInRooms(self) :
		for i in self.habitaciones :
			if i.cortinas!=None and i.luces!=None :
				x = 'Cortinas/Luces'
			elif i.cortinas!=None :
				x = 'Cortinas'
			elif i.luces!=None :
				x = 'Luces'
			else :
				x = 'Vacia'
			print (i.nombre + ': ' + x )

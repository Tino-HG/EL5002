import moduloCortinas
import moduloLuces
import habitacion
from threading import Thread

class casa(object):

    def __init__(self):
        self.habitaciones = []

    def addRoom(self, nombre):
        self.habitaciones.append(habitacion(nombre))
        # 'nombre' corresponde al nombre o numeracion designada a la habitacion (arbitrario)

    def showRooms(self):
        for i in self.habitaciones :
            print (i.nombre)

    def showModulesInRooms(self):
        for i in self.habitaciones:
            if i.cortinas!=None :
                x = 'Cortinas  '
            elif i.luces!=None :
                x = x + 'Luces'
            else:
                x = 'Vacia'
            print (i.nombre + ' ' + x)

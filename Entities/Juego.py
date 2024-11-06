from Entities import Aventurero
from Entities import Mision
class Juego():
    def __init__(self):
        self.__aventureros = []
        self.__misiones = []
    #Metodos
    def registrar_aventurero(self, aventurero):
        self.__aventureros.append(aventurero)
    
    def registrar_mision(self, mision):
        self.__misiones.append(mision)

    def realizar_mision(self, nombre_mision):
        mision = None
        for m in self.__misiones:
            if m.get_nombre() == nombre_mision:
                mision = m
                break
        if not mision:
            print("Misión no encontrada!")
            return
        if mision.is_completado():
            print("Esta mision ya ha sido completada!")
            return
    
    #Solicitar ID de participantes hasta que no haya mas
    participantes = []
    while True:
        id_aventurero = input("Ingrese el ID del aventurero (o 'fin' para terminar): ")
        if id_aventurero == 'fin':
            break

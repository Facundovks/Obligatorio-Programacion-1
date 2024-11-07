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
    #Buscar la misión por su nombre
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

            aventurero = None
            for a in self.__aventureros:
                if "" + (a.get_id()) == id_aventurero:
                    aventurero = a
                    break
            if aventurero == False:
                print("El aventurero no existe!")
                return
            #Validar que el rango del aventurero esté acorde al rango de la misión
            #if aventurero.get_puntos_de_habilidad() < mision.get_rango()??
        #Ver si se cumplen los requisitos de la mision
        if mision.get_tipo() == "grupal" and len(participantes) < mision.get_min_miembros():
            print("No hay suficientes aventureros para realizar la misión!")
            return
        #Si se cumple todo, completar la mision
        mision.completar_mision()
        recompensa_por_aventurero = mision.get_recompensa() / len(participantes)
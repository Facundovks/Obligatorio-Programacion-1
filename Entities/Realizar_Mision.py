from Entities import Aventurero
from Entities import Mision
from Entities import Mago
from Entities import Ranger
from Entities import Guerrero

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
        #Matriz con los valores de cada rango
        rangos = [[1, 20],[21, 40], [41,60], [61,80], [81, 100]]
        while True:
            id_aventurero = input("Ingrese el ID del aventurero (o 'fin' para terminar): ")
            if id_aventurero == 'fin':
                break

            aventurero = None
            for a in self.__aventureros:
                if str(a.get_id()) == id_aventurero:
                    aventurero = a
                    break
            if aventurero == False:
                print("El aventurero no existe!")
                return
            #Validar que el rango del aventurero esté acorde al rango de la misión
            for a in self.__aventureros:
                if aventurero.get_clase() == "Ranger":
                    if rangos[1][0] > aventurero.get_puntos_de_habilidad() + Ranger.get_puntos_habilidad:
                        print("El rango de su Ranger es 1")
                    elif rangos[2][0] > aventurero.get_puntos_de_habilidad() + Ranger.get_puntos_habilidad:
                        print("El rango de su Ranger es 2")
                    elif rangos[3][0] > aventurero.get_puntos_de_habilidad() + Ranger.get_puntos_habilidad:
                        print("El rango de su Ranger es 3")
                    elif rangos[4][0] > aventurero.get_puntos_de_habilidad() + Ranger.get_puntos_habilidad:
                        print ("El rango de su Ranger es 4")
                    elif rangos[4][0] <= aventurero.get_puntos_de_habilidad():
                        print ("El rango de su Ranger es 5")
                elif aventurero.get_clase == "Mago":
                    if rangos[1][0] > aventurero.get_puntos_de_habilidad() + Mago.get_mana/10:
                        print("El rango de su Mago es 1")
                    elif rangos[2][0] > aventurero.get_puntos_de_habilidad() + Mago.get_mana/10:
                        print("El rango de su Mago es 2")
                    elif rangos[3][0] > aventurero.get_puntos_de_habilidad() + Mago.get_mana/10:
                        print("El rango de su Mago es 3")
                    elif rangos[4][0] > aventurero.get_puntos_de_habilidad() + Mago.get_mana/10:
                        print("El rango de su Mago es 4")
                    elif rangos[4][0] <= aventurero.get_puntos_de_habilidad() + Mago.get_mana/10:
                        print("El rango de su Mago es 5")
                elif aventurero.get_clase == "Guerrero":
                    if rangos[1][0] > aventurero.get_puntos_de_habilidad() + Guerrero.get_fuerza/2:
                        print("El rango de su Guerrero es 1")
                    elif rangos[2][0] > aventurero.get_puntos_de_habilidad() + Guerrero.get_fuerza/2:
                        print("El rango de su Guerrero es 2")
                    elif rangos[3][0] > aventurero.get_puntos_de_habilidad() + Guerrero.get_fuerza/2:
                        print("El rango de su Guerrero es 3")
                    elif rangos[4][0] > aventurero.get_puntos_de_habilidad() + Guerrero.get_fuerza/2:
                        print("El rango de su Guerrero es 4")
                    elif rangos[4][0] <= aventurero.get_puntos_de_habilidad() + Guerrero.get_fuerza/2:
                        print("El rango de su Guerrero es 5")
                    
                #Ver si se cumplen los requisitos de la mision
                if mision.get_tipo() == "grupal" and len(participantes) < mision.get_min_miembros():
                    print("No hay suficientes aventureros para realizar la misión!")
                    return
                #Si se cumple todo, completar la mision
                mision.completar_mision()
                recompensa_por_aventurero = mision.get_recompensa() / len(participantes)
                for p in participantes:
                    p.set_dinero(recompensa_por_aventurero + p.get_dinero)
                    if mision.get_rango() == 1:
                        p.set_experiencia(5 + p.get_experiencia)
                    if mision.get_rango() == 2:
                        p.set_experiencia(10 + p.get_experiencia)
                    if mision.get_rango() == 3:
                        p.set_experiencia(20 + p.get_experiencia)
                    if mision.get_rango() == 4:
                        p.set_experiencia(50 + p.get_experiencia)
                    if mision.get_rango() == 5:
                        p.set_experiencia(100 + p.get_experiencia)
from Realizar_Mision import Juego

def ver_top_5_misiones_con_mas_recompensa(self):
    #Ordenar las misiones de mayor a menor, segun su rango (experiencia), en caso de mismo rango, ordenar alfabeticamente
    n = len(Juego.self.__misiones)
    for i in range(n):
        max_m = i
        for j in range(i+1, n):
            if (Juego.self.__misiones[j].get_rango() > Juego.self.__misiones[i].get_rango())or \
                (Juego.self.__misiones[j].get_rango() == Juego.self.__misiones[i].get_rango) and \
                (Juego.self.__misiones[j].get_nombre() > Juego.self.__misiones[i].get_nombre()):
                max_m = j
        #Intercambiar los rankings 
        Juego.self.__aventureros_con_misiones_completadas[i], Juego.self.__aventureros_con_misiones_completadas[max_m] = Juego.self.__aventureros_con_misiones_completadas[max_m] , Juego.self.__aventureros_con_misiones_completadas[i]
    top_5 = Juego.self.__misiones[:5]
    for i in top_5:
        print(f"{i+1}-{top_5[i]}")
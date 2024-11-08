from Realizar_Mision import Juego

def ver_top_10_aventureros_con_mas_misiones_resueltas(self):
    self.__aventureros_con_misiones_completadas = []
    #Filtrar aventureros con misiones completadas
    for aventurero in Juego.self.__aventureros:
        if aventurero.get_experiencia() == 0:
            print("El aventurero no tiene misiones completadas")
            return
        else: 
            self.__aventureros_con_misiones_completadas.append(aventurero)
            return
    if not self.__aventureros_con_misiones_completadas:
        print("No hay aventureros con misiones completadas")
        return
    #Ordenar los aventureros de mayor a menor, segun su experiencia, en caso de misma experiencia, ordenar alfabeticamente
    n = len(self.__aventureros_con_misiones_completadas)
    for i in range(n):
        max_a = i
        for j in range(i + 1, n):
            if (self.__aventureros_con_misiones_completadas[j].get_experiencia() > self.__aventureros_con_misiones_completadas[i].get_experiencia())or \
                (self.__aventureros_con_misiones_completadas[j].get_experiencia() == self.__aventureros_con_misiones_completadas[i].get_experiencia) and \
                (self.__aventureros_con_misiones_completadas[j].get_nombre() > self.__aventureros_con_misiones_completadas[i].get_nombre()):
                max_a = j
                
        #Intercambiar los rankings si se cumple el if
        self.__aventureros_con_misiones_completadas[i], self.__aventureros_con_misiones_completadas[max_a] = self.__aventureros_con_misiones_completadas[max_a] , self.__aventureros_con_misiones_completadas[i]
    top_10 = self.__aventureros_con_misiones_completadas[:10]
    for i in top_10:
        print(f"{i+1}-{top_10[i]}")
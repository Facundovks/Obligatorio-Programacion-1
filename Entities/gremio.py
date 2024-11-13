from .aventurero import Aventurero
from .Guerrero import Guerrero
from .Mago import Mago
from .Mision import Mision
from .Ranger import Ranger, Mascota


def registrar_aventurero(nombre, id, clase, puntos_habilidad, experiencia, dinero):
    try:
        if not (1 <= puntos_habilidad <= 100 or 1 <= experiencia or 1 <= dinero):
            print("Error: Los puntos de habilidad deben estar entre 1 y 100.")
            return
        if clase == "Guerrero":
            fuerza = input("Ingrese la fuerza del Guerrero ")

            if not (1 <= int(fuerza) <= 100):
                print("Error: La fuerza del Guerrero debe estar entre 1 y 100.")
                return
            aventurero = Guerrero(
                nombre, id, puntos_habilidad, experiencia, int(dinero), int(fuerza)
            )

        elif clase == "Mago":
            mana = input("Ingrese el mana del mago ")
            if not (1 <= int(mana) <= 1000):
                print("Error: El mana del Mago debe estar entre 1 y 1000.")
                return
            aventurero = Mago(
                nombre, id, puntos_habilidad, experiencia, dinero, int(mana)
            )

        elif clase == "Ranger":
            nombre_mascota = input("Ingrese el nombre de la mascota")
            puntos_mascota = input("Ingrese los puntos de la mascota")
            if int(puntos_mascota) > 0 and int(puntos_mascota) < 51:
                mascota = Mascota(nombre_mascota, int(puntos_mascota))
                aventurero = Ranger(
                    nombre, id, puntos_habilidad, experiencia, dinero, mascota
                )

        else:
            print("Clase no válida.")
            return

        print(f"Aventurero {nombre} registrado con éxito.")
        return aventurero
    except ValueError as e:
        print(f"Error de entrada: {e}")


def registrar_mision(nombre, rango, recompensa, completado, tipo, min_miembros):
    try:
        if not isinstance(completado, bool):
            raise ValueError(
                "El parámetro 'completado' debe ser un valor booleano (True o False)."
            )

        if tipo not in ["grupal", "individual"]:
            raise ValueError("El parámetro 'tipo' debe ser 'grupal' o 'individual'.")

        if tipo == "grupal" and (min_miembros is None or min_miembros <= 0):
            raise ValueError(
                "Para una misión grupal se debe especificar el número mínimo de miembros."
            )

        if rango < 1 or rango > 5:
            raise ValueError("Rango no es valido")

        mision = Mision(nombre, rango, recompensa, completado, tipo, min_miembros)

        print(f"Misión '{nombre}' registrada con éxito!")
        return mision

    except ValueError as e:
        print(f"Error al ingresar los datos de la misión: {e}")


def calcular_habilidad(aventurero):
    if isinstance(aventurero, Guerrero):
        return aventurero.get_puntos_habilidad() + aventurero.get_fuerza() / 2
    elif isinstance(aventurero, Mago):
        return aventurero.get_puntos_habilidad() + aventurero.get_mana() / 10
    elif isinstance(aventurero, Ranger):
        puntos_mascota = (
            aventurero.get_mascota().get_puntos_habilidad()
            if aventurero.get_mascota()
            else 0
        )
        return aventurero.get_puntos_habilidad() + puntos_mascota
    else:
        return 0


def ordenar_por_habilidad_y_experiencia(aventureros):
    aventureros_ordenados = sorted(
        aventureros,
        key=lambda aventurero: (
            -calcular_habilidad(aventurero),
            aventurero.get_experiencia(),
            aventurero.get_nombre(),
        ),
    )
    return aventureros_ordenados


def mostrar_top_10(aventureros):
    aventureros_ordenados = ordenar_por_habilidad_y_experiencia(aventureros)
    print("Top 10 Aventureros por Mayor Habilidad:")
    for i, aventurero in enumerate(aventureros_ordenados[:10]):
        print(f"{i+1}. {aventurero.get_nombre()} - {type(aventurero).__name__}")
        print(f"   Habilidad total: {calcular_habilidad(aventurero)}")
        print(f"   Experiencia: {aventurero.get_experiencia()}")
        print(f"   Dinero: {aventurero.get_dinero()}")
        print("")

def opcion_realizar_mision(aventureros,misiones):
    nombre_mision = str(input("Escriba el nombre de la mision: "))
    mision = None
    for m in misiones:
        if m.get_nombre() == nombre_mision:
            mision = m
            break
    if not mision:
        print("Misión no encontrada!")
        return
    if mision.is_completado():
        print("Esta mision ya ha sido completada!")
        return
    
    participantes = []
    rangos = [[1, 20],[21, 40], [41,60], [61,80], [81, 100]]
    while True:
        id_aventurero = input("Ingrese el ID del aventurero (o 'fin' para terminar): ")
        if id_aventurero == 'fin':
            break

        aventurero = None
        for a in aventureros:
            if str(a.get_id()) == id_aventurero:
                aventurero = a
                participantes.append(aventurero)
                break
        if not aventurero:
            print("El aventurero no existe!")
            return

        for a in aventureros:
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
                    
            if mision.get_tipo() == "grupal" and len(participantes) < mision.get_min_miembros():
                print("No hay suficientes aventureros para realizar la misión!")
                return
            mision.completar_mision()
            recompensa_por_aventurero = mision.get_recompensa() / len(participantes)
            for p in participantes:
                p.set_dinero(recompensa_por_aventurero + p.get_dinero())
                if mision.get_rango() == 1:
                    p.set_experiencia(5 + p.get_experiencia())
                if mision.get_rango() == 2:
                    p.set_experiencia(10 + p.get_experiencia())
                if mision.get_rango() == 3:
                    p.set_experiencia(20 + p.get_experiencia())
                if mision.get_rango() == 4:
                    p.set_experiencia(50 + p.get_experiencia())
                if mision.get_rango() == 5:
                    p.set_experiencia(100 + p.get_experiencia())

def ver_top_10_aventureros_con_mas_misiones_resueltas(aventureros):
    aventureros_con_misiones_completadas = []
    for aventurero in aventureros:
        if aventurero.get_experiencia() == 0:
            print("El aventurero no tiene misiones completadas")
            return
        else: 
            aventureros_con_misiones_completadas.append(aventurero)
            return
    if not aventureros_con_misiones_completadas:
        print("No hay aventureros con misiones completadas")
        return
    n = len(aventureros_con_misiones_completadas)
    for i in range(n):
        max_a = i
        for j in range(i + 1, n):
            if (aventureros_con_misiones_completadas[j].get_experiencia() > aventureros_con_misiones_completadas[i].get_experiencia())or \
                (aventureros_con_misiones_completadas[j].get_experiencia() == aventureros_con_misiones_completadas[i].get_experiencia) and \
                (aventureros_con_misiones_completadas[j].get_nombre() > aventureros_con_misiones_completadas[i].get_nombre()):
                max_a = j
                
        aventureros_con_misiones_completadas[i], aventureros_con_misiones_completadas[max_a] = aventureros_con_misiones_completadas[max_a] , aventureros_con_misiones_completadas[i]
    top_10 = aventureros_con_misiones_completadas[:10]
    for i in top_10:
        print(f"{i+1}-{top_10[i]}")

def ver_top_5_misiones_con_mas_recompensa(misiones):
    n = len(misiones)
    for i in range(n):
        max_m = i
        for j in range(i+1, n):
            if (misiones[j].get_dinero() > misiones[i].get_dinero())or \
                (misiones[j].get_dinero() == misiones[i].get_dinero) and \
                (misiones[j].get_nombre() > misiones[i].get_nombre()):
                max_m = j
        misiones[i], misiones[max_m] = misiones[max_m] , misiones[i]
    top_5 = misiones[:5]
    for i in top_5:
        print(f"{i+1}-{top_5[i]}")
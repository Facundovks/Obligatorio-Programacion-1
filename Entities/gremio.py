from .aventurero import Aventurero
from .Guerrero import Guerrero
from .Mago import Mago
from .Mision import Mision
from .Ranger import Ranger, Mascota


def registrar_aventurero(nombre, id, clase, puntos_habilidad, experiencia, dinero):
    try:
        if not (1 <= puntos_habilidad <= 100 and 1 <= experiencia and 1 <= dinero):
            print("Error: Datos ingresados inaválidos.")
            return None
        if clase == "Guerrero":
            fuerza = input("Ingrese la fuerza del Guerrero ")

            if not (1 <= int(fuerza) <= 100):
                print("Error: La fuerza del Guerrero debe estar entre 1 y 100.")
                return None
            aventurero = Guerrero(
                nombre, id, puntos_habilidad, experiencia, int(dinero), int(fuerza)
            )

        elif clase == "Mago":
            mana = input("Ingrese el mana del mago ")
            if not (1 <= int(mana) <= 1000):
                print("Error: El mana del Mago debe estar entre 1 y 1000.")
                return None
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
            return None

        print(f"Aventurero {nombre} registrado con éxito.")
        return aventurero
    except ValueError as e:
        print(f"Error de entrada: {e}")
        return None


def registrar_mision(nombre, rango, recompensa, completado, tipo, min_miembros):
    try:
        if not isinstance(completado, bool):
            print(
                "El parámetro 'completado' debe ser un valor booleano (True o False)."
            )
            return None

        if tipo not in ["grupal", "individual"]:
            raise ValueError("El parámetro 'tipo' debe ser 'grupal' o 'individual'.")

        if tipo == "grupal" and (min_miembros is None or min_miembros <= 0):
            print(
                "Para una misión grupal se debe especificar el número mínimo de miembros."
            )
            return None

        if rango < 1 or rango > 5:
            print("Rango no es valido") 
            return None

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


def ver_top_10_aventureros_con_mas_misiones_resueltas(aventureros):
    aventureros_con_misiones_completadas = []

    for aventurero in aventureros:
        if aventurero.get_misiones_completadas() > 0:
            aventureros_con_misiones_completadas.append(aventurero)
        

    if not aventureros_con_misiones_completadas:
        print("No hay aventureros con misiones completadas.")
        return

    n = len(aventureros_con_misiones_completadas)
    for i in range(n):
        max_a = i
        for j in range(i + 1, n):
            if (
                aventureros_con_misiones_completadas[j].get_misiones_completadas()
                > aventureros_con_misiones_completadas[i].get_misiones_completadas()
            ) or (
                aventureros_con_misiones_completadas[j].get_misiones_completadas()
                == aventureros_con_misiones_completadas[i].get_misiones_completadas()
                and aventureros_con_misiones_completadas[j].get_nombre()
                > aventureros_con_misiones_completadas[i].get_nombre()
            ):
                max_a = j

        (
            aventureros_con_misiones_completadas[i],
            aventureros_con_misiones_completadas[max_a],
        ) = (
            aventureros_con_misiones_completadas[max_a],
            aventureros_con_misiones_completadas[i],
        )

    top_10 = aventureros_con_misiones_completadas[:10]

    for i, aventurero in enumerate(top_10):
        print(
            f"{i + 1} - {aventurero.get_nombre()} con {aventurero.get_misiones_completadas()} misiones resueltas"
        )


def ver_top_5_misiones_con_mas_recompensa(misiones):
    n = len(misiones)

    for i in range(n):
        max_m = i
        for j in range(i + 1, n):
            if misiones[j].get_recompensa() > misiones[max_m].get_recompensa():
                max_m = j
            elif misiones[j].get_recompensa() == misiones[max_m].get_recompensa():
                if misiones[j].get_nombre() > misiones[max_m].get_nombre():
                    max_m = j
        misiones[i], misiones[max_m] = misiones[max_m], misiones[i]

    top_5 = misiones[:5]

    for i, m in enumerate(top_5):
        print(
            f"{i + 1} - {m.get_nombre()} con recompensa: {m.get_recompensa()} monedas"
        )

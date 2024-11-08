from aventurero import Aventurero
from Guerrero import Guerrero
from Mago import Mago
from Mision import Mision
from Ranger import Ranger, Mascota


def registrar_aventurero( nombre, id, clase, puntos_habilidad, experiencia, dinero
):
    try:
        if not (1 <= puntos_habilidad <= 100):
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
            aventurero = Mago(nombre, id, puntos_habilidad, experiencia, dinero, int(mana))

        elif clase == "Ranger":
            nombre_mascota= input("Ingrese el nombre de la mascota")
            puntos_mascota=input("Ingrese los puntos de la mascota")
            if (int(puntos_mascota) > 0 and int(puntos_mascota) < 51):
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

juan=registrar_aventurero(
    "Juan", 1, "Guerrero", 80, 1500, 200.0
)
print(juan)
import sys
from Exceptions.ErrorMision import ErrorMisión
from Exceptions.ErrorAventurero import ErrorAventurero
from Entities.gremio import (
    registrar_aventurero,
    registrar_mision,
    mostrar_top_10,
    ver_top_10_aventureros_con_mas_misiones_resueltas,
    ver_top_5_misiones_con_mas_recompensa,
)
from Entities.aventurero import Aventurero
from Entities.Guerrero import Guerrero
from Entities.Mago import Mago
from Entities.Mision import Mision
from Entities.Ranger import Ranger, Mascota

aventureros = [
    Guerrero("Aventurero1", 1, 80, 150, 100.0, 50),
    Mago("Aventurero2", 2, 60, 200, 120.5, 500),
    Ranger("Aventurero3", 3, 70, 120, 80.0, Mascota("Fido", 30)),
    Guerrero("Aventurero4", 4, 90, 300, 250.0, 75),
    Mago("Aventurero5", 5, 85, 400, 200.0, 700),
    Ranger("Aventurero6", 6, 50, 100, 50.0, Mascota("Bella", 45)),
    Guerrero("Aventurero7", 7, 40, 50, 60.0, 20),
    Mago("Aventurero8", 8, 55, 180, 90.0, 300),
    Ranger("Aventurero9", 9, 65, 130, 150.0, Mascota("Rocky", 20)),
    Guerrero("Aventurero10", 10, 95, 500, 500.0, 85),
]

misiones = [
    Mision("Exploración en las Montañas", 3, 1500.0, False, "individual", None),
    Mision("Defensa del Castillo", 2, 2500.0, True, "grupal", 4),
    Mision("Rescate en el Bosque", 1, 800.0, False, "individual", None),
    Mision("Asalto a la Fortaleza Oscura", 5, 5000.0, False, "individual", None),
    Mision("Caza de Dragón", 4, 4000.0, False, "grupal", 3),
    Mision("Expedición a las Ruinas Antiguas", 2, 2200.0, True, "grupal", 5),
    Mision("Protección de la Aldea", 3, 1700.0, True, "grupal", 2),
    Mision("Investigación de Magia Oscura", 4, 3500.0, False, "individual", None),
    Mision("Toma de la Torre Maldita", 5, 6000.0, True, "grupal", 6),
    Mision("Misión de Exploración Subterránea", 1, 1000.0, False, "individual", None),
]


def mostrar_menu():
    print("\nBienvenido al Simulador de Gremio de Aventureros!")
    print("Seleccione una opción:")
    print("1. Registrar Aventurero")
    print("2. Registrar Misión")
    print("3. Realizar Misión")
    print("4. Otras Consultas")
    print("5. Salir")


def opcion_registrar_aventurero():
    nombre = input("Ingrese el nombre del aventurero: ")
    id_ = int(input("Ingrese el id del aventurero: "))
    for aventurero in aventureros:
        if aventurero.get_id() == id_:
            print("Error: El ID ingresado ya está en uso. Por favor, ingrese un ID único.")
            return 
    clase = input("Ingrese la clase del aventurero(Guerrero,Mago,Ranger): ")
    puntos_habilidad = int(
        input("Ingrese los puntos de habilidad del aventurero(1 a 100): ")
    )
    experiencia = int(input("Ingrese la experiencia del aventurero: "))
    dinero = int(input("Ingrese el dinero del aventurero: "))

    aventurero=registrar_aventurero(nombre, id_, clase, puntos_habilidad, experiencia, dinero)
    if (aventurero != None):
        aventureros.append(aventurero)


def opcion_registrar_mision():

    nombre = input("Ingrese el nombre de la mision: ")
    rango = int(input("Ingrese el rango de la mision(1 a 5)): "))
    recompensa = int(input("Ingrese la recompensa de la mision: "))
    completado = bool(input("Ingrese si la mision esta completada o no(1 para si/vacio para no) "))
    Tipo = input("Ingrese el tipo de mision(grupal, individual) ")
    min_miembros = int(input("Ingrese el minimo de miembros(vacio si individual): "))

    mision=registrar_mision(nombre, rango, recompensa, completado, Tipo, min_miembros)
    if (mision != None):
        misiones.append(mision)

def opcion_realizar_mision():
    try:
        nombre_mision = str(input("Escriba el nombre de la mision: "))
        mision = None
        for m in misiones:
            if m.get_nombre() == nombre_mision:
                mision = m
                break
        if not mision:
            print("Misión no encontrada!")
            raise ErrorMisión()
        if mision.is_completado():
            print("Esta mision ya ha sido completada!")
            raise ErrorMisión()

        participantes = []
        rangos = [[1, 20], [21, 40], [41, 60], [61, 80], [81, 100]]
        while True:
            id_aventurero = str(input("Ingrese el ID del aventurero (o 'fin' para terminar): "))
            aventurero = None
            if id_aventurero == "fin":
                    break
            for a in aventureros:            
                if str(a.get_id()) == id_aventurero:
                    aventurero = a
                    if mision.get_tipo() == "individual" and len(participantes) >= 1:
                        print("Esta es una misión individual, ya no se pueden agregar más aventureros.")
                        raise ErrorAventurero()
                    participantes.append(aventurero)

                
            if not aventurero:
                print("El aventurero no existe!")
                raise ErrorAventurero()

            for p in participantes:
                if p.get_clase() == "Ranger":
                    if (
                        rangos[1][0]
                        > p.get_puntos_habilidad() + p.get_puntos_habilidad()
                    ):
                        print("El rango de su Ranger es 1")      
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_puntos_habilidad():
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero             
                    elif (
                        rangos[2][0]
                        > p.get_puntos_habilidad() + p.get_puntos_habilidad()
                    ):
                        print("El rango de su Ranger es 2")      
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_puntos_habilidad():
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero             
                    elif (
                        rangos[3][0]
                        > p.get_puntos_habilidad() + p.get_puntos_habilidad()
                    ):
                        print("El rango de su Ranger es 3")  
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_puntos_habilidad():
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero                  
                    elif (
                        rangos[4][0]
                        > p.get_puntos_habilidad() + p.get_puntos_habilidad()
                    ):
                        print("El rango de su Ranger es 4")     
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_puntos_habilidad():
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero              
                    elif rangos[4][0] <= p.get_puntos_habilidad():
                        print("El rango de su Ranger es 5") 
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_puntos_habilidad():
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero                  
                elif p.get_clase() == "Mago":
                    if (
                        rangos[1][0]
                        > p.get_puntos_habilidad() + p.get_mana() / 10
                    ):
                        print("El rango de su Mago es 1")   
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_mana() / 10:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero                 
                    elif (
                        rangos[2][0]
                        > p.get_puntos_habilidad() + p.get_mana() / 10
                    ):
                        print("El rango de su Mago es 2")    
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_mana() / 10:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero               
                    elif (
                        rangos[3][0]
                        > p.get_puntos_habilidad() + p.get_mana() / 10
                    ):
                        print("El rango de su Mago es 3")     
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_mana() / 10:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero             
                    elif (
                        rangos[4][0]
                        > p.get_puntos_habilidad() + p.get_mana() / 10
                    ):
                        print("El rango de su Mago es 4")   
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_mana() / 10:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero               
                    elif (
                        rangos[4][0]
                        <= p.get_puntos_habilidad() + p.get_mana() / 10
                    ):
                        print("El rango de su Mago es 5")   
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_mana() / 10:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero                
                elif p.get_clase() == "Guerrero":
                    if (
                        rangos[1][0]
                        > p.get_puntos_habilidad() + p.get_fuerza() / 2
                    ):
                        print("El rango de su Guerrero es 1")      
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_fuerza() / 2:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero             
                    elif (
                        rangos[2][0]
                        > p.get_puntos_habilidad() + p.get_fuerza() / 2
                    ):
                        print("El rango de su Guerrero es 2")     
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_fuerza() / 2:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero            
                    elif (
                        rangos[3][0]
                        > p.get_puntos_habilidad() + p.get_fuerza() / 2
                    ):
                        print("El rango de su Guerrero es 3")   
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_fuerza() / 2:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero
                    elif (
                        rangos[4][0]
                        > p.get_puntos_habilidad() + p.get_fuerza() / 2
                    ):
                        print("El rango de su Guerrero es 4")
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_fuerza() / 2:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero
                        
                    elif (
                        rangos[4][0]
                        <= p.get_puntos_habilidad() + p.get_fuerza() / 2
                    ):
                        print("El rango de su Guerrero es 5")      
                        if mision.get_rango() > p.get_puntos_habilidad() + p.get_fuerza() / 2:
                            print("El aventurero no tiene el rango suficiente!")
                            raise ErrorAventurero

        if (
                mision.get_tipo() == "grupal"
                and len(participantes) < mision.get_min_miembros()
            ):
                print("No hay suficientes aventureros para realizar la misión!")
                raise ErrorAventurero()

        mision.completar_mision()
        print("Se completó la misión")
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
            p.completar_mision()
                
    except (ErrorAventurero, ErrorMisión) as e:
        print(f"Se produjo un error: {e}")


def opcion_otras_consultas():
    while True:
        print("\nOtras Consultas:")
        print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
        print("2. Ver Top 10 Aventureros con Mayor Habilidad")
        print("3. Ver Top 5 Misiones con Mayor Recompensa")
        print("4. Volver al Menú Principal")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ver_top_10_aventureros_con_mas_misiones_resueltas(aventureros)
            elif opcion == 2:
                mostrar_top_10(aventureros)
            elif opcion == 3:
                ver_top_5_misiones_con_mas_recompensa(misiones)
            elif opcion == 4:
                return
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")


def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                opcion_registrar_aventurero()
            elif opcion == 2:
                opcion_registrar_mision()
            elif opcion == 3:
                opcion_realizar_mision()
            elif opcion == 4:
                opcion_otras_consultas()
            elif opcion == 5:
                print("¡Hasta luego!")
                sys.exit()
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    main()
    
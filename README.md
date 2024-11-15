Este es un Simulador de Gremios de Aventureros inspirado en los juegos tipo Dungeons and Dragons. El programa permite gestionar un grupo de aventureros, registrar y realizar misiones, y hacer diversas consultas sobre los miembros del gremio (aventureros) y las misiones.
El sistema permite registrar tres tipos diferentes de aventureros: Guerrero, Ranger y Mago, tambien permite el registro de misiones, las cuales pueden ser inidivuduales o grupales. Además el programa calcula las habilidades de los aventureros, asigna experiencia segun el 
rango de la misión completada y distribuye recompensas a partir de la misión completada.
El simulador es controlado completamente desde la terminal mediante un menú interactivo basado en opciones numéricas.
El diagrama UML esta conformado por una entidad "gremio" en donde se encuentran todos los métodos (menos el "Realizar misión, ubciado en el Main) a exponer en el módulo "Main". Un módulo que contiene la clase Misión en donde se encuentra el acceso a la información sobre sus características (el nombre(str), el rango(int),
si está completada o no (Bool), su recompensa(int), si es grupal o individual(str) y el mínimo de miembros necesarios para completarla(int). Por otro lado, se encuentra la clase "Aventureros", en la cual también está el acceso a la información de los aventureros en general
(su nombre(str), su id_(único)(int), sus puntos de habilidad(int) su experiencia()int, cantidad de misiones(int) y su dinero(double)). Luego, se desprenden de la clase "Aventureros". tres clases: "Guerrero", "Ranger" y "Mago"; éstas heredan los atributos de "Aventureros" y tienen tambien
características propias: El "Guerrero" posee el atributo fuerza (int), el "Ranger" tiene una Mascota con nombre(str) y puntos de hablididad(int), por último, el "Mago" tiene la maná como atributo(int).

Para ejecutarlo debe ejecutar el main.py dentro de visual studio

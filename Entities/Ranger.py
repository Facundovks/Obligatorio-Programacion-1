from .aventurero import Aventurero

class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        self._nombre = nombre
        self._puntos_habilidad = puntos_habilidad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_puntos_habilidad(self):
        return self._puntos_habilidad
    
    def set_puntos_habilidad(self, puntos_habilidad):
        self._puntos_habilidad = puntos_habilidad

class Ranger(Aventurero):
    def __init__(self, nombre, id_, puntos_habilidad, experiencia, dinero, mascota=None):
        super().__init__(nombre, id_,"Ranger", puntos_habilidad, experiencia, dinero)
        self._mascota = mascota

    def get_mascota(self):
        return self._mascota
    
    def set_mascota(self, mascota):
        self._mascota = mascota

    def __str__(self):

        if self._mascota:
            return f"Ranger: {self._nombre}, ID: {self._id}, Puntos de Habilidad: {self._puntos_habilidad}, Experiencia: {self._experiencia}, Dinero: {self._dinero}, Mascota: ({self._mascota})"
        else:
            return f"Ranger: {self._nombre}, ID: {self._id}, Puntos de Habilidad: {self._puntos_habilidad}, Experiencia: {self._experiencia}, Dinero: {self._dinero}, Mascota: No tiene mascota"
        
      
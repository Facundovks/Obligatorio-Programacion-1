from .aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, id_, puntos_habilidad, experiencia, dinero, fuerza):
        super().__init__(nombre, id_, "Guerrero", puntos_habilidad, experiencia, dinero) 
        self._fuerza = fuerza

    def get_fuerza(self):
        return self._fuerza
    
    def set_fuerza(self, fuerza):
        self._fuerza = fuerza

    def __str__(self):
        return f"Nombre del guerrero: {self._nombre}, ID: {self._id}, Fuerza: {self._fuerza}, Puntos de Habilidad: {self._puntos_habilidad}, Experiencia: {self._experiencia}, Dinero: {self._dinero}"

from abc import ABC, abstractmethod

class Aventurero(ABC):
    def __init__(self, nombre, clase, id_, puntos_habilidad, experiencia, dinero):
        self._nombre = nombre
        self._clase = clase
        self._id = id_
        self._puntos_habilidad = puntos_habilidad
        self._experiencia = experiencia
        self._dinero = dinero

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_clase(self):
        return self._clase
    
    def set_clase(self, clase):
        self._clase = clase

    def get_id(self):
        return self._id
    
    def set_id(self, id_):
        self._id = id_

    def get_puntos_habilidad(self):
        return self._puntos_habilidad
    
    def set_puntos_habilidad(self, puntos_habilidad):
        self._puntos_habilidad = puntos_habilidad

    def get_experiencia(self):
        return self._experiencia
    
    def set_experiencia(self, experiencia):
        self._experiencia = experiencia

    def get_dinero(self):
        return self._dinero
    
    def set_dinero(self, dinero):
        self._dinero = dinero
    
    @abstractmethod
    def __str__(self):
        pass
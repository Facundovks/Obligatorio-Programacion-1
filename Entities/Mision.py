class Mision:
    def __init__(self, nombre, rango, recompensa, completado, tipo, min_miembros=None):
        self._nombre = nombre
        self._rango = rango
        self._recompensa = recompensa
        self._completado = completado
        self._tipo = tipo
        self._min_miembros = min_miembros if tipo == "grupal" else None

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_rango(self):
        return self._rango
    
    def set_rango(self, rango):
        self._rango = rango

    def get_recompensa(self):
        return self._recompensa
    
    def set_recompensa(self, recompensa):
        self._recompensa = recompensa

    def is_completado(self):
        return self._completado
    
    def completar_mision(self):
        self._completado = True

    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_min_miembros(self):
        return self._min_miembros
    
    def set_min_miembros(self, min_miembros):
        self._min_miembros = min_miembros 
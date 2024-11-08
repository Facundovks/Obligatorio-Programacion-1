from .aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, id_, puntos_habilidad, experiencia, dinero, mana):
        super().__init__(nombre, id_, "Mago", puntos_habilidad, experiencia, dinero)
        self._mana = mana

    def get_mana(self):
        return self._mana
    
    def set_mana(self, mana):
        self._mana = mana

    def __str__(self):
        return f"Mago: {self.nombre}, ID: {self.id_}, Mana: {self._mana}, Puntos de Habilidad: {self.puntos_habilidad}, Experiencia: {self.experiencia}, Dinero: {self.dinero}"
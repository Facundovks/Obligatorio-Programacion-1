from aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, id_, puntos_habilidad, experiencia, dinero, mana):
        super().__init__(nombre, id_, puntos_habilidad, experiencia, dinero)
        self._mana = mana

    def get_mana(self):
        return self._mana
    
    def set_mana(self, mana):
        self._mana = mana

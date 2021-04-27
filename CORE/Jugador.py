import Mano
class Jugador:
    def __init__(self,nombre,puntos):
        self.mano = Mano()
        self.mesa = Mesa()
        self.nombre = nombre
        self.puntos = puntos

    def getNombre(self):
        return self.nombre
    
    def getPuntos(self):
        return self.puntos

    def getMano(self):
        return self.mano

    def getMesa(self):
        return self.mesa
    
    def modPuntos(self,cantidad):
        puntos = puntos + cantidad
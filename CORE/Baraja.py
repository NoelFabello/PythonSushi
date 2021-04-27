from Carta import Carta
import ramdon


class Baraja:

    def __init__(self):
        self.baraja = []
        inicializarCartas(self)
        ramdon.shuffle(baraja)

    def inicializarCartas(self):
        for i in range(5):
            self.baraja.append(Carta(1))
        
        for i in range(10):
            self.baraja.append(Carta(2))
        
        for i in range(5):
            self.baraja.append(Carta(3))
        
        for i in range(6):
            self.baraja.append(Carta(4))
        
        for i in range(6):
            self.baraja.append(Carta(5))
        
        for i in range(12):
            self.baraja.append(Carta(6))
        
        for i in range(8):
            self.baraja.append(Carta(7))
        
        for i in range(14):
            self.baraja.append(Carta(8))
        
        for i in range(14):
            self.baraja.append(Carta(9))
        
        for i in range(14):
            self.baraja.append(Carta(10))

    def verBaraja(self):
        for i in baraja:
            print(i.verCarta())
            
baraja = Baraja()
baraja.verBaraja()
        
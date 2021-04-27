class Carta:
    TIPOS = ["NIGIRI_C","NIGUIRI_S","NIGUIRI_T","WASABI","MAKI_1","MAKI_2","MAKI_3","TEMPURA","SASHIMI","GYOZA"]

    def __init__(self,tipoCarta):
        self.tipoCarta = tipoCarta

    def getTipo(self):
        return Carta.TIPOS[self.tipoCarta-1]

carta = Carta(1)
print(carta.getTipo())
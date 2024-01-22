from Roupa import Roupa

class Blusas(Roupa):
    def __init__(self, estampa, gola, id, nome, preco, marca, tamanho, cor):
        self.categoria = "Blusas"
        super().__init__(id, nome, preco, marca, tamanho, cor, self.categoria)

        self.__estampa = estampa
        self.__gola = gola

    def imprime_roupa(self):
        super().imprime_roupa()
        print(f"Estampa: {self.get_estampa()}")
        print(f"Gola: {self.get_gola()}")
    
    def get_gola(self):
        return self.__gola
    def get_estampa(self):
        return self.__estampa
    
    def set_estampa(self, estampa):
        self.__estampa = estampa
    def set_gola(self, gola):
        self.__gola = gola
    
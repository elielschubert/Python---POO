from Roupa import Roupa

class Calcas(Roupa):
    def __init__(self, largura, comprimento,id, nome, preco, marca, tamanho, cor):
        self.categoria = "Calças"
        super().__init__(id, nome, preco, marca, tamanho, cor, self.categoria)

        self.__largura = largura
        self.__comprimento = comprimento

    def imprime_roupa(self):
        super().imprime_roupa()
        print(f"Largura: {self.get_largura()}")
        print(f"Comprimento: {self.get_comprimento()}")


    def get_largura(self):
        return self.__largura
    
    def get_comprimento(self):
        return self.__comprimento

    def set_largura(self, largura):
        self.__largura = largura
    
    def set_comprimento(self, comprimento):
        self.__comprimento = comprimento

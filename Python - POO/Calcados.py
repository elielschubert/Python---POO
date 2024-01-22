from Roupa import Roupa

class Calcados(Roupa):
    def __init__(self, estilo, material, id, nome, preco, marca, tamanho, cor):
        self.categoria = "Calçados"
        super().__init__(id, nome, preco, marca, tamanho, cor, self.categoria)

        self.__estilo = estilo
        self.__material = material

    def imprime_roupa(self):
        super().imprime_roupa()
        print(f"Material: {self.get_material()}")
        print(f"Estilo: {self.get_estilo()}")

    def get_estilo(self):
        return self.__estilo

    def get_material(self):
        return self.__material

    def set_estilo(self, estilo):
        self.__estilo = estilo

    def set_material(self, material):
        self.__material = material
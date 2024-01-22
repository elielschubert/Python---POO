class Roupa:
    def __init__(self, id, nome, preco, marca, tamanho, cor, categoria):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__marca = marca
        self.__tamanho = tamanho
        self.__cor = cor
        self.__categoria = categoria

    def imprime_roupa(self):
        print(f"ID: {self.get_id()}")
        print(f"Nome: {self.get_nome()}")
        print(f"Preço: R${self.get_preco()}")
        print(f"Marca: {self.get_marca()}")
        print(f"Cor: {self.get_cor()}")
        print(f"Categoria: {self.get_categoria()}")

    @staticmethod
    def cadastrar_roupa():
        nome = input("Informe o nome da peça: ")
        preco = input("Informe o preço da peça: R$")
        marca = input("Informe a marca do produto: ")
        tamanho = input("Informe o tamanho da peça: ")
        cor = input("Informe a cor da peça: ")
        return [nome, preco, marca, tamanho, cor]

    def get_id(self):
        return self.__id    
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_marca(self):
        return self.__marca
    def get_tamanho(self):
        return self.__tamanho
    def get_cor(self):
        return self.__cor
    def get_categoria(self):
        return self.__categoria
    
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_preco(self, preco):
        self.__preco = preco
    def set_marca(self, marca):
        self.__marca = marca
    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho
    def set_categoria(self, categoria):
        self.__categoria = categoria
    def set_cor(self, cor):
        self.__cor = cor
        
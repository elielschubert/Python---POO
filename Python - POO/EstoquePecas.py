class EstoquePecas():
    def __init__(self):
        self.__quantidade = 0
        self.__quantidade_minima = None 
        self.__peca = None

    def get_quantidade(self): 
        return self.__quantidade
    
    def set_quantidade(self, quantidade, remover):
        if remover:
            self.__quantidade -= quantidade
        else:
            self.__quantidade += quantidade
        

    def get_quantidade_minima(self):
        return self.__quantidade_minima
    
    def set_quantidade_minima(self, quantidade_minima):
        self.__quantidade_minima = quantidade_minima
    
    def get_peca(self):
        return self.__peca
    
    def set_peca(self, peca):
        self.__peca = peca
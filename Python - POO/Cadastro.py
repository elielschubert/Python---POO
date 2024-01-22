from Roupa import Roupa
from EstoquePecas import EstoquePecas
from Validacao import validar_categoria, verificar_inteiro, verificar_quantidade
from Calcas import Calcas
from Blusas import Blusas
from Calcados import Calcados
import os

class Cadastro:
    def __init__(self):
        self.__lista_pecas = []
        self.__estoque = []
        self.__contador_pecas = 0
        
    def cadastrar_peca(self):
        os.system("cls")
        print("=== Cadastrar Peça de Roupa === ")
        self.__contador_pecas += 1

        id = self.__contador_pecas
        categoria = self.selecionar_categoria()
        valores = Roupa.cadastrar_roupa()

        if categoria == 1:
            self.cadastrar_blusas(id, *valores)
        elif categoria == 2:
            self.cadastrar_calcas(id, *valores)
        else:
            self.cadastrar_calcados(id, *valores)

    def selecionar_categoria(self):
        categorias = ["Blusas", "Calças", "Calçados"]
        print()
        for categoria in categorias:
            print(f"[{categorias.index(categoria)+1}] - {categoria}")
        print()

        categoria_escolhida = validar_categoria()

        return categoria_escolhida

    def cadastrar_blusas(self, *valores):
        estampa = input("Informe a estampa: ")
        gola = input("Informe o recorte da gola: ")

        blusas = Blusas(estampa, gola, *valores)
        self.__lista_pecas.append(blusas)

    def cadastrar_calcados(self, *valores):
        estilo = input("Informe o estilo do calçado: ")
        material = input("Informe o material do calçado: ")
        
        calcado = Calcados(estilo, material,*valores)
        self.__lista_pecas.append(calcado)

    def cadastrar_calcas(self, *valores):
        largura = input("Informe a largura da cintura: ")
        comprimento = input("Informe o comprimento da calça: ")
    
        calca = Calcas(largura, comprimento, *valores)
        self.__lista_pecas.append(calca) 

    def acessar_estoque(self):
        os.system("cls")
        print("=== Inserir Peça de Roupa no Estoque === ")

        if len(self.__lista_pecas) > 0:
            peca_escolhida = self.pesquisar_peca()

            peca_estoque = EstoquePecas()
            if len(self.__estoque) > 0:
                jaExiste = False
                for peca in self.__estoque:
                    if peca.get_peca() == peca_escolhida:
                        jaExiste = True   
                        break
                self.pedir_valores_estoque(peca_estoque, peca_escolhida, jaExiste)
            else:
                self.pedir_valores_estoque(peca_estoque, peca_escolhida, False)
        else:
            print("Não há peças de roupa cadastradas!")
        

    def pedir_valores_estoque(self, objeto, peca, jaExiste):
        if not jaExiste:
            objeto.set_peca(peca)
            quantidade_minima = verificar_inteiro("Digite a quantidade mínima a ser inserida no estoque: ")
            objeto.set_quantidade_minima(quantidade_minima)
            objeto.set_quantidade(verificar_quantidade(verificar_inteiro("Digite a quantidade que deseja enviar ao estoque: "), quantidade_minima), False)

            self.__estoque.append(objeto)
        else:
            for peca_estoque in self.__estoque:
                if peca_estoque.get_peca() == peca:
                    peca_estoque.set_quantidade(int(input("Digite a quantidade: ")), False)
                    break


    def exibir_pecas(self):
        os.system("cls") 
        print("=== Lista de Peças de Roupa === ")
        if len(self.__lista_pecas) > 0:
            for peca in self.__lista_pecas:
                peca.imprime_roupa()
                
                for quantidade in self.__estoque:
                    if peca.get_id() == quantidade.get_peca().get_id():
                        print(f"Quantidade em estoque: {quantidade.get_quantidade()}")
                        print(f"Quantidade mínima: {quantidade.get_quantidade_minima()}")
                        
                        if quantidade.get_quantidade() < quantidade.get_quantidade_minima():
                            print("ESTA PEÇA DE ROUPA PRECISA SER ADQUIRIDA!")
                        break
                
                print("\n")
                input("Pressione a tecla ENTER ")
        else:
            print("Não há peças de roupa cadastradas!") 
    
    def pesquisar_peca(self):
        while True:
            for peca in self.__lista_pecas:
                print(f"Id: {peca.get_id()} \nNome: {peca.get_nome()} \n") 
            
        
            escolha_usuario = verificar_inteiro("Digite o ID: ")

            peca_escolhida = None
            for peca in self.__lista_pecas:
                if peca.get_id() == escolha_usuario:
                    peca_escolhida = peca
                    return peca_escolhida
            print("ID inválido, tente novamente!")       
        

    def remove_estoque(self):
        os.system("cls")
        print("=== Remover peça de roupa do estoque ===")
        if len(self.__lista_pecas) > 0 and len(self.__estoque) > 0:
            peca_removida= self.pesquisar_peca()

            quantidade_removida = verificar_inteiro("Informe a quantidade: ")
            for peca_estoque in self.__estoque: 
                if peca_estoque.get_peca() == peca_removida:
                    if peca_estoque.get_quantidade() == 0 or (peca_estoque.get_quantidade() - quantidade_removida<= 0):
                        self.__estoque.remove(peca_estoque)
                        break

                    peca_estoque.set_quantidade(quantidade_removida, True)
        else:
            print("Não há peças de roupa cadastradas!")


    def deletar_peca(self):
        os.system("cls")
        print("=== Deletar Peça de Roupa ===") 
        if len(self.__lista_pecas) > 0:
            peca_escolhida = self.pesquisar_peca()
            
            if not list(filter(lambda peca_estoque : peca_estoque.get_peca() == peca_escolhida, self.__estoque)):
                self.__lista_pecas.remove(peca_escolhida)
            else:
                print ("Peça não pôde ser removida! Ainda constam itens no estoque!")
                input("Pressione a tecla ENTER... ")
            return

        else:
            print("Não há peças de roupa cadastradas")

    def editar_peca(self):
        os.system("cls")
        peca_escolhida = self.pesquisar_peca()
        
        self.exibir_pecas()

        opcao = True
        while opcao:
            selecionar_edicao = input("\nInforme a característica que você deseja alterar (ex: Cor): \n").upper().replace('Ç', 'C')
            opcao = False
            if selecionar_edicao == "NOME":
                peca_escolhida.set_nome(input("Informe o novo nome: "))

            elif selecionar_edicao == "PRECO":
                peca_escolhida.set_preco(input("Informe o novo preço: "))

            elif selecionar_edicao == "MARCA":
                peca_escolhida.set_marca(input("Informe a nova marca: "))

            elif selecionar_edicao == "COR":
                peca_escolhida.set_cor(input("Informe a nova cor: "))

            #Brusa

            elif peca_escolhida.get_categoria() == "Blusas" and selecionar_edicao == "ESTAMPA":
                peca_escolhida.set_estampa(input("Informe a estampa: "))

            elif peca_escolhida.get_categoria() == "Blusas" and selecionar_edicao == "GOLA":
                peca_escolhida.set_gola(input("Informe a nova gola "))

            elif peca_escolhida.get_categoria() == "Blusas" and selecionar_edicao == "TAMANHO":
                peca_escolhida.set_tamanho(input("Informe o novo tamanho: "))

            #Calça

            elif peca_escolhida.get_categoria() == "Calças" and selecionar_edicao == "LARGURA":
                peca_escolhida.set_largura(input("Informe a nova largura: "))

            elif peca_escolhida.get_categoria() == "Calças" and selecionar_edicao == "COMPRIMENTO":
                peca_escolhida.set_comprimento(input("Informe a nova comprimento: "))

            #Calça-do

            elif peca_escolhida.get_categoria() == "Calçados" and selecionar_edicao == "ESTILO":
                peca_escolhida.set_estilo(input("Informe o estilo: "))

            elif peca_escolhida.get_categoria() == "Calçados" and selecionar_edicao == "MATERIAL":
                peca_escolhida.set_material(input("Informe o material: "))

            else:
                print("Digite uma opção válida.")
                opcao = True

# Agradecimentos a Leonardo Rócio

def verificar_inteiro(texto):
    valor = 0
    while True:
        try:
            valor = int(input(texto))
        except Exception:
            print("Digite um valor inteiro")
        else:
            if valor >= 0:
                return valor

def verificar_quantidade(valor1, valor2):
    while True:
        try:
            if valor1 >= valor2:
                return valor1
            print("Digite uma quantidade maior do que a quantidade mínima!\n")

            valor1 = int(input("Digite novamente: "))

        except Exception:
            print("Digite um valor válido!!")

def validar_categoria():
    while True:
        try:
            id_categoria = int(input("Digite o id da categoria desejada: "))

            if 3 >= id_categoria >= 1:
                return id_categoria
            print("Digite uma opção válida!")

        except Exception:
            print("Digite um valor válido.") 


        
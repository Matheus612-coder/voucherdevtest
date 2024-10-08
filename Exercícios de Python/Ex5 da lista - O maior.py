# Elaborar uma função para retornar o maior de três números recebidos por parâmetro.

def maior(num, num2, num3):
    lista = [num,num2,num3]
    print("O maior número digitado foi" , max(lista))

num = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

maior(num,num2,num3)




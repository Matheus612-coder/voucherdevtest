# Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de 
# retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0

def data(num):
    
    if num > 0:
        print("1")
    
    elif num < 0:
        print("-1")
    
    else:
        num = 0
        print("igual a zero")

data(int(input("Digite um número: ")))


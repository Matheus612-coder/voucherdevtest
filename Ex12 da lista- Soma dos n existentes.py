# Elabore uma função que receba dois números inteiros positivos por parâmetros e retorne a
# soma dos N números inteiros existentes entre eles.

def numeros(a,b):
    soma = 0 

    for numero in range(a, b+1):
        soma = soma+numero

    print(soma)

while True:
    
    a = int(input("Digite o valor a do intervalo: "))

    if a < 0:
        print("Digite um 'a' maior do que zero!")
        break
    
    elif a>0 or a==0:

        b= int(input("digite o valor b do intervalo: "))

        if b<0:
            print("Digite um 'b' maior do que zero!")
            break
           

        else: 
            numeros(a,b)
            break






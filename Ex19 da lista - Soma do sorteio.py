# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda 
# função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

numeros = []
soma=0

import random

def sorteia():

    for numero in range(0, 101):

        i= random.choice(numero)
        numeros.append(i)

    #i = random.choice(numeros)


def somaPar():
    for item in numeros:

        if item %2==0:
            soma= soma+item
    
    print(soma)

while len(numeros) <5:
    try:
        sorteia()
        somaPar()
    
    except:
        print("Digite apenas números!")









# Escreva um programa que recebe uma tupla de números inteiros e imprima a soma de todos os 
# números pares da tupla

tupla = (1,2,3,4,5,6,7,8,8,9,0,11)

soma=0

for num in tupla:

    if num%2==0:
        soma = num+soma

print(soma)





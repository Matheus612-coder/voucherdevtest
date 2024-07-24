# Dada uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do 
# maior valor. (SEM USAR FUNÇÃO)
# matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]

matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]
maior = matriz[0][0]
contador=0

for i in matriz:
    print(i)

for linha in matriz:
    for coluna in linha:
        if maior> coluna:
            continue
        else:
            maior = coluna
            contador = coluna


print(maior,contador)














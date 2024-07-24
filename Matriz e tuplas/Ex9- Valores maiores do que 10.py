# Leia a matriz 4 x 4 abaixo. Conte e escreva quantos valores maiores que 10 ela possui. 
# R=9 valores maiores que 10.
# matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]
          
matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]

total=0

for linha in matriz:
    for coluna in linha:
        if coluna >10:
            total+=1

print("existem",total, "números maiores do que 10.")




# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais 
# elementos. Escreva ao final a matriz obtida. Saída:
# [1, 0, 0, 0, 0]
# [0, 1, 0, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 0, 1, 0]
# [0, 0, 0, 0, 1]

matriz=[]

for linha in range(5):
    lin=[]
    for coluna in range(5):
        if linha==coluna:
            lin.append(1)
        else:
            lin.append(0)

    matriz.append(lin)

for i in matriz:
    print(i)













# Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na 
# diagonal principal. (SEM USAR FUNÇÃO)
# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]

M = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

print("A SOMA DA DIAGONAL PRINCIPAL É:" , M[0][0]+M[1][1]+M[2][2])

soma = 0 

for linha in range(3):
    for coluna in range(3):
        if linha ==coluna:
            soma = soma+M[linha][coluna]

print("\n A SOMA DA DIAGONAL PRINCIPAL É:",soma)





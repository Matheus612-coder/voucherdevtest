# Considere uma lista de tuplas em que cada tupla representa informações sobre um 
# aluno, contendo o nome e a nota de uma disciplina. Escreva um programa que recebe 
# essa lista e imprima o nome do aluno que obteve a maior nota.
# alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]

alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]
maior =0
strings = []
notas =[]


for estudante in alunos:
   notas.append(estudante[1])
   strings.append(estudante[0])
   






print(alunos[notas.index(max(notas))])




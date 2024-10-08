# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra 
# for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a 
# média ponderada, com pesos 5, 3 e 2.

def notas(nota,nota2,nota3,letra):
    if letra == "a".lower():
        media_Aritimetica=(nota+nota2+nota3)/3
        print(media_Aritimetica)

    elif letra == "p".lower():
        mediaPonderada = (nota*5 + nota2*3 + nota3*2)/10
        print(mediaPonderada)

nota = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
nota3 = float(input("Digite uma nota: "))
letra = input("Digite a letra para tua avaliação: a para " 
              "média aritimética e p para média ponderada: ")

notas(nota,nota2,nota3,letra)

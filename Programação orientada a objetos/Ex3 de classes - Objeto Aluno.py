# Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os seguintes atributos:
# Nome;
# RA;
# Nota 1, nota 2, nota 3, nota 4;
# A classe deve ter o seguintes método:
# Mostrar_situacao: (APROVADO / EXAME / REPROVADO). 
# Considere que, nesse caso, a média final é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado somente se obtiver média maior ou igual a sete.
# Exame entre 5 e 6.9. Reprovado abaixo de 5
# A situação será retornada a partir das notas obtidas pelo aluno.

class Aluno:
    def __init__(self,nome,RA,nota1,nota2,nota3,nota4):
        self.nome= nome
        self.RA= RA
        self.nota1= nota1
        self.nota2= nota2
        self.nota3= nota3
        self.nota4= nota4

    def Mostrar_situacao(self):
        resultado = (self.nota1 +self.nota2+self.nota3+self.nota4)/4
        return resultado

aluno = Aluno("Mestre", "2024.1.144", 2,3,4,5)

if aluno.Mostrar_situacao()>=7:
    print("aprovado")

elif aluno.Mostrar_situacao()<=5 or aluno.Mostrar_situacao() <=6.9:
    print("exame")

else:
    print("reprovado")

print(aluno.Mostrar_situacao())




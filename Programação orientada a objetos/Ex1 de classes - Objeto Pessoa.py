# 1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:
# Nome
# Idade
# Endereço
# A classe deve ter os seguintes métodos:
# Mostrar nome;
# Alterar a idade;
# Imprimir endereço.


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def MostrarNome(self):
        return self.nome
    
    def setAlterarIdade(self, NovaIdade):
        IdadeAntiga = self.idade
        self.idade = NovaIdade
        return IdadeAntiga, NovaIdade

    def MostrarEndereco(self):
        return self.endereco
    
pessoa = Pessoa("mat", 23, "rua das árvores")

print("Nome:", pessoa.MostrarNome())

idade_antiga, idade_nova = pessoa.setAlterarIdade(20)

print("Nova idade:", idade_nova)
print("Idade Antiga", idade_antiga)

print("Endereço:", pessoa.MostrarEndereco())









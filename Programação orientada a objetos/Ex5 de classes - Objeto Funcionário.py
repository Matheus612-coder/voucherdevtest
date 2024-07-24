# - Classe Funcionário: Uma empresa quer criar um controle de pagamento para os funcionários. Crie uma classe que modele um Funcionário com os seguintes atributos e métodos:
# Nome; Sobrenome; Horas_trabalhadas; Valor_hora;
# A classe deve ter o seguintes métodos:
# O método nomeCompleto deve escrever na tela o atributo nome concatenado ao atributo sobrenome.
# O método calcularSalario faz o cálculo de quanto o funcionário irá receber no mês, multiplicando o atributo horasTrabalhadas pelo atributo valorPorHora. Em seguida, escreve o valor na tela.
# O método incrementarHoras adiciona um valor passado por parâmetro ao valor já existente no atributo valorPorHora.

class Funcionario:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome= nome
        self.sobrenome= sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora =valor_hora
    
    def nomeCompleto(self):
        return self.nome + self.sobrenome

    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_hora
    
    def incrementaHoras(self, hora):
        hora = self.valor_hora
        return hora

funcionario = Funcionario("mat", "antônio", 5,40)

print(funcionario.nomeCompleto())
print(funcionario.calcularSalario())
print(funcionario.incrementaHoras(40))










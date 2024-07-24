# Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.
# Nome;
# CPF;
# Numero;
# Saldo;
# A classe deve ter o seguintes métodos:
# Depositar()
# Sacar()  -  OBS: somente enquanto a conta possuir saldo positivo
# Imprimir saldo()

class Conta:
    def __init__(self,nome,cpf,numero,saldo):
       self.nome = nome
       self.cpf= cpf
       self.numero= numero
       self.saldo= saldo
    
    def depositar(self):
        return self.saldo

    def sacar(self):  
        return self.saldo

    def ImprimirSaldo(self):
        return self.saldo

conta = Conta("mat","012","34",1000)

while conta.saldo > 0:
    quantidade = int(input("Digite quanto quer sacar: "))

    if quantidade > conta.saldo:
        print("Saldo insuficiente")
    else:
        conta.saldo -= quantidade
        print(f"Novo saldo: {conta.saldo}")


# while conta.sacar>0:
#     quantidade = int(input("Digite quanto quer sacar: "))

#     if quantidade>conta.sacar():
#         print("saldo insuficiente")

#     else:
#         NovoSaldo = quantidade - conta.sacar()
#         print(NovoSaldo)    








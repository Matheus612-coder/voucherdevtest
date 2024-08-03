class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome=nome
        self.matricula=matricula
        self.salario=salario

    def bater_ponto(self, ponto=True):
        if ponto==True:
            return "Funcionário bateu ponto."
        
        else:
            return "Funcionário não bateu ponto."

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao=comissao

    def bater_meta(self, meta):
       if meta ==True:
         return"Vendedor atingiu a meta."
       
       else:
           return "Meta não atingida."

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, meta):
        super().__init__(nome, matricula, salario)
        self.meta=meta

    def meta(self):
        if self.meta==False:
            return "Você está demitido"

        else:
            return "Continue com o bom trabalho!"

funcionario = Funcionario("marcos", 20210304, 2000)
vendedor=Vendedor("carlos", 20210305,1500, 5)
gerente=Gerente("Mat",2021345, 4000, 5)

print(funcionario.bater_ponto(False))
print(vendedor.bater_meta(False))


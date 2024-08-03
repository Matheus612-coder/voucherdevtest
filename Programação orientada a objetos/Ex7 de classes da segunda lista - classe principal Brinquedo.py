# Classe Brinquedos: Andy Davis precisa classificar seus 
# brinquedos por Subclasses, sabemos que cada brinquedo tem 
# atributos e métodos diferentes, exemplo Buzz Lightyear voa e 
# Woody laça. Defina principais atributos:

class Brinquedos:
    def __init__(self, nome,cor,tamanho,preco):
        self.nome=nome
        self.cor= cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        return "Estou brincando com", self.nome

class Buzz(Brinquedos):
    def __init__(self, nome="Buzz", cor="Verde, branco e lilás", tamanho="20cm", preco=1500,asas=None):
        super().__init__(nome,cor, tamanho, preco)
        self.asas=asas

    def voar(self):
        return "Ao infinito e além!"
    
    def brincar(self):
        return f"{super().brincar()} \nSou astronauta. Brinco no espaço."
        

class Woody(Brinquedos):
    def __init__(self, nome="Woody", cor=None, tamanho="20cm", preco=1000,laco=None):
        super().__init__(nome, cor, tamanho, preco)
        self.laco=laco

    def acao_laco(self):
        return "Mãos ao alto! Serás laçado!"

    def brincar(self):
        return f"{super().brincar()} \nSou cowboy, mestre dos laços."
    
class Dinossauro(Brinquedos):
    def __init__(self, nome="Dino", cor="Verde", tamanho="30cm", preco=800,bracoscurtos=None):
        super().__init__(nome, cor, tamanho, preco)
        self.bracoscurtos=bracoscurtos

    def pegar(self):
        return "Com meus braços curtos nada alcanço."
    
    def brincar(self):
        return f"{super().brincar()} \nSou dino. Não me divirto."
    
class Cabecadebatata(Brinquedos):
    def __init__(self, nome="Sr.Batata", cor="Amarelo", tamanho="10cm", preco=100,customizavel=None):
        super().__init__(nome, cor, tamanho, preco)
        self.customizavel=customizavel

    def personalizar(self):
        return "Só eu sou mestre dos disfarces."

    def brincar(self):
        return f"{super().brincar()} \nSou Personalizável. Brinco de disfarces."

class Lamparina(Brinquedos):
    def __init__(self, nome="Lamparina", cor=None, tamanho= "20cm", preco=200, luz=None):
        super().__init__(nome, cor, tamanho, preco)
        self.luz=luz

    def iluminar(self):
        return "Eu dou luz."
    
    def brincar(self):
        return f"{super().brincar()} \nSou lamparina. Não Brinco nem durmo."
    
class Carrinho(Brinquedos):
    def __init__(self, nome="Carrinho", cor=None, tamanho="10x5", preco=300, controleremoto=None):
        super().__init__(nome, cor, tamanho, preco)
        self.controleremoto=controleremoto

    def mover(self):
        return "Sou rápido como um carro de verdade."

    def brincar(self):
        return f"{super().brincar()} \nSou carrinho. Não gosto de brincar."

class Playstation2(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, cd):
        super().__init__(nome, cor, tamanho, preco)
        self.cd = cd

    def ler(self):
        return "Leio jogos e até filmes."

class Ursodepelucia(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, macio):
        super().__init__(nome, cor, tamanho, preco)
        self.macio=macio

    def disfarce(self):
        return "Vejam todos quem era o vilão desde sempre!"

class Zurg(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, canhao):
        super().__init__(nome, cor, tamanho, preco)
        self.canhao=canhao

    def pai(self):
        return "Eu sou teu pai, Buzz."

class Garfo(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,trespontas):
        super().__init__(nome, cor, tamanho, preco)
        self.trespontas=trespontas

    def comer(self):
        return "Sou garfo, mas não talher."

buzz = Buzz()
print(buzz.brincar())
print(buzz.voar())
print()

woody = Woody()
print(woody.brincar())
print(woody.acao_laco())
print()

dinossauro=Dinossauro()
print(dinossauro.brincar())
print(dinossauro.pegar())
print()

cabeca=Cabecadebatata()
print(cabeca.brincar())
print(cabeca.personalizar())
print()

lamparina= Lamparina()
print(lamparina.brincar())
print(lamparina.iluminar())
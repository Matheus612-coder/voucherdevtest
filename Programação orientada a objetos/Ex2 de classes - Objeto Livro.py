# Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:
# Nome
# Autor
# Editora
# Páginas
# A classe deve ter o seguintes métodos:
# Alterar_editora()
# Listar_qtde_paginas()

class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas= paginas

    def setAlterarEditora(self, NovaEditora):
        self.editora = NovaEditora
        return NovaEditora

    def ListarQuantidadeDePaginas(self):
        return self.paginas

livro = Livro("Mil sonhos", "Jorge", "Panini", 500)

print(livro.setAlterarEditora("Comic cons"))

print(livro.ListarQuantidadeDePaginas())



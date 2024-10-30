create database Biblioteca;
use Biblioteca;

create table Livro(

	id_livro int primary key,
    titulo char(255) not null,
	isbn char not null,
	categoria char(100) not null
 );

create table Autor(

	id_autor int primary key,
	nome char(100) not null,
	data_de_nascimento date
);

create table Livro_autor(

	id_livro_autor int primary key,
	id_livro int,
	id_autor int,
	foreign key (id_livro) references Livro(id_livro),
	foreign key (id_autor) references Autor(id_autor)
);

create table Emprestimo(

	id_emprestimo int primary key,
	data_emprestimo date not null,
	data_devolucao date not null,
	id_livro int,
	foreign key (id_livro) references Livro(id_livro)
);

show tables;
describe Livro_autor;





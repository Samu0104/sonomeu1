create schema fernanda;

use fernanda; 

create table conta(
id integer primary key not null,
senha integer unique key not null,
nome_sobrenome varchar(80) unique key not null,
data_nasc date not null,
email varchar(60)
);

create table setor(
codigo integer not null,
descricao varchar(40)
);

create table produto(
id integer primary key not null,
nome varchar(40) not null,
un_medida varchar(20) not null,
preco float not null,
tipo varchar(40) null    ,
cd_setor integer not null,
ativo boolean not null,
foreign key(cd_setor) references setor(codigo)
);

create table compra(
id_conta integer not null,
idProduto integer not null,
qtd  integer not null,
foreign key (id_conta) references Conta(id),
foreign key (idProduto) references Produto(id)
);

insert into Produto values
(1,'Coala Boia Lilas','tamanho único',39.90,'short e blusa','infantil Feminino', true),
(2,'Inverno Coala','tamanho único',59.90,'calça e blusa','infantil Feminino', true),
(3,'Soft Fleece Coala Gelly','tamanho único', 39.90, 'calça e blusa', 'infantil Feminino', false),
(4,'manga longa','tamanho único',29.90,'calça e blusa','infantil Feminino', true),
(5,'Unicórnio ','tamanho único',79.90,'macacão','infantil Feminino', true),
(6,'Dino com Cristas 3D ','tamanho único',89.90,'calça e blusa','infantil Masculino', true),
(7,'Select Verde ','tamanho único',49.90,'calção e blusa','infantil Masculino', true),
(8,'Coala Verde ','tamanho único',69.90,'calça e blusa','infantil Masculino', true),
(9,'Sonic ','tamanho único',89.90,'calça e blusa','infantil Masculino', false),
(10,'supermman ','tamanho único',39.90,'calção e blusa','infantil Masculino', true),
(11,'Americano','tamanho único',120.00,'short e blusa','Feminino', true),
(12,'Americano longo ','tamanho único',89.90,'calça e blusa','Feminino', true),
(13,'Americano cetin ','tamanho único',89.90,'short e blusa','Feminino', true),
(14,'renda ','tamanho único',39.90,'short e regata','Feminino', false),
(15,'camuflado ','tamanho único',69.90,'calça e blusa','Feminino', true),
(16,'cogumelo ','tamanho único',39.90,'short e regata','Feminino', true),
(17,'inverno ','tamanho único',69.90,'calça e blusa','Masculino', true),
(18,'bola de futbol ','tamanho único',29.90,'calção e blusa',' Masculino', false),
(19,'Americano ','tamanho único',89.90,'calção e blusa',' Masculino', true),
(20,'montros S.A ','tamanho único',89.90,'calção e blusa',' Masculino', true),
(21,'capitão america ','tamanho único',89.90,'calça e blusa',' Masculino', true),
(22,'Minnie Mouse ','PLus size',89.90,'calça e blusa','Feminino', true),
(23,'Mickey Mouse','PLus size',129.90,'short e blusa',' Feminino', true),
(24,'Americano ','PLus size',59.90,'calção e blusa',' Masculino', true),
(25,'Jonas','PLus size',89.90,'calça e blusa',' Masculino', false),
(26,'azul listrado ','PLus size',49.90,'calção e blusa',' Masculino', true)
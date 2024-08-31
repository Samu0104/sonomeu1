import sqlite3

#Conectar ao banco de dados SQLite (ou criar um novo se não existir)
conn = sqlite3.connect('evelyn_tb.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Conta (
    id INTEGER PRIMARY KEY NOT NULL,
    senha INTEGER UNIQUE NOT NULL,
    nome_sobrenome VARCHAR(80) UNIQUE NOT NULL,
    data_nasc DATE NOT NULL,
    email VARCHAR(60)
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS setor (
    codigo integer not null,
    descricao varchar(40)   
)

''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(40) NOT NULL,
    un_medida VARCHAR(20) NOT NULL,
    preco FLOAT NOT NULL,
    tipo VARCHAR(40),
    setor VARCHAR(40) NOT NULL,
    ativo BOOLEAN NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS compra (
    id_conta INTEGER NOT NULL,
    idProduto INTEGER NOT NULL,
    precoProduto FLOAT NOT NULL,
    setorProduto VARCHAR(40) NOT NULL,
    FOREIGN KEY (id_conta) REFERENCES Conta(id),
    FOREIGN KEY (idProduto) REFERENCES Produto(id)
)
''')

# Inserir dados na tabela Produto
cursor.executemany('''
INSERT INTO Produto (id, nome, un_medida, preco, tipo, setor, ativo) VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    (1, 'Coala Boia Lilas', 'tamanho único', 39.90, 'short e blusa', 'infantil Feminino', True),
    (2, 'Inverno Coala', 'tamanho único', 59.90, 'calça e blusa', 'infantil Feminino', True),
    (3, 'Soft Fleece Coala Gelly', 'tamanho único', 39.90, 'calça e blusa', 'infantil Feminino', False),
    (4, 'manga longa', 'tamanho único', 29.90, 'calça e blusa', 'infantil Feminino', True),
    (5, 'Unicórnio', 'tamanho único', 79.90, 'macacão', 'infantil Feminino', True),
    (6, 'Dino com Cristas 3D', 'tamanho único', 89.90, 'calça e blusa', 'infantil Masculino', True),
    (7, 'Select Verde', 'tamanho único', 49.90, 'calção e blusa', 'infantil Masculino', True),
    (8, 'Coala Verde', 'tamanho único', 69.90, 'calça e blusa', 'infantil Masculino', True),
    (9, 'Sonic', 'tamanho único', 89.90, 'calça e blusa', 'infantil Masculino', False),
    (10, 'supermman', 'tamanho único', 39.90, 'calção e blusa', 'infantil Masculino', True),
    (11, 'Americano', 'tamanho único', 120.00, 'short e blusa', 'Feminino', True),
    (12, 'Americano longo', 'tamanho único', 89.90, 'calça e blusa', 'Feminino', True),
    (13, 'Americano cetin', 'tamanho único', 89.90, 'short e blusa', 'Feminino', True),
    (14, 'renda', 'tamanho único', 39.90, 'short e regata', 'Feminino', False),
    (15, 'camuflado', 'tamanho único', 69.90, 'calça e blusa', 'Feminino', True),
    (16, 'cogumelo', 'tamanho único', 39.90, 'short e regata', 'Feminino', True),
    (17, 'inverno', 'tamanho único', 69.90, 'calça e blusa', 'Masculino', True),
    (18, 'bola de futbol', 'tamanho único', 29.90, 'calção e blusa', 'Masculino', False),
    (19, 'Americano', 'tamanho único', 89.90, 'calção e blusa', 'Masculino', True),
    (20, 'montros S.A', 'tamanho único', 89.90, 'calção e blusa', 'Masculino', True),
    (21, 'capitão america', 'tamanho único', 89.90, 'calça e blusa', 'Masculino', True),
    (22, 'Minnie Mouse', 'PLus size', 89.90, 'calça e blusa', 'Feminino', True),
    (23, 'Mickey Mouse', 'PLus size', 129.90, 'short e blusa', 'Feminino', True),
    (24, 'Americano', 'PLus size', 59.90, 'calção e blusa', 'Masculino', True),
    (25, 'Jonas', 'PLus size', 89.90, 'calça e blusa', 'Masculino', False),
    (26, 'azul listrado', 'PLus size', 49.90, 'calção e blusa', 'Masculino', True)
])

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Tabelas criadas e dados inseridos com sucesso.")

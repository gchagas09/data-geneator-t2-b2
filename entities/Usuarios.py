class Telefone:
    def __init__(self, codigo_area, numero, descricao):
        self.codigo_area = codigo_area
        self.numero = numero
        self.descricao = descricao

class Usuario:
    def __init__(self, email, senha, nome, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

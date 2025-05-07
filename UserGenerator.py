from entities.usuario.Usuario import Usuario
from entities.usuario.Telefone import Telefone
import json
import random
from faker import Faker

faker = Faker('pt_BR')

senha = 123456
t1 = Telefone(51, 985726995, "Telefone principal")
u1 = Usuario("carol@email.com", senha, "Carolina Silva Oliveira", t1)

t2 = Telefone(51, 985057825, "Telefone principal")
u2 = Usuario("alice@email.com", senha, "Alice Bastos Neves", t2)

t3 = Telefone(51, 985052344, "Telefone Principal")
u3 = Usuario("daniel@email.com", senha, "Daniel Rodrigues Alves", t3)

t4 = Telefone(51, 999039844, "Telefone Principal")
u4 = Usuario("bob@email.com", senha, "Robert Downey Junior", t4)

usuarios = [u1, u2, u3, u4]

usuariosJson = []

def cadastra():
    for usuario in usuarios:
        telefone = {
            "codigo_area": usuario.telefone.codigo_area,
            "telefone": usuario.telefone.numero,
            "descricao": usuario.telefone.descricao
        }
        user = {
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": usuario.senha,
            "telefone": telefone
        }
        usuariosJson.append(user)

def geraJson(qtd_usuarios):
    for i in range (1, qtd_usuarios+1):
        nome = faker.name()
        email = faker.email()
        senha = f"9{random.randint(100000000, 999999999)}"
        codigo_area = random.randint(11, 79)
        celular = f"9{random.randint(100000000, 999999999)}"
        descricao = "Telefone principal"

        tel = Telefone(codigo_area, celular, descricao)
        usuario = Usuario(email, senha, nome, tel)
        
        telefone = {
            "codigo_area": usuario.telefone.codigo_area,
            "telefone": usuario.telefone.numero,
            "descricao": usuario.telefone.descricao
        }
        user = {
            "nome": usuario.nome,
            "email": usuario.email,
            "senha": usuario.senha,
            "telefone": telefone
        }

        usuarios.append(usuario)
        usuariosJson.append(user)


def generate_user(qtd_usuarios):

    cadastra()
    geraJson(qtd_usuarios)

    return [usuariosJson, usuarios]



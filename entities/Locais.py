class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

class Coordenadas:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Local:
    id_local =1
    def __init__(self, nome, endereco, coordenadas, capacidade):
        self.id_local = Local.id_local
        self.nome = nome
        self.endereco = endereco
        self.coordenadas = coordenadas
        self.capacidade = capacidade
        Local.id_local += 1
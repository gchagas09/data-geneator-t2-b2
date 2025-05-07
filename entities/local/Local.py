
class Local:
    id_local =1
    def __init__(self, nome, endereco, coordenadas, capacidade):
        self.id_local = Local.id_local
        self.nome = nome
        self.endereco = endereco
        self.coordenadas = coordenadas
        self.capacidade = capacidade
        Local.id_local += 1
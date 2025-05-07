class Zona: 
    id_zona = 1
    def __init__(self, nome, localizacao, capacidade, serie_ingresso):
        self.id_zona = Zona.id_zona
        self.nome = nome
        self.localizacao = localizacao
        self.capacidade = capacidade
        self.serie_ingresso = serie_ingresso
        Zona.id_zona +=1
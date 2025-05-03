class Eventos: 
    def __init__(self, id_evento, duracao, data_hora_inicio):
        self.id_evento = id_evento
        self.duracao = duracao
        self.data_hora_inicio = data_hora_inicio

class Integrante:
    def __init__(self, artista, ano_ingresso, ano_saida):
        self.id_artista = artista.id
        self.ano_ingresso = ano_ingresso
        self.ano_saida = ano_saida

class Artista:
    id_artista = 1
    def __init__(self, tipo, nome, data_nascimento, pais_nascimento, cidade_nascimento, eventos):
        self.id_artista = Artista.id_artista
        self.tipo = tipo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.pais_nascimento = pais_nascimento
        self.cidade_nascimento = cidade_nascimento
        self.eventos = eventos
        Artista.id_artista +=1
    
    def __init__(self, tipo, nome, ano_inicio, musicos, eventos):
        self.id_artista = Artista.id_artista
        self.tipo = tipo
        self.nome = nome
        self.ano_inicio = ano_inicio
        self.musicos = musicos
        self.eventos = eventos
        Artista.id_artista +=1


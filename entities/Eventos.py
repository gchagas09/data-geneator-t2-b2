class Ingresso:
    num_ingresso = 1
    def __init__(self, assento, data_aquisicao, usuario_email):
        self.num_ingresso = Ingresso.num_ingresso
        self.assento = assento
        self.data_aquisicao = data_aquisicao
        self.usuario_email = usuario_email
        Ingresso.num_ingresso +=1

class Serie_ingresso:
    def __init__(self, data_abertura, valor):
        self.data_abertura = data_abertura
        self.valor = valor


class Zona: 
    id_zona = 1
    def __init__(self, nome, localizacao, capacidade, serie_ingresso):
        self.id_zona = Zona.id_zona
        self.nome = nome
        self.localizacao = localizacao
        self.capacidade = capacidade
        self.serie_ingresso = serie_ingresso
        Zona.id_zona +=1

class Local:
    def __init__(self, id_local, zonas):
        self.id_local = id_local
        self.zonas = zonas
        

class Evento:
    id_evento =1
    def __init__(self, data_hora_inicio, data_hora_termino, locais):
        self.id_evento = Evento.id_evento
        self.data_hora_inicio = data_hora_inicio
        self.data_hora_termino = data_hora_termino
        self.locais = locais
        Evento.id_evento +=1


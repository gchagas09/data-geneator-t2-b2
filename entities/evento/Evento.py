class Evento:
    id_evento =1
    def __init__(self, data_hora_inicio, data_hora_termino, locais):
        self.id_evento = Evento.id_evento
        self.data_hora_inicio = data_hora_inicio
        self.data_hora_termino = data_hora_termino
        self.locais = locais
        Evento.id_evento +=1


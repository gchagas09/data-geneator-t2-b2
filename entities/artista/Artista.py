from .Integrante import Integrante
from .Evento import Evento
class Artista:
    id_artista = 1

    def __init__(self, nome):
        self.id_artista = Artista.id_artista
        self.nome = nome
        self.eventos = []
        Artista.id_artista += 1

    @classmethod
    def cria_musico(cls, nome, data_nascimento, pais_nascimento, cidade_nascimento):
        a = cls(nome)
        a.tipo = "Musico"
        a.data_nascimento = data_nascimento
        a.pais_nascimento = pais_nascimento
        a.cidade_nascimento = cidade_nascimento
        return a

    @classmethod
    def cria_banda(cls, nome, ano_inicio):
        b = cls(nome)
        b.tipo = "Banda"
        b.ano_inicio = ano_inicio
        b.musicos = []
        return b

    def cadastra_evento(self, evento):
        inicio = evento.data_hora_inicio
        final = evento.data_hora_final
        duracao = final - inicio
        duracao = duracao.total_seconds()/60
        e = Evento(evento.id_evento, duracao, inicio)
        self.eventos.append(e)

    def cadastra_integrante(self, artista, ano_ingresso, ano_saida):
        if(self.tipo == "Banda"):
            i = Integrante(artista, ano_ingresso, ano_saida)
            self.musicos.append(i)
        else:
            raise TypeError("PARA CADASTRAR INTEGRANTES, VOCÊ DEVE ADICIONA-LOS EM BANDAS")
        
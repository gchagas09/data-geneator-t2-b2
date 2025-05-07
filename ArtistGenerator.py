from entities.artista.Artista import Artista
from entities.artista.Evento import Evento
from entities.artista.Integrante import Integrante

artistas =[]
artistasJson = []

def cadastra():
    eua = "Estados Unidos"
    br = "Brasil"
    #Bruno Mars
    a1 = Artista.cria_musico("Bruno Mars", "08/10/1985", eua, "Honolu")
    artistas.append(a1)
    a16 = Artista.cria_musico("Vinicuis Félix Miranda - Bruno", "22/04/1969", br, "Goiânia")
    artistas.append(a16)
    a17 = Artista.cria_musico("José Roberto Ferreira - Marrone", "09/11/1965", br, "Buriti Alegre")
    artistas.append(a17)
    b1 = Artista.cria_banda("Bruno & Marrone","1988")
    b1.cadastra_integrante(a16, 1988, "Hoje")
    b1.cadastra_integrante(a17, 1988, "Hoje")
    artistas.append(b1)
    


def geraJson():
    for artista in artistas:
        if(artista.tipo == "Musico"):
            eventos = []
            agenda = artista.eventos
            for evento in agenda:
                e = {
                    "id_evento" : evento.id_evento,
                    "duracao" : evento.duracao,
                    "data_hora_inicio" : evento.data_hora_inicio
                }
                eventos.append(e)
            m = {
                "id_artista" : artista.id_artista,
                "nome" : artista.nome,
                "tipo" : artista.tipo,
                "data_nascimento" : artista.data_nascimento,
                "pais_nascimento" : artista.pais_nascimento,
                "cidade_nascimento" : artista.cidade_nascimento,
                "eventos" : eventos
                }
            artistasJson.append(m)
        elif(artista.tipo == "Banda"):
            integrantes = []
            eventos = []
            banda = artista.musicos
            agenda = artista.eventos
            
            for integrante in banda:
                i = {
                    "id_artista" : integrante.id_artista,
                    "nome" : integrante.nome,
                    "ano_ingresso" : integrante.ano_ingresso,
                    "ano_saida" : integrante.ano_saida
                }
                integrantes.append(i)            
            for evento in agenda:
                e = {
                    "id_evento" : evento.id_evento,
                    "duracao" : evento.duracao,
                    "data_hora_inicio" : evento.data_hora_inicio
                }
                eventos.append(e)
            b = {
              "id_artista" : artista.id_artista,
              "nome" : artista.nome,
              "tipo" : artista.tipo,
              "ano_inicio" : artista.ano_inicio,
              "integrantes" : integrantes,
              "eventos"  : eventos
            }
            artistasJson.append(b)

def generate_artists():
    cadastra()
    geraJson()
    
    return [artistasJson, artistas]
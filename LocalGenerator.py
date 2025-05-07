from entities.local.Local import Local
from entities.local.Endereco import Endereco
from entities.local.Coordenadas import Coordenadas

locais = []
locaisJson=[]

def cadastra():
    #Ginásio Gigantinho
    e1 = Endereco("Av. Padre Cacique", 891, "Ao lado do Estádio Beira-Rio", "Praia de Belas", "Porto Alegre", "RS", "90810-240")
    c1 = Coordenadas("-30.064450478625226", "-51.234092442328176")
    l1 = Local("Ginásio Giantinho", e1, c1, 5000)
    locais.append(l1)

    #Estádio Beira-Rio
    e2 = Endereco("Av. Padre Cacique", 891, "Estádio", "Praia de Belas", "Porto Alegre", "RS", "90810-240")
    c2 = Coordenadas("-30.065424321860835", "-51.235881442328186")
    l2 = Local("Estádio Beira-Rio", e2, c2, 60000)
    locais.append(l2)

    #Arena do Grêmio
    e3 = Endereco("Av. Padre Leopoldo Bretano", 110, "É o estádio", "Farrapos", "Porto Alegre", "RS", "90250-590")
    c3 = Coordenadas("-29.973845369267305", "-51.19490668465637")
    l3 = Local ("Arena do Grêmio", e3, c3, 50000)
    locais.append(l3)

    #Ópera de Arame
    e4 = Endereco("R. João Gava", 920, "Teatro", "Abranches", "Curitiba", "PR", "82130-010")
    c4 = Coordenadas("-25.384302878024723", "-49.2762625288359")
    l4 = Local ("Opera de Arame", e4, c4, 1500)
    locais.append(l4)

    #Maracanã
    e5 = Endereco("R. Professor Eurico Rabelo", 0, "Estádio", "Maracanã", "Rio de Janeiro", "RJ", "20271-150")
    c5 = Coordenadas("-22.912017705694513", "-43.23014974232818")
    l5 = Local ("Estádio Maracanã", e5, c5, 75000)
    locais.append(l5)

    #Alianz Parque
    e6 = Endereco("Av. Francisco Matarazzo", 1705, "Estádio/Arena Multiuso", "Água Branca", "São Paulo", "SP", "05001-200")
    c6 = Coordenadas("-23.527546923053052", "-46.67839109814864")
    l6 = Local("Allianz Parque", e6, c6, 40000)
    locais.append(l6)

    #Estadio Monumental
    e7 = Endereco("Av. Presidente Figueroa Alcorta", 7591, "Estádio", "Belgrano", "Buenos Aires", "Provincia de Buenos Aires", "C1424BCL")
    c7 = Coordenadas("-34.54529601697623", "-58.449737573015454")
    l7 = Local("Estadio Monumental de Buenos Aires", e7, c7, 80000)
    locais.append(l7)

    #Estadio Nacional
    e8 = Endereco("Av Grecia", 2001, "Estadio", "Ñuñoa", "Santiago", "Provincia de Santiago", "7780464")
    c8 = Coordenadas("-33.46446106941528", "-70.61076635952318")
    l8 = Local("Estadio Nacional de Chile", e8, c8, 45000)
    locais.append(l8)

    #Wembley Stadium
    e9 = Endereco("Wembley Stadium", 0, "Estadio", "Wembley Park/Tokyngton", "Wembley", "Greater London", "HA90WS")
    c9 = Coordenadas("51.55694572993845", "-0.2843919396012263")
    l9 = Local ("Wembley Satadium", e9, c9, 90000)
    locais.append(l9)

    #Royal Albert Hall
    e10 = Endereco("Kensington Gore", 0, "Teatro/Casa de Shows", "South Kensington", "Londres", "Greater London", "SW72AP")
    c10 = Coordenadas("51.500988944619564", "-0.1772587116459786")
    l10 = Local("Royal Albert Hall", e10, c10, 5000)
    locais.append(l10)

    #Estadio Olimpico de Barcelona
    e11 = Endereco("Passeig Olimpic", 15, "Estadio", "Sants-Montjuïc", "Barcelona", "Barcelona", "08038")
    c11 = Coordenadas("41.36547243361116", "2.1560300288354024")
    l11 = Local ("Estadio Olimpico de Barcelona", e11, c11, 55000)
    locais.append(l11)

    #Sydney Opera House
    e12 = Endereco("Bennelog Point", 0, "Teatro/Casa de Show", "Sydeny Central Business District", "Sydeny", "New South Wales", "2000")
    c12 = Coordenadas("-33.85654829589762", "151.2153288865077")
    l12 = Local("Sydney Opera House", e12, c12, 5000)
    locais.append(l12)

    #Tokyo Dome
    e13 = Endereco("Koraku", 1361, "Estadio", "Koraku", "Toquio", "Toquio", "112-0004")
    c13 = Coordenadas("35.70581819773872", "139.7519449441795")
    l13 = Local("Tokyo Dome", e13, c13, 55000)
    locais.append(l13)

    #Madison Square Garden
    e14 = Endereco("Pennsylvania Plaza", 4, "Arena Multiuso", "Chelsea", "Nova York", "Nova York", "10001")
    c14 = Coordenadas("40.75068737364424", "-73.99341724232818")
    l14 = Local("Madison Square Garden", e14, c14, 19500)
    locais.append(l14)

    #Red Rocks Park & Amphitheatre
    e15 = Endereco("W Alameda Parkway", 18300, "Parque e Anfiteatro", "Parque Natural", "Morison", "Colorado", "80465")
    c15 = Coordenadas("39.665641335948855", "-105.20520087116408")
    l15 = Local("Red Rocks Park & Amphitheatre", e15, c15, 9500)
    locais.append(l15)

def geraJson():
    for local in locais:
        addr = local.endereco
        endereco = {
            "rua" : addr.rua,
            "numero" : addr.numero,
            "complemento" : addr.complemento,
            "bairro" : addr.bairro,
            "cidade" : addr.cidade,
            "uf" : addr.uf,
            "cep" : addr.cep
        }
        coord = local.coordenadas
        coordenadas = {
            "latitude" : coord.latitude,
            "longitude" : coord.longitude
        }
        localizacao = {
            "nome" : local.nome,
            "endereco" : endereco,
            "coordenadas" : coordenadas,
            "capacidade" : local.capacidade
        }
        locaisJson.append(localizacao)

def generate_location():
    cadastra()
    geraJson()
    return[locaisJson, locais]
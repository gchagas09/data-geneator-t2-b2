class Ingresso:
    num_ingresso = 1
    def __init__(self, assento, data_aquisicao, usuario_email):
        self.num_ingresso = Ingresso.num_ingresso
        self.assento = assento
        self.data_aquisicao = data_aquisicao
        self.usuario_email = usuario_email
        Ingresso.num_ingresso +=1
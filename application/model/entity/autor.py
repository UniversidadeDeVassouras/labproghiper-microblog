from usuario import Usuario

class Autor(Usuario):

    def __init__(self, publicacoes = []):
        self._publicacoes = publicacoes
    
    def get_publicacoes(self):
        return self._publicacoes
        
    def set_publicacao(self, nova_pub):
        self._publicacoes.append(nova_pub)
        
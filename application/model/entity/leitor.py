from usuario import Usuario

class Leitor(Usuario):

    def __init__(self, autores_seguidos = [], pubs_curtidas = []):
        self._autores_seguidos = autores_seguidos
        self._pubs_curtidas = pubs_curtidas
    
    def get_autores_seguidos(self):
        return self._autores_seguidos

    def get_pubs_curtidas(self):
        return self._pubs_curtidas

    def set_autor_curtido(self, novo_autor):
        self._autores_seguidos.append(novo_autor)

    def set_pub_curtida(self, nova_pub):
        self._pubs_curtidas.append(nova_pub)
    

    
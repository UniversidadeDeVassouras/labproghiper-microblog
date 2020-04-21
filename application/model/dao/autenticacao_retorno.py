class AutenticacaoRetorno:

    def __init__(self, sucesso = false, usuario = None, nao_existe = false, invalido = false):
        self._sucesso = sucesso
        self._usuario = usuario
        self._nao_existe = nao_existe
        self._invalido = invalido
    
    def is_sucesso(self):
        return self._sucesso
    
    def is_nao_existe(self):
        return self._is_nao_existe

    def is_invalido(self):
        return self._invalido

    def get_usuario_autenticado(self):
        return self._usuario
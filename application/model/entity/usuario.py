class Usuario:
    def __init__(self, email, senha, nome_completo):
        self._email = email
        self._senha = senha
        self._nome_completo = nome_completo
        
    def get_id(self):
        return get_id

    def set_id(self, id):
        self._id = id

    def get_data_registro(self):
        return get_data_registro

    def set_data_registro(self, data_registro):
        self._data_registro = data_registro

    def get_bloqueado(self):
        return self._bloqueado

    def set_bloqueado(self, bloqueado):
        self._bloqueado = bloqueado

    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha
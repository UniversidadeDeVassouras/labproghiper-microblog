from autenticacao_retorno import AutenticacaoRetorno

class UsuarioDAO:

    def __init__(self):
        self._usuarios = []

    # Algoritmo - Separando a existência da combinação
    # Buscar o usuário com o email informado
    # Se usuário foi encontrado
        #então se a senha é a mesma que a informada
            #usuário autenticado
        #senão
            #email e/ou senha incorrentos
    #Senão
        #Informar que usuário não existe / não cadastrado

    def _get_usuario_por_email(self, email):
        for usuario in self._usuarios:
            if usuario.get_email() == email:
                return usuario      
        return None

    def login(self, usuario_procurado):
        usuario = self.get_usuario_por_email(usuario_procurado.get_email())
        if usuario == None:
            return AutenticacaoRetorno(nao_existe = True)
        elif usuario_procurado.get_senha() == usuario.get_senha():
            return AutenticacaoRetorno(sucesso = True, usuario = usuario)
        return AutenticacaoRetorno(invalido = False)
        
    def cadastrar(self, usuario):
        if self._get_usuario_por_email(usuario.get_email()) != None: 
            return False
        self._usuarios.append(usuario)
        return True
from application import app
from flask import render_template, request
from application.model.dao.usuario_dao import UsuarioDAO
from application.model.entity.usuario import Usuario

usuarioAutenticado = None

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
       email = request.form['email']
       senha = request.form['senha']
       usuario = Usuario(email, senha, None)
       autenticacao = UsuarioDAO().login(usuario)
       if autenticacao.is_sucesso():
         usuarioAutenticado = autenticacao.get_usuario_autenticado()
         return render_template("index.html")
       elif autenticacao.is_nao_existe():
         return render_template("register.html", usuario = usuario)
       elif autenticacao.is_invalido():
         return render_template("index.html", login_invalido = True, usuario = usuario)

    if request.method == 'GET':   
          return render_template("index.html")
                 
   

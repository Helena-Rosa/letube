from flask import Flask, render_template, redirect, request, session, flash
import random
import mysql.connector
from model.musica import recuperar_musicas, salvar_musica, deletar, ativar
from model.genero import recuperar_generos 
from model.usuario_model import cadastrar_usuario, verificar_usuario



app= Flask(__name__)

app.secret_key = "blueEtiago"
    


@app.route ("/")
@app.route("/home", methods=["GET"])
def pagina_principal():
    musicas = recuperar_musicas(True)
    generos = recuperar_generos()
    return render_template("principal.html", musicas = musicas , generos = generos )


@app.route ("/admin")
def pagina_admin():
    if "usuario_logado" not in session:
        return redirect ("/login")
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)


@app.route("/musica/post", methods= ["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url = request.form.get("url_imagem")
    genero = request.form.get("genero")
    if salvar_musica(cantor, duracao, nome_musica, genero, url):
        return redirect("/admin")
    else: 
        return "ERRO AO ADICIONAR MUSICA"


@app.route("/musica/delete/<codigo>")
def excluir_musica(codigo):
    deletar(codigo)
    return redirect("/admin")


@app.route("/musica/ativar/<codigo>/<status>")
def pag_ativar(codigo,status):
    ativar(codigo,status)
    return redirect("/admin")


@app.route ("/cadastro")
def pagina_cadastro(): 
    return render_template("cadastro.html")


@app.route("/cadastro", methods= ["POST"])
def cadastro_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    cadastrar_usuario (usuario, senha)
    return redirect ("/cadastro")

@app.route ("/login")
def pagina_login(): 
    return render_template("login.html")

@app.route ("/login", methods= ["POST"])
def rota_login_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if verificar_usuario(usuario, senha):
        session["usuario_logado"] = usuario
        flash(f"Seja Bem-vindo , {usuario}!")
        return redirect("/admin")
    else:
        flash("Usuario ou senha incorreto","danger")
        flash("Tente novamente")
        return redirect("/login")
    
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")



    

    


app.run (debug=True, host= "0.0.0.0", port="8080")
    










if __name__ == "__main__":
    app.run(debug=True)

































































































































































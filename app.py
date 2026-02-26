from flask import Flask, render_template, redirect, request
import random
import mysql.connector
from model.musica import recuperar_musicas, salvar_musica, deletar, ativar
from model.genero import recuperar_generos


app= Flask(__name__)
    


@app.route ("/")
@app.route("/home", methods=["GET"])
def pagina_principal():
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("principal.html", musicas = musicas , generos = generos )



@app.route ("/admin")
def pagina_admin():
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


@app.route("/musica/ativar/<codigo>")
def pag_ativar(codigo):
    ativar(codigo)
    return redirect("/admin")






if __name__ == "__main__":
    app.run(debug=True)

































































































































































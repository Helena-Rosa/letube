from flask import Flask, render_template, redirect, request
import random
import mysql.connector
from model.musica import recuperar_musicas
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



if __name__ == "__main__":
    app.run(debug=True)

































































































































































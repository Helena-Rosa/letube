from flask import Flask, render_template, redirect, request
import random
import mysql.connector

app= Flask(__name__)
    


@app.route ("/")
@app.route("/home", methods=["GET"])
def pagina_principal():
    
    conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "lenamusic"
    )

    #CRIANDO CURSOR
    cursor = conexao.cursor(dictionary=True)



    musicas = cursor.fetchall()

    #EXECULTANDO A CONSULTA
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero from music;")


    generos = cursor.fetchall()

    conexao.close()

    return render_template("principal.html", musicas = musicas , generos = generos )

if __name__ == "__main__":
    app.run(debug=True)

































































































































































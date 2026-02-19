from database.conexao import conectar

def recuperar_generos():
    conexao, cursor = conectar()

    #execultando a consulta 
    cursor.execute ("SELect nome, icone, cor From genero;")

    #recuperando os dados
    generos = cursor.fetchall()
    
    #fechar a conexao
    conexao.close()

    return generos
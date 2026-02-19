from database.conexao import conectar 


def recuperar_musicas():
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    #execultando a consulta 
    cursor.execute ("SELect codigo, cantor, duracao, nome, nome_genero, url_imagem from music")

    #recuperando os dados
    musicas = cursor.fetchall()
    
    #fechar a conexao
    conexao.close()

    return musicas
from database.conexao import conectar 


def recuperar_musicas():
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    #execultando a consulta 
    cursor.execute ("SELect codigo, cantor, duracao, nome, nome_genero, url_imagem, ativo from music")

    #recuperando os dados
    musicas = cursor.fetchall()
    
    #fechar a conexao
    conexao.close()

    return musicas


def salvar_musica(cantor:str, duracao:str, nome_musica:str, nome_genero:str, url_imagem:str) -> bool:
    """
    ela confere se o salvamento da musica deu certo ou nao (bool) e vai mandar pro banco de dados.
    """

    try:
        conexao, cursor = conectar()
        cursor.execute("""INSERT INTO music (cantor, duracao, nome, url_imagem, nome_genero)
                        VALUES (%s, %s, %s, %s, %s)""",
                        (cantor, duracao, nome_musica, url_imagem, nome_genero))
        
        conexao.commit()

        conexao.close()

        return True

    except Exception as erro:
            print (erro)
            return False
  

def deletar(codigo):
     
    conexao, cursor = conectar()
    cursor.execute("DELETE FROM music WHERE codigo = %s",[codigo])
    conexao.commit()
    conexao.close()



def ativar(codigo: int, status:bool):
     
    conexao, cursor = conectar()
    cursor.execute("UPDATE music SET ativo = %s WHERE codigo = %s", [status, codigo])
    conexao.commit()
    conexao.close()


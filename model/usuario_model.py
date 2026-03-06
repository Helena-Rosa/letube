from database.conexao import conectar

def cadastrar_usuario(login:str, senha: str):
    conexao, cursor = conectar()


    cursor.execute("""
INSERT INTO CADASTRO
                   (nome_usuario, 
                   senha)

                   VALUE
                        (%s,
                        %s);
                   
                """,
                [login, senha]
                   )
    
    conexao.commit()
    conexao.cursor()



def verificar_usuario(usuario: str, senha: str) -> list:

    """
    função que verifica se o usuario esta cadastrado
    se estiver cadastrado retorna os dados do ususario 
    se nao etiver cadastrado retorna none.
    """

    conexao, cursor = conectar ()
    cursor.execute("SELECT usuario, senha FROM cadastro WHERE ususario = %s and senha = %s", [usuario, senha])
    usuario = cursor.fetchone()
    
    conexao.close()

    return usuario

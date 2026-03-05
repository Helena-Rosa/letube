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
import mysql.connector



def conectar ():
    tipo_local = "nuvem"
    if tipo_local == "local":

        conexao = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "root",
            database = "lenamusic"
    )

        cursor = conexao.cursor(dictionary=True)
    else:
        conexao = mysql.connector.connect(
        host = "mysql-2b19cdd4-helenarosa-servidor.a.aivencloud.com",
        port = 12587,
        user = "avnadmin",
        password = "AVNS_QUnXnjkva_KcezN4XSF",
        database = "lenamusic"
    )
       
    
    


    #CRIANDO CURSOR
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor 

import mysql.connector 

def conectar():
    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='Login'
    )
    # Verifica se a conexão foi realizada com sucesso
    if conexao.is_connected():
        print('Conectado com sucesso')
        cursor = conexao.cursor()

    return conexao, cursor

def consultar_usuarios():
    conexao, cursor = conectar()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor
    cursor.close()
    conexao.close()
    return resultado

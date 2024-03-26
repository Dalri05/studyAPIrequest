import mysql.connector
from fastapi import FastAPI


app = FastAPI()

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="pessoas"
    )
    cursor = conexao.cursor()
except:
    print("Erro de conexão com o banco de dados:")
    exit(1)

class comandos:
    def readuser(idnome):
        comando = 'SELECT * FROM pessoas.usuarios WHERE idnome=%s' 
        cursor.execute(comando, (idnome,))
        resultado = cursor.fetchall()
        return resultado

    def read():
        comando = 'SELECT * FROM pessoas.usuarios'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado
    
    def insert():
        nome = input("digite o nome")
        idade = int(input('digite a idade'))
        email = input("digite o email")
        comando =f'INSERT INTO usuarios (nome, idade, email) VALUES ("{nome}", "{idade}", "{email}")'
        cursor.execute(comando)
        conexao.commit()

    def delete(idnome):
        comando = 'DELETE FROM pessoas.usuarios WHERE idnome=%s'
        cursor.execute(comando, (idnome))
        resultado = conexao.commit()
        return resultado

class req:
    @app.get('/user')
    def get_user():
        return comandos.read()

    @app.get('/user/{idnome}')
    def get_userid(idnome:int):
        return comandos.readuser(idnome)


    @app.post('/insert')
    def post_info():
        return comandos.insert()
    
    @app.delete('/deleteuser/{idnome}')
    def delete_user(idnome:int):
        return comandos.delete()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

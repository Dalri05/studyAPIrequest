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
except mysql.connector.Error as err:
    print(f"Erro de conexão com o banco de dados: {err}")
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

@app.get('/user')
def get_user():
    return comandos.read()

@app.get('/user/{idnome}')
def get_userid(idnome:int):
    return comandos.readuser(idnome)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

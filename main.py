import mysql.connector
from fastapi import FastAPI
import json


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
        cursor.execute(comando, (idnome,))
        resultado = conexao.commit()
        return resultado
    
    def edit(idnome, nome, idade, email): 
        comando_verificar = 'SELECT * FROM pessoas.usuarios WHERE idnome = %s'
        cursor.execute(comando_verificar, (idnome,))
        resultado = cursor.fetchone()

        if resultado: 
            comando = 'UPDATE usuarios SET nome = %s, idade = %s, email = %s WHERE idnome = %s'
            cursor.execute(comando, (nome, idade, email, idnome))
            conexao.commit()
            return "Usuário atualizado com sucesso"
        else:
            # O usuário não foi encontrado
            return "Usuário não encontrado"


    
    def insertusers(usuarios_json): 
        with open(usuarios_json, 'r') as arquivo:
            dados_json = json.load(arquivo)

        for usuario in dados_json:
            nome = usuario["nome"]
            idade = usuario["idade"]
            email = usuario["email"]
            comando = f'INSERT INTO usuarios (nome, idade, email) VALUES ("{nome}", {idade}, "{email}")'
            cursor.execute(comando)
            conexao.commit()


class req:
    @app.get('/users')
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
        return comandos.delete(idnome)

    @app.put('/update/user/{idnome}')
    def update_user(idnome: int, user_data: dict):
        nome = user_data.get('nome')
        idade = user_data.get('idade')
        email = user_data.get('email')
        return comandos.edit(idnome, nome, idade, email)


    @app.post('/insertusers')
    def post_info(usuarios_json: str):
        return comandos.insertusers(usuarios_json)


usuarios_json = "arquivos/usuario.json"
insert_user = "arquivos/insert.json"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

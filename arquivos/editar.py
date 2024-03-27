import json
import os 

insert_user = "arquivos/usuario.json"

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

usuario = {
    "nome": nome,
    "idade": idade,
    "email": email
}

try:
    if os.path.exists(insert_user):
        os.remove(insert_user)
except FileNotFoundError:
    pass

if os.path.exists(insert_user):
    with open(insert_user, 'r') as file:
        dados_json = json.load(file)
else:
    dados_json = []

dados_json.append(usuario)

with open(insert_user, 'w') as file:
    json.dump(dados_json, file, indent=4)

print("Dados escritos com sucesso no arquivo json.")

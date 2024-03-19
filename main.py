from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get('/user', response_model=User)
def get_user():
    user_data = {'name': 'Fulano', 'age': 30}
    return User(**user_data)

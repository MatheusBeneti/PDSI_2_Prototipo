from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import classes

app = FastAPI()

class Mensagem(BaseModel):
    titulo: str
    conteudo: str
    publicada: bool = False

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao FastAPI!!!"}

@app.post('/body')
def read_body(res = Body(...)):  
    print(res)
    return {"message": f"Essa é a response: {res}"}

@app.post('/baseModel')
def baseModel(res: Mensagem):  
    print(res)
    return {"message": f"Essa é a response: {res}"}
    


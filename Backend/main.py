from fastapi import FastAPI
#from fastapi.params import Body
from classes import Mensagem
import model
from database import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao FastAPI!"}

#@app.post('/body')
#def read_body(res = Body(...)):  
#   print(res)
#   return {"message": f"Essa é a response: {res}"}

@app.post('/create')
def create_table(res: Mensagem):  
    print(res)
    return {"message": f"Essa é a response: {res}"}
    


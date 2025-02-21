from fastapi import FastAPI, status, Depends
from typing import List
import classes
from classes import Mensagem
import model
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from webScrapping import exec

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/", status_code=status.HTTP_201_CREATED)
def read_root():
    return {"message": "Bem-vindo ao FastAPI!"}


@app.post('/create', status_code=status.HTTP_201_CREATED)
def create_table(res: Mensagem, db: Session = Depends(get_db)):  
    created_message = model.Model_Mensagem(**res.dict())
    db.add(created_message)
    db.commit()
    db.refresh(created_message)
    return {"message": created_message.__dict__}


@app.get("/mensagens", response_model=List[classes.Mensagem], status_code=status.HTTP_200_OK)
async def buscar_valores(db: Session = Depends(get_db), skip: int = 0, limit: int=100):
    mensagens = db.query(model.Model_Mensagem).offset(skip).limit(limit).all()
    return mensagens

@app.get("/scrapping")
def scrapping(db: Session = Depends(get_db)):
    return exec(db)  



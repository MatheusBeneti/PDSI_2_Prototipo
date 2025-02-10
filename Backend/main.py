from fastapi import FastAPI, status, Depends
from classes import Mensagem
import model
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

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
    created_message = model.Model_Mensagem(res.model_dump())
    db.add(created_message)
    db.commit()
    db.refresh(created_message)
    return {"message": created_message}


    


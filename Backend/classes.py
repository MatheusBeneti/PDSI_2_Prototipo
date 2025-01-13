from pydantic import BaseModel

class Mensagem(BaseModel):
    title: str
    content: str
    isPublished: bool = False
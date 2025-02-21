import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from database import get_db
import model
from sqlalchemy import Column, String
from database import Base

class FooterLink(Base):
    __tablename__ = "footer_links"

    nome = Column(String, primary_key=True, index=True)
    url = Column(String, nullable=False)

def exec(db: Session):
    # URL do site
    url = "https://www.ufu.br/"  # Substitua pela URL correta

    # Fazer a requisição HTTP
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar a seção específica do footer
        footer_section = soup.find("ul", {"data-block": "footer_three"})
        
        # Se não encontrar, retorna um dicionário vazio
        if not footer_section:
            return {}
        
        # Extrair os nomes e URLs e salvar no banco de dados
        links_data = []
        for item in footer_section.find_all("a"):
            name = item.text.strip()
            url = item["href"]
            
            # Criar entrada no banco de dados
            new_entry = FooterLink(nome=name, url=url)
            db.add(new_entry)
            links_data.append({"nome": name, "url": url})
        
        db.commit()
        return links_data
    else:
        return {"error": "Erro ao acessar o site."}

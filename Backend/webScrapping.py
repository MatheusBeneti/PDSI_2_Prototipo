import requests
from bs4 import BeautifulSoup

def exec():
    # URL do site
    url = "https://www.ufu.br/"  # Substitua pela URL correta

    # Fazer a requisição HTTP
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar a seção do footer
        footer = soup.find("footer")  # Pode ser necessário ajustar o seletor
        
        # Extrair os títulos e links das seções
        sections = {}
        for section in footer.find_all("div", class_="some-class"):  # Ajuste conforme necessário
            title = section.find("h2").text.strip()
            links = [a.text.strip() for a in section.find_all("a")]
            sections[title] = links

        # Exibir os dados extraídos
        for title, links in sections.items():
            print(f"{title}:")
            for link in links:
                print(f"  - {link}")
    else:
        print("Erro ao acessar o site.")

from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def teste_hello():
    response = client.get("/")
    assert response.status_code == 201
    assert response.json() == {"message": "Bem-vindo ao FastAPI!!!"}
    
def teste_quadrado():
    num = 4
    response = client.get(f"/quadrado/{num}")
    assert response.status_code == 200
    assert response.text == str(num ** 2)

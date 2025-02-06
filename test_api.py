from fastapi.testclient import TestClient
from api import app  # Assure-toi que ton fichier API s'appelle bien api.py

client = TestClient(app)

def test_welcome():
    """Test de la route d'accueil"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Bienvenu (e) dans notre API"

def test_prediction():
    """Test de l'endpoint de prédiction"""
    data = {"feature1": 10.5, "feature2": 20.3}  # Mets tes vraies features
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "probability" in response.json()
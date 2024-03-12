from fastapi.testclient import TestClient
import shutil
from pathlib import Path
import sys
sys.path.append('../') 
from app.main import app
import pandas as pd

client = TestClient(app)

def test_search_resimages_file_found():
    caminho_origem = Path("./tests/data_tests/output_2100-01-01.csv")
    caminho_destino = Path("./app/data/results_images/output_2100-01-01.csv")
    shutil.copy(caminho_origem, caminho_destino)

    today = pd.Timestamp("today").strftime("%Y-%m-%d")
    response = client.get(f"/api/search_resimages?filename={today}")
    assert response.status_code == 200
    caminho_destino.unlink()

def test_search_resimages_file_not_found():
    response = client.get("/api/search_resimages?filename=5100-01-01")
    assert response.status_code == 200 


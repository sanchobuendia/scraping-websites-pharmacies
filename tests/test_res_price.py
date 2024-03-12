from fastapi.testclient import TestClient
import shutil
from pathlib import Path
import sys
sys.path.append('../') 
from app.main import app

client = TestClient(app)

def test_search_resimages_file_found():
    caminho_origem = Path("./tests/data_tests/output_2100-01-01.csv")
    caminho_destino = Path("./app/data/results_price/output_2100-01-01.csv")
    shutil.copy(caminho_origem, caminho_destino)

    response = client.get("/api/resultprice")
    assert response.status_code == 200
    caminho_destino.unlink()


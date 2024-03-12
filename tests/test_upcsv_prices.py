from fastapi.testclient import TestClient
import sys
sys.path.append('../') 
from app.main import app
from pathlib import Path
from datetime import datetime

client = TestClient(app)

def test_upload_image():

    response = client.post("/api/uploadprice/", files={"csv_file": open("./tests/data_tests/BUSCAR_PRECOS.csv", "rb")})

    assert response.status_code == 200

    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = Path(f"./app/data/data_price/input_{today}.csv")
    file_path.unlink()



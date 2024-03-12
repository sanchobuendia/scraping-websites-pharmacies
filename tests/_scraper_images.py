from fastapi.testclient import TestClient
import sys
sys.path.append('../') 
from app.main import app
from pathlib import Path
from datetime import datetime

client = TestClient(app)

def test_upload_image():

    response = client.post("/api/uploadprice/", files={"csv_file": open("./tests/data_tests/BUSCAR_IMAGENS.csv", "rb")})
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with open(r"tests\data_tests\BANNER MOSAICO_PANVEL_MIP.jpg", "rb") as f:
        files = {"file": ("BANNER MOSAICO_PANVEL_MIP.png", f)}
        response = client.post("/api/upimages/", files=files)

    response = client.post("/api/scraperimages/")
    
    assert response.status_code == 200

    file_path = Path(f"./app/data/data_price/input_{today}.csv")
    file_path.unlink()

    file_path = Path(r"app\data\target_images\BANNER MOSAICO_PANVEL_MIP.png")
    file_path.unlink()



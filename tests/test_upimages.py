from fastapi.testclient import TestClient
import shutil
from pathlib import Path
import os
import sys
sys.path.append('../') 
from app.main import app

client = TestClient(app)

# Define a test function for the /upimages/ route
def test_upload_file():
    # Use the TestClient to simulate an HTTP request to the /upimages/ route
    with open(r"tests\data_tests\BANNER BIG TOWER_PANVEL_MILLAR.jpg", "rb") as f:
        files = {"file": ("BANNER BIG TOWER_PANVEL_MILLAR.png", f)}
        response = client.post("/api/upimages/", files=files)

    assert response.status_code == 200
    assert response.json() == {"filename": "BANNER BIG TOWER_PANVEL_MILLAR.png"}

    file_path = Path(r"app\data\target_images\BANNER BIG TOWER_PANVEL_MILLAR.png")
    file_path.unlink()



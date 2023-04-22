from fastapi.testclient import TestClient
import sys
sys.path.append("..")
from api import app

client = TestClient(app)

def test_get_mcp():
    response = client.get("/market/mcp")
    assert response.status_code == 200
    assert response.json() == {"message": "success"}


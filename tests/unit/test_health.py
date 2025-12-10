import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../backend/src"))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

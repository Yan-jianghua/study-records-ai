from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_info_returns_project_name() -> None:
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"name": "学习记录管理器与AI助手"}
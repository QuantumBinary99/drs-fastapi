import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_service_info():
    response = client.get("/service-info")
    assert response.status_code == 200
    assert response.json()["id"] == "com.example.drs"

def test_get_object():
    response = client.get("/objects/314159")
    assert response.status_code == 200
    assert response.json()["id"] == "314159"

def test_get_object_not_found():
    response = client.get("/objects/123")
    assert response.status_code == 404
    assert response.json()["detail"] == "Object not found"

def test_get_access_url():
    response = client.get("/objects/314159/access/access123")
    assert response.status_code == 200
    assert response.json()["url"] == "https://drs.example.org/314159"

def test_get_access_url_not_found():
    response = client.get("/objects/314159/access/access456")
    assert response.status_code == 404
    assert response.json()["detail"] == "Access URL not found"
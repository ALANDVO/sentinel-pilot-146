"""Test health endpoint."""
import pytest
from fastapi.testclient import TestClient
from sentinel_pilot_146.api import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


def test_health_endpoint(client):
    """Test health check endpoint."""
    response = client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "healthy"
    assert data["service"] == "sentinel-pilot-146"
    assert data["version"] == "0.1.0"


def test_root_endpoint(client):
    """Test root endpoint."""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["message"] == "Sentinel Pilot 146 API is running"
    assert data["version"] == "0.1.0"


def test_api_doc(client):
    """Test that API docs are accessible."""
    response = client.get("/docs")
    
    assert response.status_code == 200
    # Check for swagger-ui related content instead of "FastAPI"
    assert "swagger-ui" in response.text or "Sentinel Pilot 146 API - Swagger UI" in response.text


def test_api_redoc(client):
    """Test that ReDoc is accessible."""
    response = client.get("/redoc")
    
    assert response.status_code == 200
    # Check for redoc related content instead of "FastAPI"
    assert "ReDoc" in response.text or "Sentinel Pilot 146 API - ReDoc" in response.text


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""Test SEO capabilities endpoint."""
import pytest
from fastapi.testclient import TestClient
from sentinel_pilot_146.api import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


def test_seo_capabilities_endpoint(client):
    """Test SEO capabilities endpoint."""
    response = client.get("/seo/capabilities")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["service"] == "sentinel-pilot-146"
    assert "capabilities" in data
    assert isinstance(data["capabilities"], list)
    assert len(data["capabilities"]) > 0
    assert data["version"] == "0.1.0"
    assert data["sub_skills_count"] == 26
    assert data["sub_agents_count"] == 19
    
    # Verify all expected capabilities are present
    expected_caps = [
        "technical-seo",
        "ee-at-analysis",
        "schema-markup",
        "geo-aeo",
        "backlinks-analysis",
        "local-seo",
        "e-commerce-seo",
        "international-seo",
        "google-apis",
        "pdf-excel-reporting"
    ]
    for cap in expected_caps:
        assert cap in data["capabilities"], f"Missing capability: {cap}"

"""Core API module for Sentinel Pilot 146."""
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any

app = FastAPI(
    title="Sentinel Pilot 146 API",
    description="AI/ML Developer Tools API",
    version="0.1.0"
)

@app.get("/health")
async def health_check() -> JSONResponse:
    """Health check endpoint.
    
    Returns:
        JSONResponse: Health status information.
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "sentinel-pilot-146",
            "version": "0.1.0"
        }
    )

@app.get("/")
async def root() -> JSONResponse:
    """Root endpoint.
    
    Returns:
        JSONResponse: Welcome message.
    """
    return JSONResponse(
        status_code=200,
        content={
            "message": "Sentinel Pilot 146 API is running",
            "version": "0.1.0"
        }
    )

@app.get("/about")
async def about() -> JSONResponse:
    """About endpoint.
    
    Returns:
        JSONResponse: About information including maintainer contact.
    """
    return JSONResponse(
        status_code=200,
        content={
            "maintainer": "Alan Vo",
            "website": "https://alanvo.net",
            "x_profile": "https://x.com/alanvoasi",
            "service": "sentinel-pilot-146",
            "version": "0.1.0"
        }
    )

@app.get("/seo/capabilities")
async def seo_capabilities() -> JSONResponse:
    """SEO capabilities endpoint.
    
    Returns:
        JSONResponse: Available SEO skills and capabilities.
    """
    return JSONResponse(
        status_code=200,
        content={
            "service": "sentinel-pilot-146",
            "capabilities": [
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
            ],
            "version": "0.1.0",
            "sub_skills_count": 26,
            "sub_agents_count": 19
        }
    )

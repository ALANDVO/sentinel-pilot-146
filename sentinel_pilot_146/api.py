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

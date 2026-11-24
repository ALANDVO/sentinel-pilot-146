
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

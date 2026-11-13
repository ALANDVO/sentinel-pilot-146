"""Main entry point for Sentinel Pilot 146."""
import uvicorn
from sentinel_pilot_146.api import app

def main():
    """Run the application."""
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()

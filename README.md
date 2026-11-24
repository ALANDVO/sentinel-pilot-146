# Sentinel Pilot 146 — Alan Vo

Current version: `1.2.0`.

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data.

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   python main.py
   ```

3. Test the health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

4. Test SEO capabilities:
   ```bash
   curl http://localhost:8000/seo/capabilities
   ```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /about` - About page
- `GET /seo/capabilities` - SEO capabilities listing

## Testing

Run tests:
```bash
pytest
```

## Development

This is a base implementation for Sentinel Pilot 146. More features will be added incrementally.

### Contact

- Website: https://alanvo.net
- X: https://x.com/alanvoasi

Maintainer: Alan Vo <alanvo@gmail.com>

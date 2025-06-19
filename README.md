# Document Parsing Application

This Flask application parses documents using the RunPulse API. It requires an API key which is supplied via the `API_KEY` environment variable.

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Export your API key before launching the app:
   ```bash
   export API_KEY=<your-key>
   python app/app.py
   ```

## Docker

The Docker image expects the `API_KEY` environment variable at runtime. Example:

```bash
docker build -t document-parser .
docker run -e API_KEY=<your-key> -p 5000:5000 document-parser
```

Alternatively, you can pass the key during build:

```bash
docker build --build-arg API_KEY=<your-key> -t document-parser .
```

## Tests

The tests require the `API_KEY` variable as well. It is set automatically within the test suite, so running

```bash
pytest
```

should work without additional configuration.

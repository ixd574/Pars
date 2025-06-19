# Document Parsing Application

This Flask application parses documents using the RunPulse API. It requires an API key which is supplied via the `API_KEY` environment variable.

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Export your API key and start the Flask server:
   ```bash
   export API_KEY=<your-key>
   python app/app.py
   ```

3. Open `http://localhost:5000` in your browser and upload a document.
   The parsed output will be saved to `app/result.json`.

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

## Deploying to Vercel

Vercel routes all requests to the serverless handler defined in `api/index.py`.
The `vercel.json` configuration uses the `python3.10` runtime:

```json
{
  "functions": { "api/index.py": { "runtime": "python3.10" } },
  "routes": [{ "src": "/(.*)", "dest": "api/index.py" }]
}
```

Deploy with:

```bash
vercel --prod
```

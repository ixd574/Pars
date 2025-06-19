import os
import sys
import importlib
import io
import json
import pytest

# Ensure the API_KEY is set before importing the app module
os.environ.setdefault("API_KEY", "test-key")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app as flask_app
app_module = importlib.import_module("app.app")

@pytest.fixture()
def client(tmp_path, monkeypatch):
    flask_app.config["TESTING"] = True
    flask_app.config["UPLOAD_FOLDER"] = str(tmp_path / "uploads")
    os.makedirs(flask_app.config["UPLOAD_FOLDER"], exist_ok=True)
    monkeypatch.chdir(tmp_path)
    with flask_app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Document Parsing App' in response.data

def test_upload_file_success(client, monkeypatch):
    def fake_process_file(path):
        return {'message': 'ok'}
    monkeypatch.setattr(app_module, 'process_file', fake_process_file)
    data = {'file': (io.BytesIO(b'hello'), 'sample.txt')}
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'ok'}
    with open('result.json') as f:
        assert json.load(f) == {'message': 'ok'}

def test_upload_disallowed_file(client):
    data = {'file': (io.BytesIO(b'hello'), 'sample.exe')}
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 400

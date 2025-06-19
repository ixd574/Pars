import importlib
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_api_key_loaded(monkeypatch):
    monkeypatch.setenv('API_KEY', 'dummy-key')
    module = importlib.reload(importlib.import_module('app.app'))
    assert module.API_KEY == 'dummy-key'

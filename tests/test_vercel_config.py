import json


def test_runtime_version():
    with open('vercel.json') as f:
        config = json.load(f)
    runtime = config['functions']['api/index.py']['runtime']
    assert runtime.startswith('vercel-python@')

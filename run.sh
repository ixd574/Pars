#!/bin/bash

# Start the Flask application
cd /home/ubuntu/deployment/app
export PYTHONPATH=/home/ubuntu/deployment/lib:$PYTHONPATH
if [ -z "$API_KEY" ]; then
  echo "API_KEY environment variable not set" >&2
  exit 1
fi
python3 app.py

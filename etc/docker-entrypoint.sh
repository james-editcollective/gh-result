#!/bin/bash

set -e


# gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker app.main:app
gunicorn --bind unix:/tmp/gunicorn.sock -k uvicorn.workers.UvicornWorker app.main:app --reload
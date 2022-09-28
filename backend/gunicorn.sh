#!/bin/sh
gunicorn --chdir backend run:app -w 2 --threads 2 -b 0.0.0.0:443
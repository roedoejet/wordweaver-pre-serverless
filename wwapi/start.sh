#!/bin/bash
docker run -p 80:80 -v $(pwd)/wwapi:/app/wwapi ww /start-reload.sh
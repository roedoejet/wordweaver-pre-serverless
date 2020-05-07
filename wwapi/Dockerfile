FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py

COPY ./wwapi /app/wwapi

RUN pip install -e /app/
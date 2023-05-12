FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py

COPY ./wordweaver /app/wordweaver

# RUN apt-get update && apt-get install texlive texlive-humanities -y

RUN pip install -e /app/

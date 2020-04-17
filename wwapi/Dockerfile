FROM python:3.7

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./ /app

RUN pip install -e /app

CMD ["uvicorn", "wwapi.main:app", "--host", "0.0.0.0", "--port", "80"]
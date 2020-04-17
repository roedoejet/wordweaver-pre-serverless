FROM python:3.7

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./ /app

RUN pip install -e /app

# Prod
# CMD ["uvicorn", "wwapi.main:app", "--host", "$HOST", "--port", "$PORT"]
# Dev
CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "--port", "80", "--log-level", "debug", "wwapi.main:app"]
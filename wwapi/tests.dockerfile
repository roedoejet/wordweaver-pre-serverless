FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py

COPY ./wwapi /app/wwapi
COPY ./test /app/test
COPY ./start-tests.sh /start-tests.sh

RUN chmod +x /start-tests.sh

RUN pip install -e /app/

CMD ["bash", "-c", "while true; do sleep 1; done"]
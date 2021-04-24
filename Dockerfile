FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app/

RUN python -m pip install -U pip
RUN python -m pip install -r requirements.txt

COPY ./src/ /app/src/

CMD uvicorn src:app --host=0.0.0.0 --port=$PORT

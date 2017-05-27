FROM python:2.7-alpine
MAINTAINER Edward Leoni

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_KEY_ID
ARG AWS_REGION_NAME

RUN mkdir /app
WORKDIR /app

ADD . .

RUN echo "export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID; export AWS_SECRET_KEY_ID=$AWS_SECRET_KEY_ID; export AWS_REGION_NAME=$AWS_REGION_NAME; export FLASK_APP=/app/app.py; flask run --host=0.0.0.0 --port=5000" > /run.sh

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "/run.sh"]

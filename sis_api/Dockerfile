FROM python:3.8.8

COPY . /code

WORKDIR /code

RUN apt-get update -y && \
    pip install -r ./requirements.txt 

ENV TZ=America/Sao_Paulo

EXPOSE 5000

ENTRYPOINT ["python3", "-m", "sis_api"]
FROM python:3.8-buster
ENV PYTHON_UNBUFFERED = 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    apt-get install -y \
    unzip make cmake gcc libc-dev postgresql postgresql-client wget

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
COPY ./app /app

RUN useradd trucker -m -s /bin/bash && \
    chown -R trucker /home/trucker
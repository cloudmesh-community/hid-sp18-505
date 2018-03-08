FROM python:3.6
EXPOSE 5000

RUN apt-get update -y --fix-missing
RUN apt-get upgrade -y
RUN apt-get install -y mongodb-clients psmisc

WORKDIR /opt/app/
COPY ./server /opt/app/
RUN pip install -r requirements.txt

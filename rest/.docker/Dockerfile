FROM python:latest

EXPOSE 5000
EXPOSE 8000

RUN apt-get update --fix-missing -y
RUN apt-get upgrade -y
RUN apt-get install -y psmisc mongodb-clients

WORKDIR /opt/everest

CMD [ "bash" ]
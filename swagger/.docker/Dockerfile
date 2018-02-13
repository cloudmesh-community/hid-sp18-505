FROM python:latest

EXPOSE 5000
EXPOSE 8000
EXPOSE 8080

RUN apt-get update --fix-missing -y
RUN apt-get upgrade -y
RUN apt-get install -y psmisc mongodb-clients binutils libproj-dev gdal-bin

WORKDIR /opt/app
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD [ "bash" ]

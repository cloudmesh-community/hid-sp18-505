FROM python:3.6

RUN apt-get update -y --fix-missing
RUN apt-get upgrade -y
RUN apt-get install -y mongodb-clients psmisc
EXPOSE 5000
EXPOSE 8000

WORKDIR /opt/app/
COPY . /opt/app/
RUN pip install -r requirements.txt
CMD ["bash"]

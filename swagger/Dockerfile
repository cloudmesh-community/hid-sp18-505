FROM python:3.6

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y mongodb-clients psmisc
EXPOSE 5000

WORKDIR /opt/app/
COPY ./server/ /opt/app/
RUN pip install -r requirements.txt
COPY ./bootstrap.sh bootstrap.sh
RUN chmod +x /opt/app/bootstrap.sh
# CMD ["/opt/app/bootstrap.sh"]
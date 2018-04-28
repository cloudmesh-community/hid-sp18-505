FROM python:3.6.5
LABEL maintainer="Averill Cate, Jr <acatejr@gmail.com>"
EXPOSE 8000

RUN apt-get update -y
RUN apt-get install -y binutils libproj-dev gdal-bin postgresql-client

WORKDIR /opt/app
COPY . /opt/app/
RUN pip install -r requirements.txt
CMD ["bash"]

FROM python:3.6
EXPOSE 8000
ENV FLASK_APP app.py

RUN apt-get update -y 

ADD app /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD python -m flask run --port=8000 --host=0.0.0.0
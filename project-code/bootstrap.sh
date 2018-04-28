#!/bin/bash

chown -R $USER:$USER . > /dev/null 2>&1
docker-compose up -d --build
docker exec eapi_app_1 ./manage.py migrate
docker exec eapi_app_1 ./manage.py csu
docker exec eapi_app_1 ./manage.py runscript srer_raingages
docker exec eapi_app_1 ./manage.py runscript srer_precip
docker exec eapi_app_1 ./manage.py runscript wgew_raingages
docker exec eapi_app_1 ./manage.py runscript wgew_precip_events
docker exec eapi_app_1 ./manage.py runserver 0.0.0.0:8000 &

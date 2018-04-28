# EAPI

This the application source code, data sets, and Docker build components of the EAPI application.

In terms of "the cloud", the application was setup to run in an Amazon Elastic Beanstalk instance (EB).

This document does not address the deployment to EB.  EB deployment involves setting up an individual or corporate account that typically require personal information, credit card accounts and other items that are beyond the scope of this project.

[The live version of the application](http://www.earthapi.net)

## Procedures

_Before proceeding, if not already installed, please install and configure Docker for your operating system._  
_This application is best suited for testing and development on a Unix based operating system (e.g., Ubuntu or OSX)._  

These are the steps for running a local version of the application.

Create a .env file.
Edit the .env file and change its settings by following env-template.

### Method 1

    chown -R $USER:$USER . > /dev/null 2>&1
    docker-compose up -d --build
    docker exec eapi_app_1 ./manage.py csu
    docker exec eapi_app_1 ./manage.py migrate
    docker exec eapi_app_1 ./manage.py runscript srer_raingages
    docker exec eapi_app_1 ./manage.py runscript srer_precip
    docker exec eapi_app_1 ./manage.py runscript wgew_raingages
    docker exec eapi_app_1 ./manage.py runscript wgew_precip_events
    docker exec eapi_app_1 ./manage.py runserver 0.0.0.0:8000 &

### Method 2

    chmod +x bootstrap.sh
    ./bootstrap.sh

If everything executes properly open a browser to http://127.0.0.1:8000

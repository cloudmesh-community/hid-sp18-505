#!/bin/bash
export MONGO_HOST=swagger_mongodb_1

cd ./server
python loader.py && python app.py

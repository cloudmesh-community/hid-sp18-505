all: clean start-docker
	@echo "Swagger Project Makefile"

clean:
	@echo "Cleaning .pyc files"
	rm -rf *.pyc	

start-docker:
	touch .env
	echo "export MONGO_HOST=swagger_mongodb_1" >> .env
	@echo "Starting docker."
	docker-compose up -d --build

stop:
	echo "Stopping service."
	docker-compose stop
	
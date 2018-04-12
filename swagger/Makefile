all: clean start-docker
	@echo "Swagger Project Makefile"

clean:
	@echo "Cleaning .pyc files"
	rm -rf *.pyc
	touch .env

start-docker:
	@echo "Starting docker."
	docker-compose up -d --build

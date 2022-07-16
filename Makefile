NAME = ponponon/snapshot
VERSION = 1.0.1

.PHONY: build up down logs

build:  docker-build
up: docker-compose-up
down: docker-compose-down
logs: docker-compose-logs

docker-build:
	docker build -t "${NAME}" .

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down

docker-compose-logs:
	docker-compose logs --tail=100 -f

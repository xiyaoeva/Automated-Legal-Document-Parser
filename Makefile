
.PHONY: train run test up

up:
	docker-compose up -d mongo

train:
	python -m app.train

run:
	python -m app.app

test:
	pytest -q

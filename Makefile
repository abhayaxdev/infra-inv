.PHONY: install migrate env setup collectstatic test makemigrations

install:
	pip install -r requirements.txt

env:
	@if [ -f .env ]; then \
		echo ".env already exists, skipping"; \
	else \
		cp .env.example .env; \
		echo "Created .env from .env.example"; \
	fi

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

setup: install env migrate

collectstatic:
	python manage.py collectstatic --noinput

test:
	python manage.py test
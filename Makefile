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

migrate: env
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

setup:
	@set -e; \
	if [ -d ../.venv ]; then \
		echo "Using existing virtual environment at ../.venv"; \
		_pip="../.venv/bin/pip"; \
		_python="../.venv/bin/python"; \
	else \
		_ans="n"; \
		if [ -t 0 ]; then \
			printf "Create a virtual environment at ../.venv? [y/N] "; \
			read _ans; \
		fi; \
		case "$${_ans:-n}" in \
			[yY]|[yY][eE][sS]) \
				echo "Creating virtual environment..."; \
				python3 -m venv ../.venv; \
				_pip="../.venv/bin/pip"; \
				_python="../.venv/bin/python"; \
				;; \
			*) \
				echo "Skipping virtual environment, using system Python"; \
				_pip="pip"; \
				_python="python"; \
				;; \
		esac; \
	fi; \
	$$_pip install -r requirements.txt; \
	if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env from .env.example"; \
	else \
		echo ".env already exists, skipping"; \
	fi; \
	echo ""; \
	echo "Setup complete. Configure .env, then run: make migrate"

collectstatic:
	python manage.py collectstatic --noinput

test:
	python manage.py test
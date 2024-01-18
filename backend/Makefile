test:
	cd src && poetry run pytest --ds pzaz.settings

setup: dotenv makemigrations migrate test createsuperuser runserver

makemigrations:
	cd src && poetry run python3 manage.py makemigrations

migrate:
	cd src && poetry run python3 manage.py migrate

dotenv:
	cp .env.example .env
	$(info Please fill the dotenv file (.env))

createsuperuser:
	cd src && poetry run python3 manage.py createsuperuser


runserver:
	cd src && poetry run python3 manage.py runserver

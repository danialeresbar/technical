start:
	docker-compose up

build-and-start:
	docker-compose up --build

stop:
	docker-compose down

stop-and-clean:
	docker-compose down -v

drivers:
	docker exec -it technical-web ./manage.py drivers

superuser:
	docker exec -it technical-web ./manage.py createsuperuser

bash:
	docker exec -it technical-web bash

shell:
	docker exec -it technical-web ./manage.py shell

makemigrations:
	docker exec -it technical-web ./manage.py makemigrations

migrate:
	docker exec -it technical-web ./manage.py migrate

test:
	docker exec -it technical-web ./manage.py test

statics:
	docker exec -it technical-web ./manage.py collectstatic --noinput

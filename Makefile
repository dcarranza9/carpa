superuser:
	docker exec -it carpa ./manage.py createsuperuser

shell:
	docker exec -it carpa ./manage.py shell

makemigrations:
	docker exec -it carpa ./manage.py makemigrations

migrate:
	docker exec -it carpa ./manage.py migrate

initialfixture:
	docker exec -it carpa ./manage.py loaddata initial

testfixture:
	docker exec -it carpa ./manage.py loaddata test

test:
	docker exec -it carpa ./manage.py test

statics:
	docker exec -it carpa ./manage.py collectstatic --noinput

makemessages:
	docker exec -it carpa django-admin makemessages

compilemessages:
	docker exec -it carpa django-admin compilemessages

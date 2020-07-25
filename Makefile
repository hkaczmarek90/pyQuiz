app.migrate:
	docker exec -i django python manage.py migrate

app.recreate: app.install app.db.reset app.migrate app.factories

app.install:
	docker exec -i django pip install -r requirements.txt

app.db.reset:
	docker exec -i django python manage.py reset_db --noinput

app.test:
	docker exec -i django python manage.py test

app.makemigrations:
	docker exec -i django python manage.py makemigrations

app.factories:
	docker exec -i django python manage.py loaddata initial_data.yaml

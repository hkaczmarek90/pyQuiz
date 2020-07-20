app.migrate:
	docker exec -i django python manage.py migrate

app.recreate:
    app.install app.db.reset app.migrate

app.install:
	docker exec -i django pip install -r requirements.txt

app.db.reset:
	docker exec -i django python manage.py reset_db --noinput

app.test:
    docker exec -i django python manage.py test

app.makemigrations:
    docker exec -i django python mange.py makemigrations
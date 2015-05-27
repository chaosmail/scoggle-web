# Scoggle - the home of data scores

## Heroku

Add a remote heroku endpoint to your local repository.

```
heroku git:remote -a scoggle
```

Set the Django env vars to use production settings

```
heroku config:set DJANGO_SETTINGS_MODULE=scoggle.settings_production
```

Generate a new Django secret key and add it to the env

```
heroku config:set DJANGO_SECRET_KEY='new_secret_key_goes_here'
```

Push the master branch to heroku.

```
git push heroku master
```

Add a database

```
heroku addons:add heroku-postgresql:dev
```

Start the app

```
heroku ps:scale web=1
```

### Additional Stuff

* `heroku run bash` : runs a bash shell from your local machine
* `heroku run python manage.py collectstatic --noinput` : collects your static files and copies them into the `settings.STATIC_ROOT` directory
# Scoggle - the home of data scores

## Heroku

Add a remote heroku endpoint to your local repository.

```
heroku git:remote -a scoggle
```

Push the master branch to heroku.

```
git push heroku master
```

Install all the dependencies

```
heroku run pip install -r requirements.txt --app scoggle
```

Set the Django env vars to use production settings

```
heroku config:set DJANGO_SETTINGS_MODULE=scoggle.settings_production
```

Collect all your static files

```
heroku run python manage.py collectstatic
```

### Additional Stuff

* `heroku run bash` : runs a bash shell from your local machine
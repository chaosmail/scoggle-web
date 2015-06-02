# Scoggle - the home of data scores

Scoggle is the home of your algorithm scores. Submit, analyze and visualize your performance!

## Run it locally

### Getting Started

Install the dependencies.

```
pip install -r requirements.txt
```

Migrate the database

```
python manage.py migrate
```

Run the development server

```
python manage.py runserver
```

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Getting Started

Create a new project on heroku called `my-scoggle`

Add a remote heroku endpoint to your local repository.

```
heroku git:remote -a my-scoggle
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

Migrate the database

```
heroku run python manage.py migrate
```

Start the app with the heroku free plan

```
heroku ps:scale web=1
```

### Updating the application



### Additional Stuff

* `heroku restart` : restarts the application 
* `heroku logs` : prints the logs from the remote app
* `heroku run bash` : runs a bash shell from your local machine
* `heroku run python manage.py collectstatic --noinput` : collects your static files and copies them into the `settings.STATIC_ROOT` directory
* `heroku plugins:install https://github.com/naaman/heroku-vim` : Installs vim to your heroku shell which can then be accessed via `heroku vim`

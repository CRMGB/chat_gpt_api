# Chat GPT API
Django app to handle questions, topics and prompts to Chat GPT API, store them and display them through a template.

## How to run locally:
Make sure you use a virtual environment and python!

1. Install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```
2. comment the line:

```python
# Needed for Heroku
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
```

3. Make your own .env file with the following content:

```python
SECRET_KEY=<YOUR OWN SECRET KEY>
NAME=<YOUR OWN NAME>
USER=<YOUR OWN USER>
PASSWORD=<YOUR OWN PASSWORD>
HOST='localhost'
API_GPT_KEY=<YOUR OWN API_GPT_KEY>
SECRET_KEY=<YOUR OWN SECRET_KEY>
```

4. Run:

```python
python manage.py migrate
python manage.py runserver
```

## How to run locally with heroku:
- heroku local

## How to deploy to Heroku:

1. Uncomment the line if you commented it for locally setup:

```python
# Needed for Heroku
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
```

2. Push to the server:

```bash
git push heroku main
```

Hosting url:

    - https://chat-gpt-api-django.herokuapp.com/

Run Heroku db:

```bash
heroku run su - postgres
```

## Error handling:

```bash
An error has ocurred contacting ChatGPT, APIError: <error>
Failed to connect to ChatGPT, APIConnectionError: <error>
Failed to connect to ChatGPT, RateLimitError: <error>
```

## How to set the .env credentials with Heroku

```bash
heroku config:set DB_NAME='<your dB name>'
heroku config:set DB_PASSWORD='<your dB pass>'
```
...and so on
    
## Improvements:
- Some unittest will be great!
- Pagination showing the last 5 answers/questions and be able to click them.
- Use Natural Language Processing (NLP) techniques to improve the relevance and accuracy of the responses.
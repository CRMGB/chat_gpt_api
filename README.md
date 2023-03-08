# Chat GPT API
Django app to handle questions, topics and prompts to Chat GPT API, store them and display them through a template.

## How to run locally:
!make sure you use a virtual environment and python!
1.install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```

2. Make your own .env file with the follow content:

```python
API_GPT_KEY = <Your GPT Key> (refer to: https://platform.openai.com/account/api-keys )
```

3. Run:

```python
python manage.py migrate
python manage.py runserver
```

## Error handling:

```bash
An error has ocurred contacting ChatGPT, APIError: <error>
Failed to connect to ChatGPT, APIConnectionError: <error>
Failed to connect to ChatGPT, RateLimitError: <error>
```
    
## Improvements:
- Some unittest will be great!
- Pagination showing the last 5 answers/questions and be able to click them.
- Use Natural Language Processing (NLP) techniques to improve the relevance and accuracy of the responses.
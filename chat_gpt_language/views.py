import openai
from django.conf import settings
from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import View

from chat_gpt_language.forms import QuestionForm
from chat_gpt_language.models import AnswerModel, QuestionModel

openai.api_key = settings.API_GPT_KEY_SETTINGS
 
class GPT3View(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any)-> HttpResponse:
        return render(request, "chat.html")
        
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any)-> HttpResponse:
        """Post method entry point to get the user's input, save it, save chatGPT response
        and render the template with both"""
        if request.method == 'POST':
            question_input = request.POST.get('question', None)
            form = QuestionForm(request.POST)
            print(question_input)
            if form.is_valid():
                try:
                    resp_chat_gpt = contract_chat_gpt(question_input)
                    instance = form.save()
                    question_entry = QuestionModel.objects.get(id=instance.id)
                    answer = AnswerModel.objects.create(
                        question_fk=question_entry, 
                        answer=resp_chat_gpt
                    )
                    context={
                        "questions":QuestionModel.objects.filter().order_by('-created')[:5], 
                        "response": answer
                    }             
                    return render(request, "chat.html", context)
                except:
                    raise "Error"
        else:
            prompt = "Who was Napoleon Bonaparte?"
            resp = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)
            print(str(resp))
            return HttpResponse(str(resp["choices"][0]["text"]))

def contract_chat_gpt(question_input: str) -> str:
    """ Method to contact chat gpt API, the exceptions are taken from the documentation"""
    try:
        resp = openai.Completion.create(
            engine="text-davinci-001", prompt=question_input, max_tokens=1000
        )
        return str(resp["choices"][0]["text"])
    except openai.error.APIError as e:
        raise ValueError(f"An error has ocurred contacting ChatGPT, APIError: {e}")
    except openai.error.APIConnectionError as e:
        raise ValueError(f"Failed to connect to ChatGPT, APIConnectionError: {e}")
    except openai.error.RateLimitError as e:
        raise ValueError(f"Failed to connect to ChatGPT, RateLimitError: {e}")

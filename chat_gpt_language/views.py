import typing
import openai
from django.conf import settings
from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib import messages
from chat_gpt_language.forms import QuestionForm
from chat_gpt_language.models import AnswerModel, QuestionModel

openai.api_key = settings.API_GPT_KEY_SETTINGS

RedirectOrResponse = typing.Union[HttpResponseRedirect, HttpResponse]
 
class GPT3View(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any)-> HttpResponse:
        context={
            "questions":QuestionModel.objects.filter(user__id=self.request.user.id).order_by('-created')[:5], 
        }        
        return render(request, "chat.html", context)
        
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any)-> RedirectOrResponse:
        """Post method entry point to get the user's input, save it, save chatGPT response
        and render the template with both"""
        if request.method == 'POST':
            question_input = request.POST.get('question', None)
            form = QuestionForm(request.POST)
            if form.is_valid():
                try:
                    resp_chat_gpt = contract_chat_gpt(question_input)
                    thought = form.save(commit=False)
                    thought.user = request.user
                    thought.save()
                    answer = AnswerModel.objects.create(
                        question_fk=QuestionModel.objects.last(), 
                        answer=resp_chat_gpt
                    )
                    context={
                        "questions":QuestionModel.objects.filter(user__id=self.request.user.id).order_by('-created')[:5], 
                        "response": answer
                    }             
                    return render(request, "chat.html", context)
                except:
                    messages.error(request, f"An error happened 1: '{resp_chat_gpt}'.")
                return redirect("chat")
            else:
                messages.error(request, f"An error happened 2: '{form.errors}'.")
            return redirect("chat")


def contract_chat_gpt(question_input: str) -> str:
    """ Method to contact chat gpt API, the exceptions are taken from the documentation."""
    try:
        resp = openai.Completion.create(
            engine="text-davinci-001", prompt=question_input, max_tokens=1000
        )
        return str(resp["choices"][0]["text"])
    except openai.error.APIError as e:
        print(f"An error has ocurred contacting ChatGPT, APIError: {e}")
    except openai.error.APIConnectionError as e:
        print(f"Failed to connect to ChatGPT, APIConnectionError: {e}")
    except openai.error.RateLimitError as e:
        print(f"Failed to connect to ChatGPT, RateLimitError: {e}")
    return e

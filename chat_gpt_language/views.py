import openai
from django.conf import settings
from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import View

openai.api_key = settings.API_GPT_KEY_SETTINGS
 
class QuestionView(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any)-> HttpResponse:
        return render(request, "chat.html")
        
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any)-> HttpResponse:
        if request.method == 'POST':
            question_input = request.POST.get('question', None)
            print(question_input)
            try:
                resp = openai.Completion.create(
                    engine="text-davinci-001", prompt=question_input, max_tokens=1000
                )
                return render(
                    request, "chat.html", context={"response":str(resp["choices"][0]["text"]), "page":"register"}
                )
            except:
                raise "Error"
        else:
            prompt = "Who was Napoleon Bonaparte?"
            resp = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=1000)
            print(str(resp))
            return HttpResponse(str(resp["choices"][0]["text"]))            
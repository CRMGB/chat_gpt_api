from django.contrib import admin

from chat_gpt_language.models import AnswerModel, QuestionModel

admin.site.register(QuestionModel)

admin.site.register(AnswerModel)

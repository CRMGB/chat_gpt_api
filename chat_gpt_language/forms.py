from django.forms import ModelForm
from .models import QuestionModel, AnswerModel

class QuestionForm(ModelForm):
    class Meta:
        model = QuestionModel
        fields = ["question"]

class AnswerForm(ModelForm):
    class Meta:
        model = AnswerModel
        fields = ["answer"]
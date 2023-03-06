
from django.urls import path
from .views import QuestionView
from . import views

urlpatterns=[
  path('',views.QuestionView.as_view(), name="csv_upload"),
]
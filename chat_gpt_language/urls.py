
from django.urls import path
from .views import GPT3View
from . import views

urlpatterns=[
  path('',views.GPT3View.as_view(), name="chat"),
]
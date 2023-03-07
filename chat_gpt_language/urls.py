
from django.urls import path
from .views import GPT3View
from . import views

urlpatterns=[
  path('chat',views.GPT3View.as_view(), name="chat"),
]

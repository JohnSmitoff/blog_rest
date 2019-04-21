from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path("^questions/$", views.QuestionList.as_view(), name="questions"),
]

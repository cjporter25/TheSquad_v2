from django.urls import path

# From the same directory, import views
from . import views

urlpatterns = [
    path('submit', views.MySquadSubmission.as_view()),
    path('home', views.MySquadView.as_view()),
]
from django.urls import path

# From the same directory, import views
from . import views

urlpatterns = [
    path('mysquad', views.MySquadView.as_view()),
]
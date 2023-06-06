from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('hello/', views.say_hello),
]

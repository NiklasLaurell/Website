from django.urls import path
from . import views

urlpatterns = [
    path('Test_app/', views.index),
]

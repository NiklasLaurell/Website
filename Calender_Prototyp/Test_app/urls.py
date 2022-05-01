from django.urls import path
from . import views

urlpatterns = [
    path('Test_app/', views.index),
    path('Test_app/move', views.index2),  # domain Test_app.com
]

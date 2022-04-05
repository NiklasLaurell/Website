from django.urls import path

from . import views

urlpatterns = [
    path('schema/', views.index)  # our-domain.com/schema/
]

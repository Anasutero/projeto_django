from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.abre_index, name='abre_index')
]

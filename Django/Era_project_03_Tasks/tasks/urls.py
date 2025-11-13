# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tasks, name='view_tasks'),
    path('add/', views.add_task, name='add_task'),
]

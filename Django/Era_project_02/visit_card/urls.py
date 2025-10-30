from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                      # Главная страница
    path('portfolio/', views.portfolio, name='portfolio'),  # Портфолио
    path('intro/', views.intro, name='intro'),              # Введение в Django
    path('first-page/', views.first_page, name='first_page'), # Первая страница
    path('routing/', views.routing, name='routing'),        # Маршрутизация
    path('jinja-variables/', views.jinja_variables, name='jinja_variables'), # Jinja переменные
    path('jinja-logic/', views.jinja_logic, name='jinja_logic'), # Jinja логика
    path('jinja-loops/', views.jinja_loops, name='jinja_loops'), # Jinja циклы
]

from django.shortcuts import render

def home(request):
    return render(request, 'visit_card/home.html')

def portfolio(request):
    return render(request, 'visit_card/portfolio.html')

def intro(request):
    context = {
        'topic': 'Введение в Django',
        'description': 'Django - это фреймворк для создания веб-приложений на Python.',
        'skills': ['Установка Django', 'Создание проекта', 'Запуск сервера']
    }
    return render(request, 'visit_card/topic_page.html', context)

def first_page(request):
    context = {
        'topic': 'Моя первая страница на Django',
        'description': 'Создание простых страниц и настройка маршрутов.',
        'skills': ['Создание view-функций', 'Настройка URLs', 'Базовые шаблоны']
    }
    return render(request, 'visit_card/topic_page.html', context)

def routing(request):
    context = {
        'topic': 'Маршрутизация в Django',
        'description': 'Изучаем как создавать различные пути для страниц.',
        'skills': ['Параметры в URLs', 'Динамические маршруты', 'Именованные URL']
    }
    return render(request, 'visit_card/topic_page.html', context)

def jinja_variables(request):
    context = {
        'topic': 'Jinja: Переменные и наследование',
        'description': 'Шаблонизатор Jinja позволяет динамически создавать HTML.',
        'skills': ['Переменные в шаблонах', 'Наследование шаблонов', 'Блоки']
    }
    return render(request, 'visit_card/topic_page.html', context)

def jinja_logic(request):
    context = {
        'topic': 'Jinja: Логические выражения',
        'description': 'Использование условий if-else в шаблонах.',
        'skills': ['Условия if/elif/else', 'Логические операторы', 'Фильтры']
    }
    return render(request, 'visit_card/topic_page.html', context)

def jinja_loops(request):
    context = {
        'topic': 'Jinja: Циклы и статические файлы',
        'description': 'Работа со списками и подключение CSS/изображений.',
        'skills': ['Циклы for', 'Работа со списками', 'Подключение статики']
    }
    return render(request, 'visit_card/topic_page.html', context)

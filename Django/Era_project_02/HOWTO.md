# Урок: Создаём многостраничный сайт-визитку и повторяем пройденные темы

## Цель: Создать сайт-визитку с главной страницей и страницами по всем пройденным темам

---

## 🎯 Шаг 1: Подготовка проекта

**Объяснение:** Создаём "штаб" нашего проекта и "рабочее приложение", где будут жить все наши страницы.

```bash
# Создаём главный штаб проекта
django-admin startproject config .

# Создаём наше рабочее приложение для сайта-визитки
python manage.py startapp visit_card
```

**Регистрируем приложение в config/settings.py:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', 
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'visit_card',  # ← Добавляем наше приложение!
]
```
*Комментарий:* Так мы говорим Django: "Теперь ты знаешь о нашем приложении visit_card и будешь с ним работать!"

---

## 🎯 Шаг 2: Создаём "адреса" для страниц (URLs)

**Объяснение:** Каждая страница нашего сайта должна иметь свой адрес, как комната в доме.

**В файле visit_card/urls.py (создаём его):**
```python
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
```

**Подключаем в config/urls.py:**
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visit_card.urls')),  # ← Подключаем наши адреса!
]
```

---

## 🎯 Шаг 3: Создаём "мозг" страниц (Views)

**Объяснение:** Views - это функции-помощники, которые решают, что показать пользователю на каждой странице.

**В visit_card/views.py:**
```python
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
```

---

## 🎯 Шаг 4: Создаём базовый "скелет" сайта

**Объяснение:** Базовый шаблон - это основа, которая повторяется на всех страницах (меню, подвал).

**visit_card/templates/visit_card/base.html:**
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Мой учебный сайт{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'visit_card/css/style.css' %}">
</head>
<body>
    <header>
        <h1>🚀 Мой учебный проект по Django</h1>
        <nav>
            <a href="{% url 'home' %}">Главная</a> |
            <a href="{% url 'portfolio' %}">Портфолио</a> |
            <a href="{% url 'intro' %}">Введение</a> |
            <a href="{% url 'first_page' %}">Первая страница</a> |
            <a href="{% url 'routing' %}">Маршрутизация</a> |
            <a href="{% url 'jinja_variables' %}">Jinja Переменные</a> |
            <a href="{% url 'jinja_logic' %}">Jinja Логика</a> |
            <a href="{% url 'jinja_loops' %}">Jinja Циклы</a>
        </nav>
    </header>

    <main>
        {% block content %}
        <!-- Сюда будет подставляться содержимое других страниц -->
        {% endblock %}
    </main>

    <footer>
        <p>© 2025 Мой учебный проект. Создано с ❤️ на Django</p>
    </footer>
</body>
</html>
```

---

## 🎯 Шаг 5: Создаём главную страницу

**visit_card/templates/visit_card/home.html:**
```html
{% extends 'visit_card/base.html' %}
{% load static %}

{% block title %}Главная страница{% endblock %}

{% block content %}
<div class="hero">
    <h2>Привет! Я изучаю Django</h2>
    <p>Это мой сайт-визитка, где я собрал все проекты и темы, которые мы прошли.</p>
    <img src="{% static 'visit_card/images/my_photo.jpg' %}" alt="Моё фото" class="profile-photo">
</div>

<div class="skills">
    <h3>Что я уже умею:</h3>
    <ul>
        <li>Создавать проекты Django</li>
        <li>Работать с шаблонами Jinja</li>
        <li>Настраивать маршруты (URLs)</li>
        <li>Подключать CSS и изображения</li>
        <li>Создавать многостраничные сайты</li>
    </ul>
</div>
{% endblock %}
```

---

## 🎯 Шаг 6: Создаём страницу портфолио

**visit_card/templates/visit_card/portfolio.html:**
```html
{% extends 'visit_card/base.html' %}
{% load static %}

{% block title %}Моё портфолио{% endblock %}

{% block content %}
<h2>Мои проекты</h2>

<div class="projects">
    <div class="project-card">
        <h3>🎯 Сайт-визитка</h3>
        <p>Многостраничный сайт на Django с информацией о моих навыках.</p>
    </div>
    
    <div class="project-card">
        <h3>📚 Учебные страницы</h3>
        <p>Страницы по всем пройденным темам Django и Jinja.</p>
    </div>
    
    <div class="project-card">
        <h3>🎨 Стильный дизайн</h3>
        <p>Красивое оформление с помощью CSS и адаптивной вёрстки.</p>
    </div>
</div>

<h3>Мои навыки:</h3>
<ul>
    <li>Python программирование</li>
    <li>Django фреймворк</li>
    <li>HTML/CSS верстка</li>
    <li>Работа с Git</li>
    <li>Основы JavaScript</li>
</ul>
{% endblock %}
```

---

## 🎯 Шаг 7: Создаём универсальную страницу для тем

**Объяснение:** Эта страница будет использоваться для ВСЕХ учебных тем. Мы передаём разный контент через context!

**visit_card/templates/visit_card/topic_page.html:**
```html
{% extends 'visit_card/base.html' %}

{% block title %}{{ topic }}{% endblock %}

{% block content %}
<div class="topic-header">
    <h2>{{ topic }}</h2>
    <p class="description">{{ description }}</p>
</div>

<div class="skills-list">
    <h3>Что я изучил в этой теме:</h3>
    <ul>
        {% for skill in skills %}
        <li>✅ {{ skill }}</li>
        {% endfor %}
    </ul>
</div>

<div class="navigation">
    <p><strong>Изучили эту тему? Проверьте свои знания!</strong></p>
    <a href="{% url 'home' %}" class="button">На главную</a>
</div>
{% endblock %}
```

---

## 🎯 Шаг 8: Создаём стили для сайта

**Объяснение:** CSS делает наш сайт красивым! Создаём папку для стилей.

**visit_card/static/visit_card/css/style.css:**
```css
/* Общие стили */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #333;
    line-height: 1.6;
}

/* Шапка */
header {
    background: rgba(255, 255, 255, 0.95);
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

header h1 {
    color: #4a4a4a;
    margin: 0 0 15px 0;
}

nav a {
    color: #667eea;
    text-decoration: none;
    margin: 0 10px;
    font-weight: bold;
    transition: color 0.3s;
}

nav a:hover {
    color: #764ba2;
    text-decoration: underline;
}

/* Основной контент */
main {
    max-width: 1000px;
    margin: 30px auto;
    padding: 30px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.1);
}

/* Герой-секция на главной */
.hero {
    text-align: center;
    padding: 30px 0;
}

.profile-photo {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 5px solid #667eea;
    margin: 20px 0;
}

/* Карточки проектов */
.projects {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin: 30px 0;
}

.project-card {
    flex: 1;
    min-width: 250px;
    background: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    border-left: 4px solid #667eea;
}

/* Списки навыков */
.skills-list ul {
    list-style: none;
    padding: 0;
}

.skills-list li {
    background: #e9ecef;
    margin: 10px 0;
    padding: 10px 15px;
    border-radius: 5px;
    border-left: 4px solid #28a745;
}

/* Кнопки */
.button {
    display: inline-block;
    background: #667eea;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s;
}

.button:hover {
    background: #764ba2;
}

/* Заголовки тем */
.topic-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 30px;
    border-radius: 10px;
    margin-bottom: 30px;
}

.topic-header h2 {
    margin: 0;
    font-size: 2em;
}

.description {
    font-size: 1.2em;
    opacity: 0.9;
}

/* Подвал */
footer {
    text-align: center;
    padding: 20px;
    background: rgba(0, 0, 0, 0.8);
    color: white;
    margin-top: 50px;
}
```

---

## 🎯 Шаг 9: Создаём структуру папок

**Объяснение:** Правильная организация файлов - ключ к успеху!

```
visit_card/
├── templates/
│   └── visit_card/
│       ├── base.html              # Базовый шаблон
│       ├── home.html              # Главная страница
│       ├── portfolio.html         # Портфолио
│       └── topic_page.html        # Универсальная страница тем
├── static/
│   └── visit_card/
│       ├── css/
│       │   └── style.css          # Наши стили
│       └── images/
│           └── my_photo.jpg       # Твоя фотография
```

---

## 🎯 Шаг 10: Запускаем сайт!

```bash
# Запускаем сервер
python manage.py runserver
```

**Открой в браузере:** `http://127.0.0.1:8000/`

## Что ты увидишь:

1. **Главная страница** - с твоим фото и списком навыков
2. **Портфолио** - с проектами и умениями  
3. **8 учебных страниц** - по всем пройденным темам
4. **Красивый дизайн** - с градиентами и анимациями
5. **Единое меню** - для навигации по всему сайту

## 🎉 Поздравляю! 

Ты создал полноценный многостраничный сайт, который:
- Повторяет все пройденные темы
- Имеет красивый дизайн
- Легко расширяется
- Может стать твоим цифровым портфолио!

Теперь ты можешь добавлять новые страницы, менять стили или добавлять настоящие проекты в портфолио! 🚀

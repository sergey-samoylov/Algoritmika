# Урок по Django: Создание сайта "TASKS"

В этом уроке мы создадим простое приложение для управления задачами с возможностью переключения между светлой и темной темами.

## Шаг 1: Создание проекта и приложения

```bash
# Создаем проект Django
django-admin startproject config .

# Создаем приложение tasks
python manage.py startapp tasks
```

## Шаг 2: Настройка проекта

В файле `tasks_project/settings.py` добавляем наше приложение:

```python
# tasks_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Добавляем наше приложение
]

# Добавляем настройки для статических файлов
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

## Шаг 3: Создание базового шаблона

Создаем папку `templates` в директории приложения `tasks`, а внутри нее файл `base.html`:

```html
<!-- tasks/templates/base.html -->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TASKS - Менеджер задач{% endblock %}</title>
    
    <!-- Подключаем CSS стили -->
    <link rel="stylesheet" href="/static/css/style.css">
    
    <!-- Скрипт для переключения темы -->
    <script>
        function toggleTheme() {
            const body = document.body;
            body.classList.toggle('dark-theme');
            body.classList.toggle('light-theme');
            
            // Сохраняем выбор темы в localStorage
            const isDark = body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        }
        
        // При загрузке страницы устанавливаем сохраненную тему
        document.addEventListener('DOMContentLoaded', function() {
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.body.classList.add(savedTheme + '-theme');
        });
    </script>
</head>
<body class="light-theme">
    <header>
        <div class="container">
            <h1>TASKS - Менеджер задач</h1>
            <button id="theme-toggle" onclick="toggleTheme()">🌙</button>
        </div>
    </header>
    
    <main class="container">
        {% block content %}
        <!-- Содержимое страниц будет здесь -->
        {% endblock %}
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 TASKS Manager</p>
        </div>
    </footer>
</body>
</html>
```

## Шаг 4: Создание CSS стилей

Создаем структуру папок для статических файлов и файл стилей:

```bash
mkdir -p static/css
```

Создаем файл `static/css/style.css`:

```css
/* static/css/style.css */

/* Общие стили */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    transition: all 0.3s ease;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Светлая тема */
body.light-theme {
    background-color: #f5f5f5;
    color: #333;
}

body.light-theme header {
    background-color: #4a90e2;
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

body.light-theme footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}

body.light-theme .task-item {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

body.light-theme .btn {
    background-color: #4a90e2;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

body.light-theme .btn:hover {
    background-color: #357abd;
}

body.light-theme .form-input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
}

/* Темная тема */
body.dark-theme {
    background-color: #1a1a1a;
    color: #e0e0e0;
}

body.dark-theme header {
    background-color: #2d3748;
    color: #e2e8f0;
    padding: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
}

body.dark-theme footer {
    background-color: #2d3748;
    color: #e2e8f0;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}

body.dark-theme .task-item {
    background-color: #2d3748;
    border: 1px solid #4a5568;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

body.dark-theme .btn {
    background-color: #4a5568;
    color: #e2e8f0;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

body.dark-theme .btn:hover {
    background-color: #2d3748;
}

body.dark-theme .form-input {
    width: 100%;
    padding: 10px;
    background-color: #2d3748;
    color: #e2e8f0;
    border: 1px solid #4a5568;
    border-radius: 5px;
    margin-bottom: 10px;
}

/* Общие стили компонентов */
header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#theme-toggle {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
}

.task-list {
    margin-top: 2rem;
}

.empty-message {
    text-align: center;
    padding: 2rem;
    color: #666;
}

.add-task-form {
    margin-top: 2rem;
    padding: 20px;
    border-radius: 5px;
}

.form-group {
    margin-bottom: 15px;
}

.form-label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}
```

## Шаг 5: Создание представлений

В файле `tasks/views.py` создаем представления:

```python
# tasks/views.py
from django.shortcuts import render, redirect

# Временное хранилище задач (в реальном приложении используем базу данных)
# Это глобальная переменная, которая будет хранить задачи в памяти
# ВНИМАНИЕ: при перезагрузке сервера все задачи будут потеряны!
tasks_list = []

def view_tasks(request):
    """
    Отображает страницу со списком всех задач.
    
    Если список задач пуст, отображается сообщение об этом.
    В противном случае отображается список всех задач.
    """
    context = {
        'tasks': tasks_list,
        'title': 'Мои задачи'
    }
    return render(request, 'view_tasks.html', context)

def add_task(request):
    """
    Обрабатывает добавление новой задачи через POST запрос.
    
    Если метод запроса POST, извлекает данные формы (название задачи)
    и добавляет новую задачу в список. После успешного добавления
    перенаправляет пользователя на страницу со списком задач.
    
    Если метод GET, просто отображает форму для добавления задачи.
    """
    if request.method == 'POST':
        # Извлекаем данные из POST запроса
        task_title = request.POST.get('task_title', '').strip()
        
        # Проверяем, что поле не пустое
        if task_title:
            # Добавляем задачу в список
            # В реальном приложении здесь будет сохранение в базу данных
            tasks_list.append({
                'id': len(tasks_list) + 1,
                'title': task_title,
                'completed': False
            })
            
            # Перенаправляем на страницу со списком задач
            # Это предотвращает повторную отправку формы при обновлении страницы
            return redirect('view_tasks')
    
    # Если метод GET или если форма невалидна, отображаем форму
    context = {
        'title': 'Добавить задачу'
    }
    return render(request, 'add.html', context)
```

## Шаг 6: Создание шаблонов страниц

Создаем файл `tasks/templates/view_tasks.html`:

```html
<!-- tasks/templates/view_tasks.html -->
{% extends "base.html" %}

{% block title %}{{ title }} - TASKS{% endblock %}

{% block content %}
<div class="task-list">
    <h2>{{ title }}</h2>
    
    {% if tasks %}
        <!-- Если есть задачи, отображаем их список -->
        {% for task in tasks %}
        <div class="task-item">
            <h3>Задача #{{ task.id }}</h3>
            <p>{{ task.title }}</p>
            <p>Статус: {% if task.completed %}Выполнено{% else %}В процессе{% endif %}</p>
        </div>
        {% endfor %}
    {% else %}
        <!-- Если список задач пуст, показываем сообщение -->
        <div class="empty-message">
            <h3>Список задач пуст</h3>
            <p>Добавьте свою первую задачу!</p>
        </div>
    {% endif %}
    
    <!-- Кнопка для перехода к добавлению задачи -->
    <div style="text-align: center; margin-top: 20px;">
        <a href="{% url 'add_task' %}" class="btn">Добавить задачу</a>
    </div>
</div>
{% endblock %}
```

Создаем файл `tasks/templates/add.html`:

```html
<!-- tasks/templates/add.html -->
{% extends "base.html" %}

{% block title %}{{ title }} - TASKS{% endblock %}

{% block content %}
<div class="add-task-form">
    <h2>{{ title }}</h2>
    
    <!-- Форма для добавления новой задачи -->
    <!-- method="post" указывает, что форма отправляет POST запрос -->
    <!-- В Django формы, изменяющие данные, должны использовать POST -->
    <form method="post">
        <!-- В Django все POST формы должны содержать csrf_token -->
        <!-- Это защита от межсайтовой подделки запросов -->
        {% csrf_token %}
        
        <div class="form-group">
            <label for="task_title" class="form-label">Название задачи:</label>
            <input type="text" id="task_title" name="task_title" class="form-input" 
                   placeholder="Введите название задачи" required>
        </div>
        
        <button type="submit" class="btn">Добавить задачу</button>
    </form>
    
    <!-- Ссылка для возврата к списку задач -->
    <div style="margin-top: 15px;">
        <a href="{% url 'view_tasks' %}">← Вернуться к списку задач</a>
    </div>
</div>
{% endblock %}
```

## Шаг 7: Настройка URL-маршрутов

Создаем файл `tasks/urls.py`:

```python
# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tasks, name='view_tasks'),
    path('add/', views.add_task, name='add_task'),
]
```

Обновляем главный файл URL-маршрутов `tasks_project/urls.py`:

```python
# tasks_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Подключаем URL-ы приложения tasks
]
```

## Шаг 8: Запуск приложения

```bash
# Применяем миграции (хотя у нас пока нет моделей)
python manage.py migrate

# Запускаем сервер
python manage.py runserver
```

Теперь вы можете открыть браузер и перейти по адресу `http://127.0.0.1:8000/` чтобы увидеть ваше приложение.

## Объяснение ключевых моментов:

### POST запросы в Django

В нашем приложении форма добавления задачи использует метод POST. Это важно по нескольким причинам:

1. **Безопасность**: POST запросы не кэшируются браузером и не сохраняются в истории
2. **Защита CSRF**: Django требует csrf_token для всех POST запросов
3. **Идемпотентность**: GET запросы должны быть идемпотентными (не изменять данные)

### Процесс добавления задачи:

1. Пользователь заполняет форму и нажимает "Добавить задачу"
2. Браузер отправляет POST запрос на сервер с данными формы
3. Django проверяет csrf_token и извлекает данные из request.POST
4. Если данные валидны, задача добавляется в список
5. Пользователь перенаправляется на страницу со списком задач

### Временное хранилище

Мы используем глобальную переменную `tasks_list` для хранения задач. В реальном приложении это нужно заменить на базу данных с использованием моделей Django.

Приложение готово! Теперь вы можете добавлять задачи и переключаться между светлой и темной темами.

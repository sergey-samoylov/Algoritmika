from django.shortcuts import render

# Обработчик для главной страницы
def home(request):
    # Мы просто говорим: "Верни пользователю HTML-шаблон с именем 'home.html'"
    return render(request, 'visit_card/home.html')

# Обработчик для страницы портфолио
def portfolio(request):
    # И здесь тоже: "Верни шаблон 'portfolio.html'"
    return render(request, 'visit_card/portfolio.html')

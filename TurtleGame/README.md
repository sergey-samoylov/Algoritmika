# :snake: Создаём первую игру на Python за 1 час!

Привет, будущий гейм-девелопер! 

Сегодня мы сделаем простую игру, где ты будешь управлять оранжевым шариком, убегать от красных квадратов и собирать зелёные треугольники. Поехали!

## 🔧 Подготовка

1. Открой IDLE (если нет Python - скачай с [python.org](https://python.org)) или изучай Vim и работай, как настоящий программер 😉
1. Создай новый файл: File → New File
1. Сохрани как my_game.py

## 🏗️ Шаг 1: Настраиваем игру

```Python
# Импортируем только нужные модули
from turtle import Turtle, Screen
from random import randint

# Настройки игры
SCREEN_WIDTH = 800   # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
PLAYER_SPEED = 10    # Скорость игрока
BOT_SPEED = 5        # Скорость врагов (в 2 раза медленнее игрока)
```

💡 *Совет: Эти числа можно менять чтобы сделать игру сложнее/легче!*

## 🧩 Шаг 2: Создаём главного героя

```Python
class Hero(Turtle):
    def __init__(self):
        super().__init__()  # Используем "силу" черепашки
        self.shape("circle")  # Делаем круглым
        self.color("orange")  # Оранжевый цвет
        self.penup()  # Чтобы не рисовал линию
        self.speed(0)  # Максимальная скорость анимации
        self.goto(0, -200)  # Стартовая позиция
        self.step = PLAYER_SPEED  # Скорость движения
    
    # Функции движения
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
```

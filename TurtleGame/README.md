# 🐢 Создаём игру "Черепашка vs Боты" за 1 час!

![Черепаха добралась до зелёного кристалла. Ей мешали красные боты-охранники.](img/turtle_game.png "Turtle Game")

Привет, будущий гейм-девелопер! 

Сегодня мы сделаем простую игру, где ты будешь управлять оранжевым шариком, убегать от красных квадратов и собирать зелёные треугольники. 

На самом деле:

- 🟠 -- боевая черепаха
- 🟥 -- бот-охранник
- 💚 -- магический зелёный бриллиант

Сейчас мы сделаем данную игру, где оранжевая черепашка собирает кристаллы и убегает от красных ботов.

Всё просто - повторяй за мной шаг за шагом!

Поехали!

## 🔧 Подготовка

1. Открой IDLE (если нет Python - скачай с [python.org](https://python.org)) или изучай [Vim](https://www.youtube.com/watch?v=d8XtNXutVto) и работай, как настоящий программер 😉
1. Создай новый файл: File → New File
1. Сохрани как turtle_game.py

## 🏗️ Шаг 1: Импортируем только необходимые модули

```Python
# Импортируем только нужные модули
from turtle import Turtle, Screen
from random import randint
from time import sleep
```
**Объяснение:**

- Turtle - для создания персонажей
- Screen - для создания экрана
- randint - для случайных чисел
- sleep - для паузы в игре

## Шаг 2: Определяем константы

```Python
SCREEN_WIDTH = 400       # Ширина окна
SCREEN_HEIGHT = 300      # Высота окна
PLAYER_SPEED = 10        # Скорость черепашки
BOT_SPEED = 7            # Скорость ботов
COLLISION_DISTANCE = 20  # Дистанция столкновения
WIN_SCORE = 3            # Кристаллов для победы
```

💡 *Совет: Эти числа можно менять чтобы сделать игру сложнее/легче!*

## 😵‍💫 Шаг 3: Создаём класс Sprite

```Python
class Sprite(Turtle):
    def __init__(self, x, y, step, shape, color):
        super().__init__()  # Создаем черепашку
        self.penup()       # Чтобы не рисовала линию
        self.speed(0)      # Максимальная скорость
        self.goto(x, y)    # Стартовая позиция
        self.color(color)  # Цвет
        self.shape(shape)  # Форма
        self.step = step   # Скорость
```

🦸‍♂️ Sprite -> базовый для всех персонажей - и черепашки, и ботов, и даже кристалла.

## 👾 Шаг 4: Добавляем движение

❗В **тот же класс Sprite** добавляем:

```Python
class Sprite(Turtle):
    # <Здесь инициализация класса из Шаг 3>
    def move_up(self):
        new_y = self.ycor() + self.step
        if new_y < SCREEN_HEIGHT/2 - 10:  # Проверяем границу
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - self.step
        if new_y > -SCREEN_HEIGHT/2 + 10:
            self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - self.step
        if new_x > -SCREEN_WIDTH/2 + 10:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + self.step
        if new_x < SCREEN_WIDTH/2 - 10:
            self.goto(new_x, self.ycor())
```

Теперь 🟠 черепашка сможет двигаться во все стороны! А боты и кристалл эти методы использовать не будут.

## 🤖 Шаг 5: Столкновения и движение ботов

❗Продолжаем **дописывать** в класс Sprite:

```Python
class Sprite(Turtle):
    # <Здесь инициализация класса из Шаг 3>
    # <Здесь движения черепашки из Шаг 4>
    def is_collide(self, sprite):
        return self.distance(sprite) < COLLISION_DISTANCE

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        try:
            self.forward(self.step)
            if abs(self.xcor() - self.x_end) < self.step:
                self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
        except:
            return  # Если окно закрыто - ничего не делаем
```

💥 **Важно: Враги будут ходить туда-сюда автоматически!**

## 🎯 Шаг 6: Создаём игру

Теперь пишем основной код после класса Sprite:

```Python
# Создаём экран
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Черепашка vs Боты")
screen.bgcolor("black")

# Создаём персонажей
player = Sprite(0, -100, PLAYER_SPEED, 'circle', 'orange')
enemy1 = Sprite(-SCREEN_WIDTH//2 + 20, 50, BOT_SPEED, 'square', 'red')
enemy2 = Sprite(SCREEN_WIDTH//2 - 20, -50, BOT_SPEED, 'square', 'red')
goal = Sprite(0, SCREEN_HEIGHT//2 - 30, 0, 'triangle', 'green')

# Задаём движение ботов
enemy1.set_move(-SCREEN_WIDTH//2 + 20, 50, SCREEN_WIDTH//2 - 20, 50)
enemy2.set_move(SCREEN_WIDTH//2 - 20, -50, -SCREEN_WIDTH//2 + 20, -50)

# Настраиваем управление
# СТРЕЛКИ
screen.onkey(player.move_up, "Up")      # Стрелка вверх
screen.onkey(player.move_down, "Down")  # Стрелка вниз
screen.onkey(player.move_left, "Left")  # Стрелка влево
screen.onkey(player.move_right, "Right") # Стрелка вправо
# VIM keys
screen.onkey(player.move_up, "k")    # k = вверх
screen.onkey(player.move_down, "j")  # j = вниз
screen.onkey(player.move_left, "h")  # h = влево
screen.onkey(player.move_right, "l") # l = вправо

screen.listen()  # Начинаем слушать клавиатуру

# Игровые переменные
score = 0
game_active = True
```

🍀 *Фишка: Цель будет телепортироваться при касании!*

## 🎮 Шаг 5: Настраиваем управление

```Python
def setup_controls(player, screen):
    # СТРЕЛКИ
    screen.onkey(player.move_up, "Up")      # Стрелка вверх
    screen.onkey(player.move_down, "Down")  # Стрелка вниз
    screen.onkey(player.move_left, "Left")  # Стрелка влево
    screen.onkey(player.move_right, "Right") # Стрелка вправо
    # VIM keys
    screen.onkey(player.move_up, "k")    # k = вверх
    screen.onkey(player.move_down, "j")  # j = вниз
    screen.onkey(player.move_left, "h")  # h = влево
    screen.onkey(player.move_right, "l") # l = вправо

    screen.listen()  # Начинаем слушать клавиатуру
```

⌨️ *Дополнительно: Можно добавить управление на WASD!*

## 🏁 Шаг 7: Главный игровой цикл

Добавляем в конец файла:

```Python
try:
    while game_active and score < WIN_SCORE:
        enemy1.make_step()
        enemy2.make_step()
        
        # Если собрали кристалл
        if player.is_collide(goal):
            score += 1
            enemy1.hideturtle()  # Прячем ботов
            enemy2.hideturtle()
            sleep(1)            # Пауза 1 сек
            enemy1.showturtle() # Показываем
            enemy2.showturtle()
            # Новое положение кристалла
            goal.goto(randint(-SCREEN_WIDTH//2 + 30, SCREEN_WIDTH//2 - 30), 
                     SCREEN_HEIGHT//2 - 30)
            player.goto(0, -100)  # Возвращаем черепашку
        
        # Если боты поймали
        if player.is_collide(enemy1) or player.is_collide(enemy2):
            goal.hideturtle()
            print(f"Охранные боты одолели черепашку. Она собрала {score} кристаллов.")
            game_active = False

    # Проверяем победу
    if score >= WIN_SCORE:
        print(f"Ты победил -> добрался черепашкой до кристалла {WIN_SCORE} раза!")
        enemy1.hideturtle()
        enemy2.hideturtle()

    screen.mainloop()

except:
    print("Игра завершена")
```

## 🚀 Как запустить игру

- Нажми F5 или Run → Run Module или прямо в терминале ```Bash python turtle_game.py```
- Управляй оранжевым кружком стрелками
- Собирай зелёные треугольники, избегая красных квадратов!

## 💡 Советы по улучшению

- Добавь звуки при столкновениях
- Сделай несколько уровней сложности
- Добавь бонусные предметы
- Измени цвета и формы персонажей

## 🎉 Поздравляю!

Ты только что создал свою первую игру на Python!

Теперь можешь похвастаться друзьям или улучшить игру как хочешь.

Помни - все великие программисты начинали с таких простых проектов!

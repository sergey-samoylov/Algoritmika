#!/usr/bin/env python3
"""Модуль игры 'Черепашка vs Боты'.

Игрок управляет черепашкой, собирает кристаллы
и убегает от охранных ботов.
Для победы нужно собрать 3 кристалла, избегая столкновений с ботами.
"""

from random import randint
from time import sleep
from turtle import Turtle, Screen


# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
PLAYER_SPEED = 10
BOT_SPEED = 7
COLLISION_DISTANCE = 20
WIN_SCORE = 3


class Sprite(Turtle):
    """Базовый класс для всех игровых объектов."""

    def __init__(self, x: int, y: int, step: int, shape: str, color: str) -> None:
        """Инициализирует спрайт с заданными параметрами.
        
        Args:
            x: Начальная координата по оси X.
            y: Начальная координата по оси Y.
            step: Шаг движения спрайта.
            shape: Форма спрайта.
            color: Цвет спрайта.
        """
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_up(self) -> None:
        """Перемещает спрайт вверх с проверкой границ экрана."""
        new_y = self.ycor() + self.step
        if new_y < SCREEN_HEIGHT / 2 - 10:
            self.goto(self.xcor(), new_y)

    def move_down(self) -> None:
        """Перемещает спрайт вниз с проверкой границ экрана."""
        new_y = self.ycor() - self.step
        if new_y > -SCREEN_HEIGHT / 2 + 10:
            self.goto(self.xcor(), new_y)

    def move_left(self) -> None:
        """Перемещает спрайт влево с проверкой границ экрана."""
        new_x = self.xcor() - self.step
        if new_x > -SCREEN_WIDTH / 2 + 10:
            self.goto(new_x, self.ycor())

    def move_right(self) -> None:
        """Перемещает спрайт вправо с проверкой границ экрана."""
        new_x = self.xcor() + self.step
        if new_x < SCREEN_WIDTH / 2 - 10:
            self.goto(new_x, self.ycor())

    def is_collide(self, sprite: Turtle) -> bool:
        """Проверяет столкновение с другим спрайтом.
        
        Args:
            sprite: Другой спрайт для проверки столкновения.
            
        Returns:
            True если расстояние между спрайтами меньше COLLISION_DISTANCE.
        """
        return self.distance(sprite) < COLLISION_DISTANCE

    def set_move(self, x_start: int, y_start: int, 
                x_end: int, y_end: int) -> None:
        """Устанавливает маршрут движения между двумя точками.
        
        Args:
            x_start: Начальная координата X.
            y_start: Начальная координата Y.
            x_end: Конечная координата X.
            y_end: Конечная координата Y.
        """
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self) -> None:
        """Выполняет один шаг движения по заданному маршруту."""
        try:
            self.forward(self.step)
            if abs(self.xcor() - self.x_end) < self.step:
                self.set_move(self.x_end, self.y_end, 
                             self.x_start, self.y_start)
        except:
            return


def main() -> None:
    """Основная функция игры, содержащая инициализацию и игровой цикл."""
    # Создаем экран
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Черепашка vs Боты")
    screen.bgcolor("black")

    # Создаем персонажей
    player = Sprite(0, -100, PLAYER_SPEED, 'circle', 'orange')
    enemy1 = Sprite(-SCREEN_WIDTH // 2 + 20, 50, BOT_SPEED, 'square', 'red')
    enemy2 = Sprite(SCREEN_WIDTH // 2 - 20, -50, BOT_SPEED, 'square', 'red')
    goal = Sprite(0, SCREEN_HEIGHT // 2 - 30, 0, 'triangle', 'green')

    # Настраиваем движение ботов
    enemy1.set_move(-SCREEN_WIDTH // 2 + 20, 50, 
                   SCREEN_WIDTH // 2 - 20, 50)
    enemy2.set_move(SCREEN_WIDTH // 2 - 20, -50, 
                   -SCREEN_WIDTH // 2 + 20, -50)

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

    # Игровой цикл
    score = 0
    game_active = True

    try:
        while game_active and score < WIN_SCORE:
            enemy1.make_step()
            enemy2.make_step()
            
            if player.is_collide(goal):
                score += 1
                enemy1.hideturtle()
                enemy2.hideturtle()
                sleep(1)
                enemy1.showturtle()
                enemy2.showturtle()
                goal.goto(randint(-SCREEN_WIDTH // 2 + 30, 
                           SCREEN_WIDTH // 2 - 30),
                         SCREEN_HEIGHT // 2 - 30)
                player.goto(0, -100)
            
            if player.is_collide(enemy1) or player.is_collide(enemy2):
                goal.hideturtle()
                print(f"Охранные боты одолели черепашку. "
                      f"Собрано кристаллов - {score}.")
                game_active = False

        if score >= WIN_SCORE:
            print("Ты победил -> 3 раза добрался черепашкой до кристалла!")
            enemy1.hideturtle()
            enemy2.hideturtle()

        screen.mainloop()

    except:
        print("Игра завершена")


if __name__ == "__main__":
    main()

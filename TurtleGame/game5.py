#!/usr/bin/env python3

# Стандартные модули
from random import randint
from turtle import Screen, Turtle


# Константы игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 10
BOT_SPEED = 5
BOT_MIN_Y = -150
BOT_MAX_Y = 150


class Hero(Turtle):
    """Класс игрока, управляемого пользователем.

    Наследует функциональность от класса Turtle для отрисовки и управления.
    """

    def __init__(self) -> None:
        """Инициализирует героя с базовыми параметрами."""
        # super() вызывает конструктор родительского класса (Turtle)
        # Это необходимо для правильной инициализации объекта как черепашки
        # Если просто использовать def __init__(self), мы потеряем всю функциональность Turtle
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.speed(0)
        self.reset_position()
        self.step: int = PLAYER_SPEED

    def reset_position(self) -> None:
        """Сбрасывает позицию игрока в начальное положение ниже ботов."""
        self.goto(0, -250)

    def move_up(self) -> None:
        """Перемещает игрока вверх с проверкой границ экрана."""
        new_y = self.ycor() + self.step
        if new_y < SCREEN_HEIGHT / 2 - 20:
            self.goto(self.xcor(), new_y)

    def move_down(self) -> None:
        """Перемещает игрока вниз с проверкой границ экрана."""
        new_y = self.ycor() - self.step
        if new_y > -SCREEN_HEIGHT / 2 + 20:
            self.goto(self.xcor(), new_y)

    def move_left(self) -> None:
        """Перемещает игрока влево с проверкой границ экрана."""
        new_x = self.xcor() - self.step
        if new_x > -SCREEN_WIDTH / 2 + 20:
            self.goto(new_x, self.ycor())

    def move_right(self) -> None:
        """Перемещает игрока вправо с проверкой границ экрана."""
        new_x = self.xcor() + self.step
        if new_x < SCREEN_WIDTH / 2 - 20:
            self.goto(new_x, self.ycor())


class Enemy(Turtle):
    """Класс врага, двигающегося автоматически по горизонтали.

    Наследует функциональность от класса Turtle.
    """

    def __init__(self, x: int, y: int) -> None:
        """Инициализирует врага с начальными параметрами движения.

        Args:
            x: Начальная координата X
            y: Начальная координата Y (определяет уровень движения)
        """
        super().__init__()  # Инициализация Turtle
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.step: int = BOT_SPEED
        self.x_start: int = x
        self.y_start: int = y
        self.x_end: int = -x
        self.y_end: int = y
        self.goto(x, y)
        self.setheading(self.towards(self.x_end, self.y_end))

    def move(self) -> None:
        """Обновляет позицию врага, разворачивая его у границ экрана."""
        self.forward(self.step)

        # Проверка достижения конечной точки с небольшим допуском
        if (abs(self.xcor() - self.x_end) < self.step and
                abs(self.ycor() - self.y_end) < self.step):
            # Меняем направление движения на противоположное
            self.x_start, self.x_end = self.x_end, self.x_start
            self.y_start, self.y_end = self.y_end, self.y_start
            self.setheading(self.towards(self.x_end, self.y_end))


class Target(Turtle):
    """Класс цели, которую должен собрать игрок."""

    def __init__(self) -> None:
        """Инициализирует цель со случайной начальной позицией."""
        super().__init__()
        self.shape("triangle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.new_position()

    def new_position(self) -> None:
        """Устанавливает новую случайную позицию для цели."""
        x = randint(-SCREEN_WIDTH // 2 + 50, SCREEN_WIDTH // 2 - 50)
        y = randint(100, SCREEN_HEIGHT // 2 - 50)
        self.goto(x, y)


def setup_controls(player: Hero, screen: Screen) -> None:
    """Настраивает управление для игрока.

    Args:
        player: Объект игрока
        screen: Экран игры
    """
    # Управление стрелками
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")
    # Управление Vim-стиль (hjkl)
    screen.onkey(player.move_up, "k")
    screen.onkey(player.move_down, "j")
    screen.onkey(player.move_left, "h")
    screen.onkey(player.move_right, "l")
    screen.listen()


def main() -> None:
    """Основная функция игры, содержащая игровой цикл."""
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Моя первая игра!")
    screen.bgcolor("black")

    player = Hero()
    target = Target()

    # Создаем ботов на разных уровнях
    y1 = randint(BOT_MIN_Y, BOT_MAX_Y)
    y2 = randint(BOT_MIN_Y, BOT_MAX_Y)
    # Гарантируем достаточное расстояние между ботами
    while abs(y1 - y2) < 50:
        y2 = randint(BOT_MIN_Y, BOT_MAX_Y)

    enemy1 = Enemy(-SCREEN_WIDTH // 2 + 20, y1)
    enemy2 = Enemy(SCREEN_WIDTH // 2 - 20, y2)

    setup_controls(player, screen)

    score: int = 0
    game_over: bool = False

    while not game_over:
        enemy1.move()
        enemy2.move()

        if player.distance(target) < 20:
            score += 1
            target.new_position()
            player.reset_position()
            print(f"Счёт: {score}")

        if (player.distance(enemy1) < 20 or
                player.distance(enemy2) < 20):
            print("Игра окончена! Твой счёт:", score)
            game_over = True

    screen.mainloop()


if __name__ == "__main__":
    main()

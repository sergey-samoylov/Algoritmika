## 🎮 Учебное пособие: создаём игру Arkanoid (Breakout)

🧑‍💻 Уровень: начинающий
🧱 Частей: 3
📦 Библиотека: `pygame`
🔁 Цель: сделать свою версию классической игры Arkanoid

---

## 🔹 ШАГ 1: Окно и движущаяся платформа

📌 Цель:

* Открыть окно
* Отобразить фон
* Создать движущуюся платформу

### 🔨 Что нужно:

1. Установить `pygame`, если он ещё не установлен:

```bash
pip install pygame
```

2. Код `step1.py`:

```python
import pygame

pygame.init()

# Константы
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (200, 255, 255)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 30
PLATFORM_SPEED = 5
FPS = 40

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid — шаг 1")
clock = pygame.time.Clock()

# Загрузка платформы
platform = pygame.Rect(200, 330, PLATFORM_WIDTH, PLATFORM_HEIGHT)
move_right = False
move_left = False

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.x += PLATFORM_SPEED
    if move_left:
        platform.x -= PLATFORM_SPEED

    pygame.draw.rect(screen, (100, 100, 255), platform)
    pygame.display.update()
    clock.tick(FPS)
```

✅ **После этого шага** вы увидите окно с движущейся платформой.

---

## 🔹 ШАГ 2: Добавляем мяч и отражения

📌 Цель:

* Добавить мяч
* Заставить его двигаться
* Реализовать отскоки от стен и платформы

### 🧩 Код `step2.py`:

```python
import pygame

pygame.init()

# Константы
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (200, 255, 255)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 30
PLATFORM_SPEED = 5
BALL_SIZE = 20
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
FPS = 40

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid — шаг 2")
clock = pygame.time.Clock()

# Объекты
platform = pygame.Rect(200, 330, PLATFORM_WIDTH, PLATFORM_HEIGHT)
ball = pygame.Rect(240, 200, BALL_SIZE, BALL_SIZE)
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

move_right = False
move_left = False

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.x += PLATFORM_SPEED
    if move_left:
        platform.x -= PLATFORM_SPEED

    ball.x += ball_dx
    ball.y += ball_dy

    # Отскоки от стен
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1

    # Отскок от платформы
    if ball.colliderect(platform):
        ball_dy *= -1

    pygame.draw.rect(screen, (100, 100, 255), platform)
    pygame.draw.ellipse(screen, (255, 50, 50), ball)

    pygame.display.update()
    clock.tick(FPS)
```

✅ **После этого шага** мяч будет двигаться и отскакивать от платформы и стен.

---

## 🔹 ШАГ 3: Монстры и завершение игры

📌 Цель:

* Добавить монстров
* Проверять столкновения мяча с монстрами
* Завершать игру при победе или поражении

### 🧠 Итоговый код `arkanoid_final.py`

Используется финальный улучшенный код (как мы исправили ранее), с:

* Классами `Area`, `Picture`, `Label`
* Константами
* Докстрингами
* Функцией `show_message()`

📁 Этот код у нас уже есть - arkanoid_final.py

✅ **После этого шага** игра будет полной:

* Мяч уничтожает монстров
* Победа, если все исчезли
* Поражение, если мяч упал ниже платформы

---

## 🏁 Поздравляем!

Теперь у вас есть полноценная аркадная игра! Вы можете:

* Добавить счёт
* Сделать уровни
* Подключить звуки
* Сохранить результаты


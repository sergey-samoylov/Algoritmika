# Урок программирования: Создание 2D-игры на Python с PyGame

## Тема: "Разработка платформера с анимацией и взаимодействием объектов"

**Цель урока:** Понять основы создания 2D-игр на Python с использованием библиотеки PyGame, изучив работу с графикой, анимацией, обработкой событий и игровой логикой.

### 1. Введение в игровой движок

Давайте разберемся, как работает наша игра:

```python
import pygame
import sys
from random import randint

# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра")
```

**Объяснение:**
- `pygame.init()` - инициализирует все модули Pygame
- Мы создаем окно размером 800x600 пикселей
- `set_caption()` устанавливает заголовок окна

### 2. Главное меню игры

Функция `start_screen()` создает интерфейс главного меню:

```python
def start_screen():
    start = pygame.transform.scale(
        pygame.image.load('start.png'), 
        (200, 70)
    )
    start_rect = start.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    )
    screen.blit(start, start_rect)
```

**Задание:** Попробуй изменить позиции кнопок или их размеры. Что произойдет?

### 3. Классы игровых объектов

#### Базовый класс GameSprite:

```python
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(picture), 
            (100, 120)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
```

**Объяснение:**
- Все игровые объекты наследуются от `pygame.sprite.Sprite`
- `self.rect` - прямоугольник, определяющий позицию и размеры спрайта
- `pygame.transform.scale()` изменяет размер изображения

#### Класс Player с анимацией:

```python
class Player(GameSprite):
    def __init__(self, picture, x, y, speed):
        super().__init__(picture, x, y)
        self.speed = speed
        self.pick_ind = 0
        self.rotation = 0
        self.animation_lose = False
```

**Система анимации:**
- `rotation` определяет состояние персонажа:
  - 0 - стоит вправо
  - 1 - стоит влево  
  - 2 - бежит вправо
  - 3 - бежит влево
  - 4 - атака
  - 5 - смерть

**Практическое задание:** Добавь новое состояние анимации - "прыжок"

### 4. Игровая логика и взаимодействия

#### Движение игрока:

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    hero.update_rotation(2)  # Бежит вправо
elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
    hero.update_rotation(0)  # Стоит вправо
```

**Механика камеры:**

```python
camera.x = hero.rect.x - SCREEN_WIDTH // 2
camera.x = max(0, min(camera.x, bg_width - SCREEN_WIDTH))
```

Камера следует за игроком, но не выходит за границы уровня.

### 5. Система столкновений и победы

```python
# Проверка столкновения с врагом
if pygame.sprite.collide_rect(hero, enemy):
    screen.blit(win, (400, 300))
    # Возврат в главное меню после победы
```

**Задание:** Добавь счетчик очков, который увеличивается при победе над врагом.

### 6. Практические задания

#### Задание 1: Добавь звуковые эффекты
Добавь звук при атаке и при получении урона:

```python
attack_sound = pygame.mixer.Sound('attack.wav')
hurt_sound = pygame.mixer.Sound('hurt.wav')
```

#### Задание 2: Создай систему здоровья
Добавь отображение здоровья игрока:

```python
class Player(GameSprite):
    def __init__(self, picture, x, y, speed):
        super().__init__(picture, x, y)
        self.health = 100
```

#### Задание 3: Добавь несколько врагов
Создай группу врагов вместо одного:

```python
enemies = pygame.sprite.Group()
for i in range(5):
    enemy = Enemy('Images/Enemy/enemy.png', 600 + i*200, 390)
    enemies.add(enemy)
```

### 7. Советы по улучшению игры

1. **Оптимизация:** Загружай изображения один раз при запуске
2. **Модульность:** Раздели код на разные файлы (player.py, enemy.py, etc.)
3. **Расширяемость:** Сделай настройки игры в отдельном config.py

### 8. Домашнее задание

1. Добавь сбор монет с увеличением счета
2. Создай несколько уровней с разными фонами
3. Реализуй систему сохранения лучшего результата

### Заключение

Сегодня мы изучили:
- Основы PyGame и создание игрового окна
- Работу со спрайтами и анимацией
- Обработку пользовательского ввода
- Систему столкновений и игровую логику
- Создание игрового интерфейса

**Для дальнейшего изучения:**
- Официальная документация PyGame
- Книга "Making Games with Python & Pygame"

Удачи в создании собственных игр! 🎮

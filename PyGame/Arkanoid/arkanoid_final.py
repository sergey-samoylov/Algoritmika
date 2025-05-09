import pygame

pygame.init()

# 🎨 Цвета
BACKGROUND_COLOR = (200, 255, 255)
TEXT_COLOR = (0, 0, 0)
WIN_COLOR = (0, 200, 0)
LOSE_COLOR = (255, 0, 0)

# 🖼️ Размеры экрана
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# 🕹️ Платформа
PLATFORM_START_X = 200
PLATFORM_START_Y = 330
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 30
PLATFORM_SPEED = 5

# ⚽ Мяч
BALL_START_X = 160
BALL_START_Y = 200
BALL_WIDTH = 50
BALL_HEIGHT = 50
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# 👾 Монстры
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_ROWS = 3
ENEMY_COUNT_ROW1 = 9
ENEMY_START_X = 5
ENEMY_START_Y = 5
ENEMY_SPACING_X = 55
ENEMY_SPACING_Y = 55

# 📝 Сообщение победы/поражения
MESSAGE_X = 150
MESSAGE_Y = 150
MESSAGE_WIDTH = 50
MESSAGE_HEIGHT = 50
FONT_SIZE = 60
WIN_TEXT = "YOU WIN"
LOSE_TEXT = "YOU LOSE"

# 🕒 FPS
FPS = 40

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
clock = pygame.time.Clock()

# Состояния движения платформы
move_right = False
move_left = False
game_over = False


class Area:
    """Прямоугольная область на экране."""

    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """Создаёт прямоугольник с цветом."""
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = BACKGROUND_COLOR if color is None else color

    def color(self, new_color):
        """Изменяет цвет заливки."""
        self.fill_color = new_color

    def fill(self):
        """Рисует залитый прямоугольник."""
        pygame.draw.rect(screen, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        """Проверяет попадание точки внутрь прямоугольника."""
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        """Проверяет пересечение с другим прямоугольником."""
        return self.rect.colliderect(rect)


class Label(Area):
    """Область с текстом."""

    def set_text(self, text, fsize=12, text_color=TEXT_COLOR):
        """Создаёт текст для отображения."""
        self.image = pygame.font.SysFont(
            None, fsize
        ).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        """Рисует фон и поверх него текст."""
        self.fill()
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    """Область с изображением."""

    def __init__(self, filename, x=0, y=0, width=10, height=10):
        """Создаёт объект с изображением."""
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        """Отрисовывает изображение на экране."""
        screen.blit(self.image, (self.rect.x, self.rect.y))


def show_message(text, color):
    """Показывает сообщение (победа или поражение) и завершает игру."""
    global game_over
    message = Label(
        MESSAGE_X, MESSAGE_Y, MESSAGE_WIDTH, MESSAGE_HEIGHT, BACKGROUND_COLOR
    )
    message.set_text(text, FONT_SIZE, color)
    message.draw(10, 10)
    game_over = True


# Создание игровых объектов
ball = Picture(
    'ball.png', BALL_START_X, BALL_START_Y, BALL_WIDTH, BALL_HEIGHT
)
platform = Picture(
    'platform.png', PLATFORM_START_X, PLATFORM_START_Y,
    PLATFORM_WIDTH, PLATFORM_HEIGHT
)

# Генерация врагов
monsters = []
count = ENEMY_COUNT_ROW1
for row in range(ENEMY_ROWS):
    y = ENEMY_START_Y + (ENEMY_SPACING_Y * row)
    x = ENEMY_START_X + (27.5 * row)
    for _ in range(count):
        enemy = Picture(
            'enemy.png', x, y, ENEMY_WIDTH, ENEMY_HEIGHT
        )
        monsters.append(enemy)
        x += ENEMY_SPACING_X
    count -= 1

# Игровой цикл
while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
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
        platform.rect.x += PLATFORM_SPEED
    if move_left:
        platform.rect.x -= PLATFORM_SPEED

    ball.rect.x += BALL_SPEED_X
    ball.rect.y += BALL_SPEED_Y

    if ball.rect.y < 0:
        BALL_SPEED_Y *= -1
    if ball.rect.x < 0 or ball.rect.x > SCREEN_WIDTH - BALL_WIDTH:
        BALL_SPEED_X *= -1

    if ball.rect.colliderect(platform.rect):
        BALL_SPEED_Y *= -1

    for enemy in monsters[:]:
        enemy.draw()
        if enemy.rect.colliderect(ball.rect):
            monsters.remove(enemy)
            enemy.fill()
            BALL_SPEED_Y *= -1

    if ball.rect.y > SCREEN_HEIGHT - 150:
        show_message(LOSE_TEXT, LOSE_COLOR)

    if not monsters:
        show_message(WIN_TEXT, WIN_COLOR)

    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(FPS)


import pygame
import sys
from random import randint


# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def start_screen():
    """
    Функция отображения стартового экрана.
    
    Returns:
        tuple: Кортеж с прямоугольниками кнопок старта и выхода
    """
    # Загрузка и масштабирование изображения кнопки старта
    start_img = pygame.transform.scale(
        pygame.image.load('start.png'), 
        (200, 70)
    )
    start_rect = start_img.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    )
    screen.blit(start_img, start_rect)

    # Загрузка и масштабирование изображения кнопки выхода
    exit_img = pygame.transform.scale(
        pygame.image.load('exit.png'), 
        (200, 70)
    )
    exit_rect = exit_img.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    )
    screen.blit(exit_img, exit_rect)
    
    return start_rect, exit_rect


class GameSprite(pygame.sprite.Sprite):
    """Базовый класс для игровых спрайтов."""
    
    def __init__(self, image_path, x, y):
        """
        Инициализация спрайта.
        
        Args:
            image_path (str): Путь к изображению спрайта
            x (int): Координата X
            y (int): Координата Y
        """
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), 
            (100, 120)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, camera):
        """
        Отрисовка спрайта с учетом камеры.
        
        Args:
            camera (pygame.Rect): Область видимости камеры
        """
        screen.blit(
            self.image, 
            (self.rect.x - camera.x, self.rect.y - camera.y)
        )


class Player(GameSprite):
    """Класс игрока."""
    
    # Константы для анимации
    FACING_RIGHT = 0
    FACING_LEFT = 1
    MOVING_RIGHT = 2
    MOVING_LEFT = 3
    ATTACKING = 4
    
    def __init__(self, image_path, x, y, speed):
        """
        Инициализация игрока.
        
        Args:
            image_path (str): Путь к изображению
            x (int): Координата X
            y (int): Координата Y
            speed (int): Скорость движения
        """
        super().__init__(image_path, x, y)
        self.speed = speed
        self.frame_index = 0
        self.rotation = self.FACING_RIGHT
        self._load_animations()

    def _load_animations(self):
        """Загрузка всех анимаций для персонажа."""
        path = 'Images/Warrior/'
        
        # Анимация покоя
        self.idle_right = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'), 
                (100, 120)
            ).convert_alpha() 
            for i in range(1, 11)
        ]
        self.idle_left = [
            pygame.transform.flip(frame, True, False) 
            for frame in self.idle_right
        ]
        
        # Анимация движения
        self.move_right = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'), 
                (100, 120)
            ).convert_alpha() 
            for i in range(11, 19)
        ]
        self.move_left = [
            pygame.transform.flip(frame, True, False) 
            for frame in self.move_right
        ]
        
        # Анимация атаки
        self.attack_frames = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'), 
                (100, 120)
            ).convert_alpha() 
            for i in range(41, 48)
        ]

    def animate(self, bg_width):
        """
        Обновление анимации и положения игрока.
        
        Args:
            bg_width (int): Ширина фонового изображения
        """
        # Выбор текущего кадра анимации в зависимости от состояния
        if self.rotation == self.FACING_RIGHT:
            self.image = self.idle_right[self.frame_index // 6]
        elif self.rotation == self.FACING_LEFT:
            self.image = self.idle_left[self.frame_index // 6]
        elif self.rotation == self.MOVING_RIGHT:
            self.image = self.move_right[self.frame_index // 7]
            self.rect.x += self.speed
        elif self.rotation == self.MOVING_LEFT:
            self.image = self.move_left[self.frame_index // 7]
            self.rect.x -= self.speed
        elif self.rotation == self.ATTACKING:
            self.image = self.attack_frames[self.frame_index // 4]

        # Ограничение движения в пределах игровой области
        if self.rect.x > bg_width - 100:
            self.rotation = self.FACING_RIGHT
        if self.rect.x < 0:
            self.rotation = self.FACING_LEFT

        # Обновление индекса кадра анимации
        if self.rotation == self.ATTACKING:
            self.frame_index = (self.frame_index + 1) % 25
        else:
            self.frame_index = (self.frame_index + 1) % 55

    def update_rotation(self, new_rotation):
        """
        Обновление состояния анимации игрока.
        
        Args:
            new_rotation (int): Новое состояние анимации
        """
        if new_rotation != self.rotation:
            self.rotation = new_rotation
            self.frame_index = 0


class Enemy(GameSprite):
    """Класс врага."""
    
    def update(self):
        """Обновление положения врага."""
        if self.rect.x < 7500:
            self.rect.x += 5

    def fire(self):
        """Создание пули, выпущенной врагом."""
        bullet = Bullet(
            'Images/Enemy/bullet.png', 
            self.rect.left, 
            self.rect.centery, 
            randint(4, 7), 
            40, 
            20
        )
        bullets.add(bullet)


class Bullet(GameSprite):
    """Класс пули."""
    
    def __init__(self, image_path, x, y, speed, width, height):
        """
        Инициализация пули.
        
        Args:
            image_path (str): Путь к изображению
            x (int): Координата X
            y (int): Координата Y
            speed (int): Скорость движения
            width (int): Ширина пули
            height (int): Высота пули
        """
        super().__init__(image_path, x, y)
        self.speed = speed
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), 
            (width, height)
        )

    def update(self, player):
        """
        Обновление положения пули.
        
        Args:
            player (Player): Объект игрока для определения направления
        """
        # Движение пули с учетом направления игрока
        if player.rotation == Player.MOVING_RIGHT:
            self.rect.x -= self.speed + player.speed
        else:
            self.rect.x -= self.speed


# Загрузка и масштабирование фоновых изображений
bg_menu = pygame.transform.scale(
    pygame.image.load('bg_menu.jpg'), 
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
bg = pygame.transform.scale(
    pygame.image.load('bg.jpg'), 
    (8000, SCREEN_HEIGHT)
)
bg_width, bg_height = bg.get_size()

# Загрузка звуков
menu_music = pygame.mixer.Sound('menu_music.mp3')
menu_music.play(-1)
game_music = pygame.mixer.Sound('game_music.mp3')

# Создание игровых объектов
hero = Player('Images/Warrior/1.png', 300, 380, 3)
enemy = Enemy('Images/Enemy/enemy.png', 600, 390)
bullets = pygame.sprite.Group()

# Инициализация камеры
camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# Таймер для выстрелов врага
pygame.time.set_timer(pygame.USEREVENT, 3000)

# Флаги состояний игры
main_menu = True
running = True
finish = False
game_start = False

# Получение прямоугольников кнопок стартового экрана
start_rect, exit_rect = start_screen()

# Главный игровой цикл
while running:
    if not finish:
        if main_menu:
            # Отрисовка главного меню
            screen.blit(bg_menu, (0, 0))
            start_rect, exit_rect = start_screen()

            # Обработка событий в меню
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if start_rect.collidepoint(x, y):
                        game_start = True
                        main_menu = False
                        menu_music.stop()
                        game_music.play(-1)
                    elif exit_rect.collidepoint(x, y):
                        pygame.quit()
                        sys.exit()
                        
        if game_start:
            # Обработка событий в игре
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    enemy.fire()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        hero.update_rotation(Player.FACING_RIGHT)
                    elif event.key == pygame.K_LEFT:
                        hero.update_rotation(Player.FACING_LEFT)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        hero.update_rotation(Player.MOVING_RIGHT)
                    elif event.key == pygame.K_LEFT:
                        hero.update_rotation(Player.MOVING_LEFT)
                    elif event.key == pygame.K_SPACE:
                        hero.update_rotation(Player.ATTACKING)

            # Обновление позиции камеры
            camera.x = hero.rect.x - SCREEN_WIDTH // 2
            camera.y = hero.rect.y - SCREEN_HEIGHT // 2
            camera.x = max(0, min(camera.x, bg_width - SCREEN_WIDTH))
            camera.y = max(0, min(camera.y, bg_height - SCREEN_HEIGHT))
            
            # Отрисовка фона
            screen.blit(bg, (-camera.x, -camera.y))
           
            # Отрисовка пуль
            for bullet in bullets:
                screen.blit(
                    bullet.image, 
                    (bullet.rect.x - camera.x, bullet.rect.y - camera.y)
                )

            # Обновление и отрисовка игровых объектов
            hero.draw(camera)
            hero.animate(bg_width)
            enemy.draw(camera)
            enemy.update()
            bullets.update(hero)

    # Обновление экрана и задержка для контроля FPS
    pygame.display.flip()
    pygame.time.delay(20)

# Завершение работы Pygame
pygame.quit()
sys.exit()

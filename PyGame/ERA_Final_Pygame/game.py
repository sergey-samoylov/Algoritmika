import pygame
import sys
from random import randint


# Инициализация Pygame
pygame.init()


# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра")  # Добавлено название окна


def start_screen():
    """
    Отображает стартовый экран с кнопками начала игры и выхода.

    Returns:
        tuple: Кортеж с прямоугольниками кнопок (start_rect, stop_rect)
    """
    # Загрузка и масштабирование изображения кнопки "Старт"
    start = pygame.transform.scale(
        pygame.image.load('start.png'),
        (200, 70)
    )
    start_rect = start.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    )
    screen.blit(start, start_rect)

    # Загрузка и масштабирование изображения кнопки "Выход"
    stop = pygame.transform.scale(
        pygame.image.load('exit.png'),
        (200, 70)
    )
    stop_rect = stop.get_rect(  # Исправлено: было start.get_rect()
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    )
    screen.blit(stop, stop_rect)

    return start_rect, stop_rect


# Получаем прямоугольники кнопок стартового экрана
start_rect, stop_rect = start_screen()


class GameSprite(pygame.sprite.Sprite):
    """Базовый класс для игровых спрайтов."""

    def __init__(self, picture, x, y):
        """
        Инициализация спрайта.

        Args:
            picture (str): Путь к изображению спрайта
            x (int): Координата X
            y (int): Координата Y
        """
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(picture),
            (100, 120)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        """Отрисовка спрайта с учетом позиции камеры."""
        screen.blit(
            self.image,
            (self.rect.x - camera.x, self.rect.y - camera.y)
        )


class Player(GameSprite):
    """Класс игрока, наследуется от GameSprite."""

    def __init__(self, picture, x, y, speed):
        """
        Инициализация игрока.

        Args:
            picture (str): Путь к изображению
            x (int): Координата X
            y (int): Координата Y
            speed (int): Скорость движения
        """
        super().__init__(picture, x, y)
        self.speed = speed
        self.pick_ind = 0  # Индекс текущего кадра анимации

        # Состояния анимации:
        # 0 - стоит вправо, 1 - стоит влево
        # 2 - бежит вправо, 3 - бежит влево
        # 4 - атака, 5 - смерть
        self.rotation = 0
        self.animation_lose = False  # Флаг завершения анимации смерти

    def animate(self, path='Images/Warrior/'):
        """
        Анимация игрока в зависимости от текущего состояния.

        Args:
            path (str): Путь к папке с изображениями анимации
        """
        # Загрузка анимаций
        self.stay_right = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'),
                (100, 120)
            ).convert_alpha() for i in range(1, 11)
        ]
        self.stay_left = [
            pygame.transform.flip(picture, True, False)
            for picture in self.stay_right
        ]
        self.move_right = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'),
                (100, 120)
            ).convert_alpha() for i in range(11, 19)
        ]
        self.move_left = [
            pygame.transform.flip(picture, True, False)
            for picture in self.move_right
        ]
        self.atk = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'),
                (100, 120)
            ).convert_alpha() for i in range(41, 48)
        ]
        self.death = [
            pygame.transform.scale(
                pygame.image.load(f'{path}{i}.png'),
                (100, 120)
            ).convert_alpha() for i in range(61, 68)
        ]

        # Обработка различных состояний анимации
        if self.rotation == 0:  # Стоит вправо
            self.image = self.stay_right[self.pick_ind // 6]
        elif self.rotation == 1:  # Стоит влево
            self.image = self.stay_left[self.pick_ind // 6]
        elif self.rotation == 2:  # Бежит вправо
            self.image = self.move_right[self.pick_ind // 7]
            self.rect.x += self.speed
        elif self.rotation == 3:  # Бежит влево
            self.image = self.move_left[self.pick_ind // 7]
            self.rect.x -= self.speed
        elif self.rotation == 4:  # Атака
            self.image = self.atk[self.pick_ind // 4]
        elif self.rotation == 5:  # Смерть
            self.image = self.death[self.pick_ind // 6]

        # Ограничение движения в пределах карты
        if self.rect.x > bg_width - 100:
            self.rotation = 0
        if self.rect.x < 0:
            self.rotation = 1

        # Обновление индекса анимации
        if self.rotation == 4:  # Атака
            self.pick_ind = (self.pick_ind + 1) % 25
        else:
            self.pick_ind = (self.pick_ind + 1) % 55

        # Проверка завершения анимации смерти
        if self.rotation == 5 and self.pick_ind == 36:
            self.animation_lose = True

    def update_rotation(self, new_rotation):
        """
        Обновление состояния анимации игрока.

        Args:
            new_rotation (int): Новое состояние анимации
        """
        if new_rotation != self.rotation:
            self.rotation = new_rotation
            self.pick_ind = 0  # Сброс анимации при изменении состояния


class Enemy(GameSprite):
    """Класс врага, наследуется от GameSprite."""

    def update(self):
        """Обновление позиции врага."""
        if self.rect.x < 7500:
            self.rect.x += 5

    def fire(self):
        """Создание пули врага."""
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
    """Класс пули, наследуется от GameSprite."""

    def __init__(self, picture, x, y, speed, width, height):
        """
        Инициализация пули.

        Args:
            picture (str): Путь к изображению
            x (int): Координата X
            y (int): Координата Y
            speed (int): Скорость движения
            width (int): Ширина пули
            height (int): Высота пули
        """
        super().__init__(picture, x, y)
        self.speed = speed
        self.image = pygame.transform.scale(
            pygame.image.load(picture),
            (width, height)
        )

    def update(self):
        """Обновление позиции пули."""
        if hero.rotation == 2:  # Если игрок бежит вправо
            self.rect.x -= self.speed + hero.speed
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

# Создание текста победы
win = pygame.font.SysFont('Arial', 70).render("ПОБЕДА", True, (0, 255, 0))

# Камера для отслеживания позиции игрока
camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# Таймер для выстрелов врага
pygame.time.set_timer(pygame.USEREVENT, 3000)

# Флаги состояний игры
main_menu = True
running = True
finish = False
game_start = False

# Главный игровой цикл
while running:
    if not finish:
        if main_menu:
            # Отображение главного меню
            screen.blit(bg_menu, (0, 0))
            start_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if start_rect.collidepoint(x, y):
                        # Начало игры
                        game_start = True
                        main_menu = False
                        menu_music.stop()
                        game_music.play(-1)
                    elif stop_rect.collidepoint(x, y):
                        # Выход из игры
                        pygame.quit()
                        sys.exit()

        if game_start:
            # Обработка событий во время игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    enemy.fire()  # Враг стреляет

                # Обработка управления игроком
                if hero.rotation != 5:  # Если игрок не умер
                    if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                        hero.update_rotation(0)  # Стоит вправо
                    elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                        hero.update_rotation(1)  # Стоит влево
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        hero.update_rotation(2)  # Бежит вправо
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        hero.update_rotation(3)  # Бежит влево
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        hero.update_rotation(4)  # Атака

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
            hero.draw()
            hero.animate()
            enemy.draw()
            enemy.update()
            bullets.update()

            # Проверка условий победы/проигрыша
            if hero.rotation == 4:  # Если игрок атакует
                # Уничтожение пуль при атаке
                pygame.sprite.spritecollide(hero, bullets, True)

                # Проверка столкновения с врагом
                if pygame.sprite.collide_rect(hero, enemy):
                    screen.blit(win, (400, 300))
                    pygame.display.flip()
                    pygame.time.delay(2000)  # Задержка перед возвратом в меню

                    # Сброс игры
                    game_start = False
                    main_menu = True
                    for b in bullets:
                        b.kill()
                    hero.rotation = 0
                    hero.rect.x = 300
                    hero.rect.y = 380
                    enemy.rect.x = 600
                    enemy.rect.y = 390
                    menu_music.play(-1)
                    game_music.stop()
            else:
                # Проверка попадания пули в игрока
                if pygame.sprite.spritecollide(hero, bullets, False):
                    hero.update_rotation(5)  # Анимация смерти

            # Обработка завершения анимации смерти
            if hero.animation_lose:
                game_start = False
                main_menu = True
                hero.animation_lose = False

                # Сброс игры
                for b in bullets:
                    b.kill()
                hero.rotation = 0
                hero.rect.x = 300
                hero.rect.y = 380
                enemy.rect.x = 600
                enemy.rect.y = 390
                menu_music.play(-1)
                game_music.stop()

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(20)

# Завершение работы
pygame.quit()
sys.exit()

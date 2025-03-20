#!/usr/bin/env python3

import pygame
from random import randint

# Инициализация PyGame
pygame.init()

# Настройки окна
SCREEN_WIDTH: int = 500  # Ширина окна
SCREEN_HEIGHT: int = 500  # Высота окна
BACKGROUND_COLOR: tuple[int, int, int] = (255, 255, 255)  # Цвет фона (белый)

# Цвета
BLACK: tuple[int, int, int] = (0, 0, 0)
LIGHT_BLUE: tuple[int, int, int] = (200, 200, 255)

# Настройки шрифта
FONT_SIZE_SMALL: int = 25  # Размер шрифта для вопросов и ответов
FONT_SIZE_LARGE: int = 75  # Размер шрифта для заголовков

# Настройки карточек
CARD_WIDTH: int = 350  # Ширина карточки
CARD_HEIGHT: int = 70  # Высота карточки
CARD_PADDING_X: int = (SCREEN_WIDTH - CARD_WIDTH) // 2  # Центрирование по X
CARD_PADDING_Y_QUESTION: int = 100  # Отступ карточки с вопросом по Y
CARD_PADDING_Y_ANSWER: int = 240  # Отступ карточки с ответом по Y

# Настройки игры
FPS: int = 40  # Количество кадров в секунду


class TextArea:
    """
    Класс для создания области с текстом.
    """

    def __init__(
        self, x: int, y: int, width: int, height: int,
        color: tuple[int, int, int]
    ):
        """
        Инициализация области с текстом.

        :param x: Координата X верхнего левого угла области.
        :param y: Координата Y верхнего левого угла области.
        :param width: Ширина области.
        :param height: Высота области.
        :param color: Цвет заливки области.
        """
        self.rect = pygame.Rect(x, y, width, height)  # Прямоугольник области
        self.fill_color = color  # Цвет заливки
        self.text: str = ""  # Текст
        self.image = None  # Изображение текста

    def set_text(
        self, text: str, fsize: int, text_color: tuple[int, int, int]
    ):
        """
        Установка текста для области.

        :param text: Текст для отображения.
        :param fsize: Размер шрифта.
        :param text_color: Цвет текста.
        """
        self.text = text
        font = pygame.font.Font(None, fsize)
        text_width, text_height = font.size(text)  # Получаем размеры текста

        # Если текст не помещается в карточку, уменьшаем размер шрифта
        while text_width > self.rect.width and fsize > 10:
            fsize -= 1
            font = pygame.font.Font(None, fsize)
            text_width, text_height = font.size(text)

        self.image = font.render(text, True, text_color)

    def draw(self):
        """
        Отрисовка области с текстом.
        Текст центрируется по горизонтали и вертикали внутри карточки.
        """
        pygame.draw.rect(mw, self.fill_color, self.rect)  # Отрисовка прямоугольника

        # Получаем размеры текста
        text_width, text_height = self.image.get_size()

        # Вычисляем координаты для центрирования текста
        text_x = self.rect.x + (self.rect.width - text_width) // 2
        text_y = self.rect.y + (self.rect.height - text_height) // 2

        # Отрисовка текста
        mw.blit(self.image, (text_x, text_y))


# Создание окна игры
mw = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Учебная Игра")
mw.fill(BACKGROUND_COLOR)

# Создание карточек
quest_card = TextArea(
    CARD_PADDING_X, CARD_PADDING_Y_QUESTION, CARD_WIDTH, CARD_HEIGHT, LIGHT_BLUE
)
quest_card.set_text("Нажми Q для вопроса", FONT_SIZE_SMALL, BLACK)

ans_card = TextArea(
    CARD_PADDING_X, CARD_PADDING_Y_ANSWER, CARD_WIDTH, CARD_HEIGHT, LIGHT_BLUE
)
ans_card.set_text("Нажми A для ответа", FONT_SIZE_SMALL, BLACK)

# Основной цикл игры
clock = pygame.time.Clock()
running: bool = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                # Генерация случайного вопроса
                num = randint(1, 3)
                if num == 1:
                    quest_card.set_text(
                        'Что изучаешь в Алгоритмике?', FONT_SIZE_SMALL, BLACK
                    )
                elif num == 2:
                    quest_card.set_text(
                        'На каком языке говорят во Франции?',
                        FONT_SIZE_SMALL, BLACK
                    )
                elif num == 3:
                    quest_card.set_text(
                        'Что растёт на яблоне?', FONT_SIZE_SMALL, BLACK
                    )

            if event.key == pygame.K_a:
                # Генерация случайного ответа
                num = randint(1, 3)
                if num == 1:
                    ans_card.set_text('Python', FONT_SIZE_SMALL, BLACK)
                elif num == 2:
                    ans_card.set_text('Французский', FONT_SIZE_SMALL, BLACK)
                elif num == 3:
                    ans_card.set_text('Яблоки', FONT_SIZE_SMALL, BLACK)

    # Очистка экрана
    mw.fill(BACKGROUND_COLOR)

    # Отрисовка карточек
    quest_card.draw()
    ans_card.draw()

    # Обновление экрана
    pygame.display.update()
    clock.tick(FPS)

# Завершение игры
pygame.quit()

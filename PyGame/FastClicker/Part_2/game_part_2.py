"""Модуль для игры "Быстрый Кликер" на Pygame.

Игра на скорость реакции: нужно кликать по карточкам, когда на них появляется надпись "CLICK".
При правильном клике игрок получает очки, при ошибке - теряет.

Основные классы:
    Area - базовый класс для прямоугольных областей
    Label - класс для текстовых меток (наследуется от Area)

Основные функции:
    create_cards() - создает игровые карточки
    main() - содержит основной игровой цикл

Константы:
    Все параметры игры (цвета, размеры, шрифты) вынесены в константы в начале модуля.

Пример использования:
    Запуск осуществляется вызовом main() при выполнении модуля.
"""

import pygame
import sys

from random import randint
import time


# Инициализация pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
BACKGROUND_COLOR = (200, 255, 255)
CARD_COLOR = (255, 255, 0)
CARD_OUTLINE_COLOR = (80, 80, 255)
CARD_OUTLINE_WIDTH = 10
CARD_WIDTH, CARD_HEIGHT = 70, 100
CARD_TEXT_OFFSET_X, CARD_TEXT_OFFSET_Y = 10, 40
CARD_MARGIN = 100
CARD_START_X = 70
CARD_Y_POSITION = 170
FPS = 40
WAIT_TIME = 20
FONT_NAME = 'verdana,arial,sans-serif'
FONT_SIZE = 26
TEXT_COLOR = (0, 0, 0)

# Цвета
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (80, 80, 255)
YELLOW = (255, 255, 0)


class Area:
    """Базовый класс для прямоугольных областей на экране."""
    
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """Инициализация прямоугольной области.
        
        Args:
            x (int): Координата X верхнего левого угла
            y (int): Координата Y верхнего левого угла
            width (int): Ширина прямоугольника
            height (int): Высота прямоугольника
            color (tuple): Цвет заполнения (R, G, B)
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        """Установка нового цвета заполнения.
        
        Args:
            new_color (tuple): Новый цвет (R, G, B)
        """
        self.fill_color = new_color

    def fill(self, surface):
        """Заливка прямоугольника цветом на указанной поверхности.
        
        Args:
            surface: Поверхность для отрисовки
        """
        pygame.draw.rect(surface, self.fill_color, self.rect)

    def outline(self, surface, frame_color, thickness):
        """Отрисовка обводки прямоугольника.
        
        Args:
            surface: Поверхность для отрисовки
            frame_color (tuple): Цвет обводки (R, G, B)
            thickness (int): Толщина обводки
        """
        pygame.draw.rect(surface, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        """Проверка попадания точки в прямоугольник.
        
        Args:
            x (int): Координата X точки
            y (int): Координата Y точки
            
        Returns:
            bool: True если точка внутри прямоугольника
        """
        return self.rect.collidepoint(x, y)


class Label(Area):
    """Класс для текстовых меток, наследующий от Area."""
    
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """Инициализация текстовой метки."""
        super().__init__(x, y, width, height, color)
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.text = ""
        self.text_color = TEXT_COLOR
        self.image = None

    def set_text(self, text, fsize=FONT_SIZE, text_color=TEXT_COLOR):
        """Установка текста метки.
        
        Args:
            text (str): Текст для отображения
            fsize (int): Размер шрифта
            text_color (tuple): Цвет текста (R, G, B)
        """
        self.text = text
        self.font = pygame.font.SysFont(FONT_NAME, fsize)
        self.text_color = text_color
        self.image = self.font.render(text, True, text_color)

    def draw(self, surface, shift_x=0, shift_y=0):
        """Отрисовка метки на поверхности.
        
        Args:
            surface: Поверхность для отрисовки
            shift_x (int): Смещение текста по X
            shift_y (int): Смещение текста по Y
        """
        self.fill(surface)
        if self.image:
            surface.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


def create_cards(num_cards):
    """Создает список карточек для игры.
    
    Args:
        num_cards (int): Количество карточек
        
    Returns:
        list: Список объектов Label
    """
    cards = []
    x_pos = CARD_START_X
    
    for _ in range(num_cards):
        card = Label(x_pos, CARD_Y_POSITION, CARD_WIDTH, CARD_HEIGHT, CARD_COLOR)
        card.outline(mw, CARD_OUTLINE_COLOR, CARD_OUTLINE_WIDTH)
        card.set_text('CLICK')
        cards.append(card)
        x_pos += CARD_MARGIN
    
    return cards


def main():
    """Основная функция игры."""
    global mw
    
    # Настройка основного окна
    mw = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mw.fill(BACKGROUND_COLOR)
    pygame.display.set_caption("Fast Clicker")
    clock = pygame.time.Clock()
    
    # Инициализация игры
    num_cards = 4
    cards = create_cards(num_cards)
    wait = 0
    score = 0
    current_click_target = 0
    
    # Создаем метку для отображения счета
    score_label = Label(10, 10, 100, 30, BACKGROUND_COLOR)
    score_label.set_text(f"Счет: {score}", 20)
    score_label.draw(mw)
    
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i, card in enumerate(cards):
                    if card.collidepoint(x, y):
                        if i == current_click_target:
                            card.color(GREEN)
                            score += 1
                        else:
                            card.color(RED)
                            score = max(0, score - 1)
                        score_label.set_text(f"Счет: {score}", 20)
                        card.fill(mw)
        
        # Логика обновления карточек
        if wait == 0:
            wait = WAIT_TIME
            current_click_target = randint(0, num_cards - 1)
            for i, card in enumerate(cards):
                card.color(YELLOW)
                if i == current_click_target:
                    card.draw(mw, CARD_TEXT_OFFSET_X, CARD_TEXT_OFFSET_Y)
                else:
                    card.fill(mw)
        else:
            wait -= 1
        
        # Отрисовка интерфейса
        score_label.draw(mw)
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

"""Fast Clicker - учебная версия для платформы "Алгоритмика".

by Sergey Samoylov

Игра на скорость реакции: нужно кликать по карточкам, когда на них появляется надпись "CLICK".
При правильном клике игрок получает очки, при ошибке - теряет.

Особенности:
- Оптимизировано для платформы "Алгоритмика"
- Корректное отображение текста на карточках
- Система подсчета очков
- Таймер смены активной карточки
"""

import pygame
import sys
import random

# Настройки экрана
SCREEN_WIDTH = 500                 
SCREEN_HEIGHT = 500                
BACKGROUND_COLOR = (200, 255, 255) 

# Настройки карточек
CARD_WIDTH = 70                    
CARD_HEIGHT = 100                  
CARD_BORDER = 10                   
CARDS_MARGIN = 30                  
CARDS_COUNT = 4                    
FIRST_CARD_X = 70                  
CARD_Y = 170                       

# Цвета
CARD_COLOR = (255, 255, 0)         
BORDER_COLOR = (80, 80, 255)       
CORRECT_COLOR = (0, 255, 51)       # Зеленый для правильного ответа
WRONG_COLOR = (255, 0, 0)          # Красный для неправильного
TEXT_COLOR = (0, 0, 0)             
TEXT_SIZE = 26                     

# Тайминги
CHANGE_TIME = 20                   # Частота смены карточек (в кадрах)
FPS = 40                           # Кадров в секунду

# Текст
CARD_TEXT = "CLICK"
TEXT_OFFSET_X = 11  
TEXT_OFFSET_Y = 40  


class Area:
    """Базовый класс для прямоугольных игровых объектов."""

    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect)

    def outline(self, color, thickness):
        pygame.draw.rect(screen, color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    """Текстовая метка для карточек."""

    def set_text(self, text, size=TEXT_SIZE, color=TEXT_COLOR):
        self.image = pygame.font.SysFont('Arial', size).render(text, True, color)

    def draw(self, with_text=False):
        self.fill()
        if with_text and hasattr(self, 'image'):
            screen.blit(self.image, (self.rect.x + TEXT_OFFSET_X,
                                    self.rect.y + TEXT_OFFSET_Y))

    def color(self, new_color):
        """Изменяет цвет заливки карточки."""
        self.fill_color = new_color


def create_game_cards():
    """Создает и размещает игровые карточки."""
    cards = []
    current_card_x = FIRST_CARD_X
    
    for _ in range(CARDS_COUNT):
        card = Label(current_card_x, CARD_Y, CARD_WIDTH, CARD_HEIGHT, CARD_COLOR)
        card.outline(BORDER_COLOR, CARD_BORDER)
        card.set_text(CARD_TEXT)
        cards.append(card)
        current_card_x += CARD_WIDTH + CARDS_MARGIN
    
    return cards


def main():
    global screen
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тренажер кликов")
    clock = pygame.time.Clock()
    
    cards = create_game_cards()
    active_card = 0
    timer = 0
    score = 0
    
    # Создаем метку для отображения счета
    score_label = Label(10, 10, 100, 40, BACKGROUND_COLOR)
    score_label.set_text(f"Очки: {score}", 20)
    
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                for i, card in enumerate(cards):
                    if card.collidepoint(x, y):
                        if i == active_card:
                            card.color(CORRECT_COLOR)
                            score += 1
                        else:
                            card.color(WRONG_COLOR)
                            score = max(0, score - 1)
                        score_label.set_text(f"Очки: {score}", 20)
        
        # Логика смены активной карточки
        if timer <= 0:
            timer = CHANGE_TIME
            active_card = random.randint(0, CARDS_COUNT - 1)
            for card in cards:
                card.color(CARD_COLOR)
        else:
            timer -= 1
        
        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        
        # Рисуем карточки
        for i, card in enumerate(cards):
            card.draw(with_text=(i == active_card))
        
        # Рисуем счет
        score_label.draw(with_text=True)
        
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

"""Fast Clicker - учебная версия для платформы "Алгоритмика".

Enhanced version with:
- Click/misclick counters
- Win/lose conditions
- Game over screens
- Time limit
"""

import pygame
import sys
import random
import time

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
CORRECT_COLOR = (0, 255, 51)       
WRONG_COLOR = (255, 0, 0)          
TEXT_COLOR = (0, 0, 0)             
TEXT_SIZE = 26                     

# Тайминги
CHANGE_TIME = 20                   
FPS = 40                           

# Текст
CARD_TEXT = "CLICK"
TEXT_OFFSET_X = 11  
TEXT_OFFSET_Y = 40  

# Game settings
TIME_LIMIT = 30  # seconds
WIN_SCORE = 15


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


def show_game_over_screen(message, bg_color):
    """Показывает экран окончания игры."""
    screen.fill(bg_color)
    
    # Основное сообщение
    game_over = Label(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_color)
    game_over.set_text(message, 60, (0, 0, 100))
    game_over.draw(with_text=True)
    
    # Статистика
    stats_text = f"Очки: {score} | Верных кликов: {correct_clicks} | Ошибок: {wrong_clicks}"
    stats_label = Label(50, 230, 400, 50, bg_color)
    stats_label.set_text(stats_text, 30, (0, 0, 100))
    stats_label.draw(with_text=True)
    
    # Инструкция
    restart_label = Label(50, 300, 400, 50, bg_color)
    restart_label.set_text("Нажмите любую клавишу для выхода", 20, (0, 0, 100))
    restart_label.draw(with_text=True)
    
    pygame.display.update()
    
    # Ожидание нажатия клавиши
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


def main():
    global screen, score, correct_clicks, wrong_clicks
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тренажер кликов")
    clock = pygame.time.Clock()
    
    cards = create_game_cards()
    active_card = 0
    timer = 0
    score = 0
    correct_clicks = 0
    wrong_clicks = 0
    game_active = True
    start_time = time.time()
    
    # Создаем метки для отображения информации
    score_label = Label(10, 10, 150, 40, BACKGROUND_COLOR)
    score_label.set_text(f"Очки: {score}", 20)
    
    clicks_label = Label(10, 50, 200, 40, BACKGROUND_COLOR)
    clicks_label.set_text(f"Верно: {correct_clicks} | Ошибок: {wrong_clicks}", 20)
    
    time_label = Label(350, 10, 150, 40, BACKGROUND_COLOR)
    time_label.set_text(f"Время: {0}/{TIME_LIMIT}", 20)
    
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_active:
                x, y = pygame.mouse.get_pos()
                for i, card in enumerate(cards):
                    if card.collidepoint(x, y):
                        if i == active_card:
                            card.color(CORRECT_COLOR)
                            score += 1
                            correct_clicks += 1
                        else:
                            card.color(WRONG_COLOR)
                            score = max(0, score - 1)
                            wrong_clicks += 1
                        score_label.set_text(f"Очки: {score}", 20)
                        clicks_label.set_text(f"Верно: {correct_clicks} | Ошибок: {wrong_clicks}", 20)
        
        if game_active:
            # Логика смены активной карточки
            if timer <= 0:
                timer = CHANGE_TIME
                active_card = random.randint(0, CARDS_COUNT - 1)
                for card in cards:
                    card.color(CARD_COLOR)
            else:
                timer -= 1
            
            # Проверка времени
            current_time = int(time.time() - start_time)
            time_label.set_text(f"Время: {current_time}/{TIME_LIMIT}", 20)
            
            # Проверка условий победы/поражения
            if current_time >= TIME_LIMIT:
                game_active = False
                show_game_over_screen("Время вышло!", (250, 128, 114))  # Light red
            elif score >= WIN_SCORE:
                game_active = False
                show_game_over_screen("Ты победил!", (200, 255, 200))  # Light green
        
        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        
        # Рисуем карточки
        if game_active:
            for i, card in enumerate(cards):
                card.draw(with_text=(i == active_card))
        
        # Рисуем информацию
        score_label.draw(with_text=True)
        clicks_label.draw(with_text=True)
        time_label.draw(with_text=True)
        
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

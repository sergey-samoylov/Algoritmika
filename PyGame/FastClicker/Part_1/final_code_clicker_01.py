"""Fast Clicker - учебная версия для платформы "Алгоритмика.
by Sergey Samoylov
"""

import pygame
import sys

# Настройки экрана
SCREEN_WIDTH = 500                 # Ширина игрового окна
SCREEN_HEIGHT = 500                # Высота игрового окна
BACKGROUND_COLOR = (200, 255, 255) # Светло-голубой цвет фона

# Настройки карточек
CARD_WIDTH = 70                    # Ширина карточки
CARD_HEIGHT = 100                  # Высота карточки
CARD_BORDER = 10                   # Рамка вокруг карточки
CARDS_MARGIN = 30                  # Расстояние между карточками
CARDS_COUNT = 4                    # Количество карточек
FIRST_CARD_X = 70                  # Стартовая позиция первой карточки по X
CARD_Y = 170                       # Позиция всех карточек по Y

# Цвета
CARD_COLOR = (255, 255, 0)         # Желтый цвет карточек
BORDER_COLOR = (80, 80, 255)       # Синий цвет рамки
TEXT_COLOR = (0, 0, 0)             # Черный цвет текста
TEXT_SIZE = 26                     # Размер шрифта

"""
Платформа "Алгоритмика" пока не поддерживает стандартный рендеринг шрифтов.
Поэтому приходится использовать подбор значений в отступах:
"""
TEXT_OFFSET_X = 11  # Горизонтальный отступ для центрирования текста
TEXT_OFFSET_Y = 40  # Вертикальный отступ для центрирования текста


class Area:
    """Базовый класс для прямоугольных игровых объектов."""
    
    def __init__(self, x, y, width, height, color):
        """Создает прямоугольную область."""
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self):
        """Закрашивает прямоугольник установленным цветом."""
        pygame.draw.rect(screen, self.fill_color, self.rect)

    def outline(self, color, thickness):
        """Рисует контур прямоугольника."""
        pygame.draw.rect(screen, color, self.rect, thickness)


class Label(Area):
    """Текстовая метка для карточек (оптимизировано для Алгоритмики)."""
    
    def set_text(self, text, size=TEXT_SIZE, color=TEXT_COLOR):
        """Устанавливает текст на карточке."""
        self.image = pygame.font.SysFont('Arial', size).render(text, True, color)
        
    def draw(self):
        """Рисует карточку с текстом."""
        self.fill()
        screen.blit(self.image, (self.rect.x + TEXT_OFFSET_X, 
                                self.rect.y + TEXT_OFFSET_Y))


def create_game_cards():
    """Создает и размещает игровые карточки."""
    cards = []
    current_card_x = FIRST_CARD_X  # Текущая позиция по X
    
    for _ in range(CARDS_COUNT):
        card = Label(current_card_x, CARD_Y, CARD_WIDTH, CARD_HEIGHT, CARD_COLOR)
        card.outline(BORDER_COLOR, CARD_BORDER)  # Рамка толщиной 10px
        card.set_text('CLICK')
        cards.append(card)
        current_card_x += CARD_WIDTH + CARDS_MARGIN  # Сдвигаем позицию
    
    return cards


def main():
    """Запускает игру."""
    global screen  # Делаем screen глобальной переменной
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тренажер кликов")
    clock = pygame.time.Clock()
    
    game_cards = create_game_cards()
    
    running = True
    while running:
        # Обработка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        for card in game_cards:
            card.draw()
        
        pygame.display.update()
        clock.tick(40)  # 40 кадров в секунду
    
    pygame.quit()
    sys.exit()

# Позволяет запускать код как самостоятельную программу,
# но не выполняется при импорте
if __name__ == "__main__":
    main()

# Этот блок (3 строчки выше):
#     Защищает от случайного выполнения кода при импорте модуля
#     Делает файл одновременно и импортируемым модулем, и исполняемым скриптом
# 
# Для учебного проекта это важно, так как:
#     Показывает правильный стиль программирования
#     Позволяет импортировать классы без запуска игры

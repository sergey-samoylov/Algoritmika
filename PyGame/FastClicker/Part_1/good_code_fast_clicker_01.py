"""Fast Clicker - часть 1 (финальная версия с русской документацией).

Модуль реализует карточки с автоматически центрированным текстом,
который гарантированно помещается внутри границ карточки.
"""

import pygame
import sys

# Константы игры
SCREEN_WIDTH = 500                  # Ширина игрового окна
SCREEN_HEIGHT = 500                 # Высота игрового окна
BACKGROUND_COLOR = (200, 255, 255)  # Светло-голубой цвет фона

CARD_WIDTH = 70                     # Ширина одной карточки
CARD_HEIGHT = 100                   # Высота одной карточки
CARD_MARGIN = 30                    # Расстояние между карточками
NUM_CARDS = 4                       # Количество карточек
START_X = 70                        # Стартовая позиция первой карточки по X

# Цвета элементов
YELLOW = (255, 255, 0)              # Желтый цвет карточек
BLUE = (80, 80, 255)                # Синий цвет рамки карточек


class Area:
    """Базовый класс для создания прямоугольных областей.

    Позволяет создавать, закрашивать и обводить прямоугольники.
    """

    def __init__(self, x: int = 0, y: int = 0, width: int = 10, height: int = 10, color: tuple = None):
        """Инициализирует прямоугольную область.

        Args:
            x: Координата X верхнего левого угла
            y: Координата Y верхнего левого угла
            width: Ширина прямоугольника
            height: Высота прямоугольника
            color: Цвет заливки в формате RGB
        """
        # Создаем объект Rect для хранения размеров и позиции
        self.rect = pygame.Rect(x, y, width, height)
        # Сохраняем цвет заливки
        self.fill_color = color

    def color(self, new_color: tuple) -> None:
        """Изменяет цвет заливки прямоугольника.

        Args:
            new_color: Новый цвет в формате RGB
        """
        self.fill_color = new_color

    def fill(self) -> None:
        """Закрашивает прямоугольник текущим цветом заливки."""
        pygame.draw.rect(screen, self.fill_color, self.rect)

    def outline(self, frame_color: tuple, thickness: int) -> None:
        """Рисует контур вокруг прямоугольника.

        Args:
            frame_color: Цвет контура
            thickness: Толщина линии контура
        """
        pygame.draw.rect(screen, frame_color, self.rect, thickness)


class Label(Area):
    """Класс для создания текстовых меток с автоматическим центрированием.

    Наследуется от класса Area и добавляет функционал работы с текстом.
    """

    def set_text(self, text: str, fsize: int = 12, text_color: tuple = (0, 0, 0)) -> None:
        """Устанавливает текст метки с автоматическим подбором размера.

        Args:
            text: Текст для отображения
            fsize: Начальный размер шрифта
            text_color: Цвет текста в формате RGB
        """
        # Получаем оптимальный шрифт из доступных
        self.font = self._get_font(fsize)
        self.text_color = text_color

        # Автоматически уменьшаем размер шрифта, пока текст не поместится
        while fsize > 8:  # Минимальный допустимый размер шрифта
            # Создаем поверхность с текстом
            self.image = self.font.render(text, True, text_color)
            # Проверяем, помещается ли текст в карточку с отступами по 5 пикселей
            if (self.image.get_width() < self.rect.width - 10 and
                self.image.get_height() < self.rect.height - 10):
                break
            # Уменьшаем размер шрифта и пробуем снова
            fsize -= 1
            self.font = pygame.font.SysFont(None, fsize)

        # Рассчитываем координаты для центрирования текста
        self.text_x = (self.rect.width - self.image.get_width()) // 2
        self.text_y = (self.rect.height - self.image.get_height()) // 2

    def _get_font(self, fsize: int) -> pygame.font.Font:
        """Возвращает наиболее подходящий доступный шрифт.

        Args:
            fsize: Желаемый размер шрифта

        Returns:
            Объект шрифта pygame
        """
        # Список предпочтительных шрифтов в порядке приоритета
        font_candidates = ['verdana', 'arial', 'freesansbold', None]

        for name in font_candidates:
            try:
                # Пробуем создать шрифт
                return pygame.font.SysFont(name, fsize)
            except:
                # Если шрифт недоступен, пробуем следующий
                continue
        # Если ничего не найдено, возвращаем системный шрифт
        return pygame.font.SysFont(None, fsize)

    def draw(self) -> None:
        """Отрисовывает карточку с центрированным текстом."""
        # Сначала рисуем заливку
        self.fill()
        # Затем рисуем текст в рассчитанной позиции
        screen.blit(self.image, (self.rect.x + self.text_x, self.rect.y + self.text_y))


def create_cards() -> list:
    """Создает и возвращает список игровых карточек.

    Returns:
        Список объектов Label - игровые карточки
    """
    cards = []
    current_x = START_X  # Начальная позиция по X

    for i in range(NUM_CARDS):
        # Создаем новую карточку
        card = Label(current_x, 170, CARD_WIDTH, CARD_HEIGHT, YELLOW)
        # Добавляем синюю рамку толщиной 10 пикселей
        card.outline(BLUE, 10)
        # Устанавливаем текст (номер карточки увеличивается от 1 до NUM_CARDS)
        card.set_text(f'КЛИК {i+1}', 20)
        # Добавляем карточку в список
        cards.append(card)
        # Сдвигаем позицию для следующей карточки
        current_x += CARD_WIDTH + CARD_MARGIN

    return cards


def main() -> None:
    """Главная функция игры, управляющая основным циклом."""
    global screen  # Используем глобальную переменную для экрана

    # Инициализация pygame
    pygame.init()
    # Создаем окно игры
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Устанавливаем заголовок окна
    pygame.display.set_caption("Fast Clicker")
    # Создаем объект для контроля FPS
    clock = pygame.time.Clock()

    # Создаем игровые карточки
    cards = create_cards()

    # Основной игровой цикл
    running = True
    while running:
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Закрашиваем фон каждый кадр
        screen.fill(BACKGROUND_COLOR)

        # Рисуем все карточки
        for card in cards:
            card.draw()

        # Обновляем экран
        pygame.display.flip()
        # Поддерживаем 40 FPS
        clock.tick(40)

    # Завершаем работу pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # Запускаем игру только если файл выполняется напрямую
    main()

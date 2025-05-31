import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint with Transparency")

# Цвет фона (rose)
BG_COLOR = (245, 234, 207)
screen.fill(BG_COLOR)

# Прозрачный холст (альфа-канал)
canvas = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
canvas.fill((255, 255, 255, 0))  # Прозрачный фон

# Начальные настройки кисти
brush_color = (0, 0, 0, 255)  # Чёрный цвет (R, G, B, Alpha)
brush_size = 5                 # Размер кисти
drawing = False                # Флаг: рисуем или нет
alpha = 128                    # Начальная прозрачность (0-255)
last_pos = None                # Последняя позиция мыши

# Цвета для палитры
COLORS = {
    "black": (0, 0, 0, 255),
    "red": (255, 0, 0, 255),
    "green": (0, 255, 0, 255),
    "blue": (0, 0, 255, 255),
    "yellow": (255, 255, 0, 255),
    "eraser": (255, 255, 255, 255)  # Ластик (белый)
}

# Размеры кисти
SIZES = [2, 5, 10, 20]

def draw_palette():
    """Рисует палитру цветов и размеры кисти."""
    # Рисуем цвета
    x, y = 10, 10
    for color_name, color_rgba in COLORS.items():
        pygame.draw.rect(screen, color_rgba[:3], (x, y, 30, 30))
        x += 35

    # Рисуем размеры кисти
    x = 10
    y = 50
    for size in SIZES:
        pygame.draw.circle(screen, (100, 100, 100), (x + 15, y + 15), size)
        x += 35

        
    font = pygame.font.SysFont('Arial', 20)
    # Отображаем текущую прозрачность
    alpha_text = font.render(f"Alpha: {alpha}", True, (0, 0, 0))
    screen.blit(alpha_text, (10, 130))

def draw_line(start, end, color, size):
    """Рисует линию между двумя точками."""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(canvas, color, (x, y), size)

# Главный цикл программы
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажатие кнопки мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            # Проверяем, кликнули ли по палитре
            color_x, color_y = 10, 10
            for color_name, color_rgba in COLORS.items():
                if color_x <= x <= color_x + 30 and color_y <= y <= color_y + 30:
                    brush_color = (*color_rgba[:3], alpha)
                color_x += 35

            # Проверяем, кликнули ли по размеру кисти
            size_x, size_y = 10, 50
            for size in SIZES:
                if size_x <= x <= size_x + 30 and size_y <= y <= size_y + 30:
                    brush_size = size
                size_x += 35
                
            # Проверяем, кликнули ли по кнопке очистки
            if 10 <= x <= 110 and 90 <= y <= 120:
                canvas.fill((255, 255, 255, 0))
                
            if event.button == 1:  # Левая кнопка
                drawing = True
                last_pos = event.pos
                pygame.draw.circle(canvas, brush_color, event.pos, brush_size)

        # Отпускание кнопки мыши
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None

        # Движение мыши с зажатой кнопкой — рисуем
        elif event.type == pygame.MOUSEMOTION and drawing:
            if last_pos:
                draw_line(last_pos, event.pos, brush_color, brush_size)
            last_pos = event.pos

    # Обработка нажатий клавиш для изменения прозрачности
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        alpha = min(255, alpha + 1)
        brush_color = (*brush_color[:3], alpha)
    if keys[pygame.K_DOWN]:
        alpha = max(0, alpha - 1)
        brush_color = (*brush_color[:3], alpha)

    # Очищаем экран и рисуем холст
    screen.fill(BG_COLOR)
    screen.blit(canvas, (0, 0))

    # Рисуем палитру
    draw_palette()
    pygame.display.flip()
    clock.tick(60)  # Ограничиваем FPS

# Выход из Pygame
pygame.quit()

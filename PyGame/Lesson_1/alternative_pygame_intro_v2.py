# Этот код исключительно для работы на платформе "Алгоритмика"

import pygame
from random import choice

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Question Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (200, 200, 255)
BLACK = (0, 0, 0)

# Font setup - using default font
font = pygame.font.Font(None, 36)  # Size 36 is large enough to see

# Game state
question = "Q - задать вопрос"
answer = "А - получить ответ"

# Main game loop
clock = pygame.time.Clock()
running = True
try:
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    question = choice([
                        "Что ты изучаешь?",
                        "Основной язык Франции?",
                        "Что растёт на яблоне?"
                    ])
                elif event.key == pygame.K_a:
                    answer = choice([
                        "Python",
                        "Французский",
                        "Яблоки"
                    ])

        # Draw everything
        screen.fill(WHITE)

        # Question box (top)
        pygame.draw.rect(screen, BLUE, (50, 100, 400, 70))
        q_text = font.render(question, True, BLACK)
        screen.blit(q_text, (60, 125))  # Fixed position

        # Answer box (bottom)
        pygame.draw.rect(screen, BLUE, (50, 250, 400, 70))
        a_text = font.render(answer, True, BLACK)
        screen.blit(a_text, (60, 275))  # Fixed position

        pygame.display.update()
        clock.tick(40)
finally:
    pygame.quit()

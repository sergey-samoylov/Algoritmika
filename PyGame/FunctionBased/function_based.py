#!/usr/bin/env python3

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH: int = 800
HEIGHT: int = 600
screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Controls Example")

# Colors
BLUE: tuple[int, int, int] = (0, 0, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)

# Game variables
player_x: int = 400
player_y: int = 300
player_speed: int = 15

def handle_controls(events: list[pygame.event.Event]) -> None:
    """
    Handle key presses and mouse clicks.
    """
    global player_x, player_y

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Vim based key navigation
            if event.key == pygame.K_k:
                player_y -= player_speed
            if event.key == pygame.K_j:
                player_y += player_speed
            if event.key == pygame.K_h:
                player_x -= player_speed
            if event.key == pygame.K_l:
                player_x += player_speed

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at:", event.pos)
            if event.button == 3:  # Right mouse button
                print("Right mouse button clicked at:", event.pos)

def draw_player() -> None:
    """
    Draw the player on the screen.
    """
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))

def main() -> None:
    """
    Main game loop.
    """
    global screen

    clock: pygame.time.Clock = pygame.time.Clock()

    while True:
        # Get all events
        events: list[pygame.event.Event] = pygame.event.get()

        # Handle controls
        handle_controls(events)

        # Clear the screen
        screen.fill(BLACK)

        # Draw the player
        draw_player()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()

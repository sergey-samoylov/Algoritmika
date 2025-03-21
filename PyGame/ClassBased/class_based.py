#!/usr/bin/env python3

import pygame
import sys

# Screen dimensions
WIDTH: int = 800
HEIGHT: int = 600

# Colors
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)

class Player:
    """A class to represent the player."""

    def __init__(self, x: int, y: int, speed: int) -> None:
        self.x: int = x
        self.y: int = y
        self.speed: int = speed
        self.size: int = 50

    def move(self, dx: int, dy: int) -> None:
        """Move the player by dx and dy."""
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the player on the screen."""
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.size, self.size))

class Game:
    """A class to manage the game loop and state."""

    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Class-Based Pygame Example")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.player: Player = Player(400, 300, 5)

    def handle_events(self) -> None:
        """Handle user input and other events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Vim based keys
                if event.key == pygame.K_k:
                    self.player.move(0, -1)
                if event.key == pygame.K_j:
                    self.player.move(0, 1)
                if event.key == pygame.K_h:
                    self.player.move(-1, 0)
                if event.key == pygame.K_l:
                    self.player.move(1, 0)

    def run(self) -> None:
        """Run the game loop."""
        while True:
            self.handle_events()

            # Clear the screen
            self.screen.fill(BLACK)

            # Draw the player
            self.player.draw(self.screen)

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()

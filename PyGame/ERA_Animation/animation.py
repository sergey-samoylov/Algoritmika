"""
Platformer Game with PyGame
Main game module containing game initialization, sprite classes and game loop
"""

import pygame
import sys

# Initialize PyGame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 50
ANIMATION_DELAY = 20

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

# Camera setup (initially set to cover entire screen)
camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


def start_screen():
    """
    Display the start menu screen with start and exit buttons.
    
    Returns:
        tuple: Rectangles for start and exit buttons
    """
    try:
        # Load and scale start button image
        start_img = pygame.transform.scale(
            pygame.image.load('start.png'), (200, 70)
        )
        start_rect = start_img.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        )
        screen.blit(start_img, start_rect)
        
        # Load and scale exit button image
        stop_img = pygame.transform.scale(
            pygame.image.load('exit.png'), (200, 70)
        )
        stop_rect = stop_img.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        screen.blit(stop_img, stop_rect)
        
        return start_rect, stop_rect
        
    except pygame.error as e:
        print(f"Error loading menu images: {e}")
        sys.exit()


class GameSprite:
    """Base class for all game sprites with basic drawing functionality."""
    
    def __init__(self, picture, x, y):
        """
        Initialize game sprite.
        
        Args:
            picture (str): Path to sprite image
            x (int): Initial x position
            y (int): Initial y position
        """
        try:
            self.image = pygame.transform.scale(
                pygame.image.load(picture), (100, 120)
            )
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        except pygame.error as e:
            print(f"Error loading sprite image {picture}: {e}")
            # Create a placeholder surface if image loading fails
            self.image = pygame.Surface((100, 120))
            self.image.fill((255, 0, 0))  # Red placeholder
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def draw(self):
        """Draw sprite on screen with camera offset."""
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y - camera.y))


class Player(GameSprite):
    """Player character with animation and movement capabilities."""
    
    # Animation states constants
    STATE_RIGHT = 0    # Facing right (idle)
    STATE_LEFT = 1     # Facing left (idle)
    STATE_MOVE_RIGHT = 2  # Moving right
    STATE_MOVE_LEFT = 3   # Moving left
    
    def __init__(self, picture, x, y, speed):
        """
        Initialize player character.
        
        Args:
            picture (str): Path to initial sprite image
            x (int): Initial x position
            y (int): Initial y position
            speed (int): Movement speed
        """
        super().__init__(picture, x, y)
        self.speed = speed
        self.rotation = self.STATE_RIGHT  # Initial facing direction
        self.pick_ind = 0  # Animation frame index
        
        # Pre-load animation frames
        self._load_animations()

    def _load_animations(self, path='Images/Warrior/'):
        """
        Load all animation frames for the player.
        
        Args:
            path (str): Path to animation frames directory
        """
        try:
            # Idle animation frames (facing right)
            self.stay_right = [
                pygame.transform.scale(
                    pygame.image.load(f'{path}{i}.png'), (100, 120)
                ).convert_alpha() for i in range(1, 11)
            ]
            # Mirror for left-facing idle
            self.stay_left = [
                pygame.transform.flip(picture, True, False) 
                for picture in self.stay_right
            ]
            
            # Movement animation frames (facing right)
            self.move_right = [
                pygame.transform.scale(
                    pygame.image.load(f'{path}{i}.png'), (100, 120)
                ).convert_alpha() for i in range(11, 19)
            ]
            # Mirror for left-facing movement
            self.move_left = [
                pygame.transform.flip(picture, True, False) 
                for picture in self.move_right
            ]
            
        except pygame.error as e:
            print(f"Error loading animation frames: {e}")
            # Create placeholder animations if loading fails
            self._create_placeholder_animations()

    def _create_placeholder_animations(self):
        """Create placeholder animations if image loading fails."""
        placeholder = pygame.Surface((100, 120))
        placeholder.fill((0, 255, 0))  # Green placeholder
        
        self.stay_right = [placeholder] * 10
        self.stay_left = [placeholder] * 10
        self.move_right = [placeholder] * 8
        self.move_left = [placeholder] * 8

    def animate(self):
        """
        Update player animation based on current state and movement.
        Handles frame selection, movement, and screen boundaries.
        """
        # Handle different animation states
        if self.rotation == self.STATE_RIGHT:
            # Idle facing right
            frame_index = (self.pick_ind // 6) % len(self.stay_right)
            self.image = self.stay_right[frame_index]
            
        elif self.rotation == self.STATE_LEFT:
            # Idle facing left
            frame_index = (self.pick_ind // 6) % len(self.stay_left)
            self.image = self.stay_left[frame_index]
            
        elif self.rotation == self.STATE_MOVE_RIGHT:
            # Moving right
            frame_index = (self.pick_ind // 7) % len(self.move_right)
            self.image = self.move_right[frame_index]
            self.rect.x += self.speed
            
        elif self.rotation == self.STATE_MOVE_LEFT:
            # Moving left
            frame_index = (self.pick_ind // 7) % len(self.move_left)
            self.image = self.move_left[frame_index]
            self.rect.x -= self.speed

        # Screen boundary checking
        if self.rect.x > BG_WIDTH - 100:
            self.rotation = self.STATE_RIGHT  # Stop at right edge
        if self.rect.x < 0:
            self.rotation = self.STATE_LEFT   # Stop at left edge

        # Update animation frame index (loop after 55 frames)
        self.pick_ind = (self.pick_ind + 1) % 55


# Load background images
try:
    BG_MENU = pygame.transform.scale(
        pygame.image.load('bg_menu.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    BG = pygame.transform.scale(
        pygame.image.load('bg.jpg'), (8000, SCREEN_HEIGHT)
    )
    BG_WIDTH, BG_HEIGHT = BG.get_size()
except pygame.error as e:
    print(f"Error loading background images: {e}")
    sys.exit()

# Create player instance
hero = Player('Images/Warrior/1.png', 300, 380, 3)

# Load and play music
try:
    menu_music = pygame.mixer.Sound('menu_music.mp3')
    game_music = pygame.mixer.Sound('game_music.mp3')
    menu_music.play(-1)  # Loop menu music
except pygame.error as e:
    print(f"Error loading music: {e}")

# Game state flags
main_menu = True
running = True
finish = False
game_start = False

# Get button rectangles from start screen
start_rect, stop_rect = start_screen()

# Main game loop
clock = pygame.time.Clock()

while running:
    if not finish:
        if main_menu:
            # Draw menu background
            screen.blit(BG_MENU, (0, 0))
            start_rect, stop_rect = start_screen()
            
            # Handle menu events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if start_rect.collidepoint(x, y):
                        # Start game
                        game_start = True
                        main_menu = False
                        menu_music.stop()
                        game_music.play(-1)
                    elif stop_rect.collidepoint(x, y):
                        # Exit game
                        pygame.quit()
                        sys.exit()
                        
        elif game_start:
            # Handle game events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                # Handle key events for player movement
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        hero.rotation = Player.STATE_RIGHT
                    elif event.key == pygame.K_LEFT:
                        hero.rotation = Player.STATE_LEFT
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        hero.rotation = Player.STATE_MOVE_RIGHT
                    elif event.key == pygame.K_LEFT:
                        hero.rotation = Player.STATE_MOVE_LEFT
            
            # Update camera position to follow player
            camera.x = hero.rect.x - SCREEN_WIDTH // 2
            camera.y = hero.rect.y - SCREEN_HEIGHT // 2
            
            # Keep camera within background bounds
            camera.x = max(0, min(camera.x, BG_WIDTH - SCREEN_WIDTH))
            camera.y = max(0, min(camera.y, BG_HEIGHT - SCREEN_HEIGHT))
            
            # Draw game scene
            screen.blit(BG, (-camera.x, -camera.y))
            hero.draw()
            hero.animate()
    
    # Update display and control frame rate
    pygame.display.flip()
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
sys.exit()

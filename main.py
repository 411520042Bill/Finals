import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Constants for the game window
WINDOW_WIDTH = 575  # Increased width
WINDOW_HEIGHT = 505  # Increased height
FPS = 60  # Frames per second

# Initialize the game
game = Game(WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

# Run the game loop
game.run()

# Quit Pygame
pygame.quit()


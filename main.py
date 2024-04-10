import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants for the game window
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 600
FPS = 60  # Frames per second

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel Style Restaurant Game")

# Define colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

# Load tile images (replace 'path_to_tile.png' with your actual file paths)
white_tile = pygame.image.load('_white_tile1.jpg')  # Replace with your first floor tile image
lpink_tile = pygame.image.load('light_pink_tile1.jpg')  # Replace with your second floor tile image
dpink_tile = pygame.image.load('dark_pink_tile1.jpg')  # Replace with your third floor tile image
monster_image = pygame.image.load('monster.jpg')
character_image = pygame.image.load('characterIlde.png')
# wall_tile = pygame.image.load('path_to_wall_tile.png')  # Replace with your wall tile image
# table_tile = pygame.image.load('path_to_table_tile.png')  # Replace with your table tile image
# ... Load other tiles as needed

# Define the layout of the restaurant (0=floor1, 1=floor2, 2=floor3, 3=wall, 4=table, etc.)
layout = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

# Function to make impenetrable object
def make_impenetrable(layout, immutable_nums):
    modified_layout = []
    for row in layout:
        modified_row = []
        for num in row:
            if num in immutable_nums:
                modified_row.append((num,))
            else:
                modified_row.append(num)
        modified_layout.append(modified_row)
    return modified_layout

immutable_nums = {3}  # Numbers to make immutable
#layout = make_immutable(layout, immutable_nums) #call the function

# Function to draw the restaurant map
def draw_map():
    tile_size = white_tile.get_width()  # Assuming each tile has the same size
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile == 0:
                window.blit(white_tile, (x * tile_size, y * tile_size))
            elif tile == 3:
                window.blit(lpink_tile, (x * tile_size, y * tile_size))
            elif tile == 2:
                window.blit(dpink_tile, (x * tile_size, y * tile_size))
            '''
            # elif tile == 3:
            #     window.blit(wall_tile, (x * tile_size, y * tile_size))
            # elif tile == 4:
            #     window.blit(table_tile, (x * tile_size, y * tile_size))
            # Add more conditions for other tiles
            '''

class Charater:    
    def __init__(self, x, y, speed=5, image_path=character_image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)  # Load the character image
        self.size = self.image.get_size()
    
    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

#Initialize and create the character
characterSize = 40 
character = Character(WINDOW_WIDTH // 2 - characterSize // 2, WINDOW_HEIGHT // 2 - characterSize // 2, image_path=character_image)

# Monster class
class Monster:
    
    def __init__(monster, x, y, size):
        monster.x = x
        monster.y = y
        monster.size = size 
        monster.frames_count = 0 
        monster.dx, monster.dy = 0, 0
        monster.angle = random.uniform(0, 2 * math.pi)

    def move(monster):
        speed = 0.03  # Fixed speed
        # directions_dx = [-0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04]  # right, left
        # directions_dy = [-0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04]  # up, down
        angle_range = math.pi / 2  # The range of angle change
        if monster.frames_count % 32 == 0:  # Number of frames moving in the same direction
            monster.angle += random.uniform(-angle_range, angle_range)  # Random angle within a small range
            monster.dx = speed * math.cos(monster.angle)
            monster.dy = speed * math.sin(monster.angle)
        monster.x += monster.dx
        monster.y += monster.dy
        monster.frames_count += 1
        
    # draw the monster
    def draw_monster(monster):
        monster_image_scaled = pygame.transform.scale(monster_image, (monster.size, monster.size))  # Scale the monster image
        window.blit(monster_image_scaled, (monster.x * monster.size, monster.y * monster.size))

# Create a monster
# To be modified: Random monster spawn point
monster_size = 30
monster = Monster(10, 10, monster_size)


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Move the monster every 10 frames
    monster.move()

    # Draw the map
    draw_map()
    
    # Draw the monster
    monster.draw_monster()

    # Update the display
    pygame.display.flip()

    # Maintain the specified frames per second
    clock.tick(FPS)


# Quit the game
pygame.quit()

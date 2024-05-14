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
pygame.display.set_caption("Pixel Style Game")

# Define colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

# Load tile images
white_tile = pygame.image.load('_white_tile1.jpg')
lpink_tile = pygame.image.load('light_pink_tile1.jpg')
dpink_tile = pygame.image.load('dark_pink_tile1.jpg')
monster_image = pygame.image.load('monster.jpg')
girl_idle_left = pygame.image.load('girl\girl_idle_left.png')
girl_idle_right = pygame.image.load('girl\girl_idle_right.png')

girl_walk_left_1 = pygame.image.load('girl\girl_walk_left_1.png')
girl_walk_left_2 = pygame.image.load('girl\girl_walk_left_2.png')
girl_walk_right_1 = pygame.image.load('girl\girl_walk_right_1.png')
girl_walk_right_2 = pygame.image.load('girl\girl_walk_right_2.png')

megaman_idle_left = pygame.image.load('megaman\megaman_idle_left.png')
megaman_blink_left = pygame.image.load('megaman\megaman_blink_left.png')
megaman_run_left_0 = pygame.image.load('megaman\megaman_run_left_0.png')
megaman_run_left_1 = pygame.image.load('megaman\megaman_run_left_1.png')
megaman_run_left_2 = pygame.image.load('megaman\megaman_run_left_2.png')

megaman_idle_right = pygame.image.load('megaman\megaman_idle_right.png')
megaman_blink_right = pygame.image.load('megaman\megaman_blink_right.png')
megaman_run_right_0 = pygame.image.load('megaman\megaman_run_right_0.png')
megaman_run_right_1 = pygame.image.load('megaman\megaman_run_right_1.png')
megaman_run_right_2 = pygame.image.load('megaman\megaman_run_right_2.png')
# Define new dimensions for the character image
walk_width = 216  # Set the desired width
walk_height = 108  # Set the desired height
char_width = 216  # Set the desired width
char_height = 108  # Set the desired height
girl_idle_left = pygame.transform.scale(girl_idle_left, (char_width, char_height))
girl_idle_right = pygame.transform.scale(girl_idle_right, (char_width, char_height))

girl_walk_left_1 = pygame.transform.scale(girl_walk_left_1, (walk_width, walk_height))
girl_walk_left_2 = pygame.transform.scale(girl_walk_left_2, (walk_width, walk_height))
girl_walk_right_1 = pygame.transform.scale(girl_walk_right_1, (walk_width, walk_height))
girl_walk_right_2 = pygame.transform.scale(girl_walk_right_2, (walk_width, walk_height))
# character_image = pygame.transform.scale(girl_walk_left_lu, (walk_width, walk_height))

# Define the layout of the area
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


# Function to draw the map
def draw_map():
    tile_size = white_tile.get_width()
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile == 0:
                window.blit(white_tile, (x * tile_size, y * tile_size))
            elif tile == 2:
                window.blit(lpink_tile, (x * tile_size, y * tile_size))
            elif tile == 3:
                window.blit(dpink_tile, (x * tile_size, y * tile_size))



class Character:
    def __init__(self, x, y, speed=3, size=30, health=3):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.health = health
        self.image = megaman_idle_left  # Start facing left
        self.rect = self.image.get_rect(center=(x, y))
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100  # Frame rate in milliseconds
        self.last_direction = 'left'  # Keep track of the last movement direction

        # Animation frames for left and right movements
        self.left_frames = [girl_walk_left_1, girl_walk_left_2, girl_walk_left_1, girl_walk_left_2]
        self.right_frames = [girl_walk_right_1, girl_walk_right_2, girl_walk_right_1, girl_walk_right_2]
        self.current_frame = 0
        self.walking = False

    def move(self, keys):
        self.walking = False
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.walking = True
            self.image = self.left_frames[self.current_frame]
            self.last_direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.walking = True
            self.image = self.right_frames[self.current_frame]
            self.last_direction = 'right'
        elif keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.walking = True
            # Move up or down while maintaining the last horizontal walking animation
            if self.last_direction == 'left':
                self.y += self.speed if keys[pygame.K_DOWN] else -self.speed
                self.image = self.left_frames[self.current_frame]
            else:
                self.y += self.speed if keys[pygame.K_DOWN] else -self.speed
                self.image = self.right_frames[self.current_frame]

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            # Set the image to the appropriate standing face when not moving
            if self.last_direction == 'left':
                self.image = girl_idle_left
            else:
                self.image = girl_idle_right

        # Update rect position
        self.rect.center = (self.x, self.y)
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.size*2))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.size*2))

        # Update animation frames
        self.update_animation()
   
   
    def take_damage(self, damage):
        self.health -= damage
        if(self.health<0):
            character.die()



    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if self.walking:
                self.current_frame = (self.current_frame + 1) % 4

    def draw(self):
        window.blit(self.image, self.rect.topleft)


character = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

class Monster:
    def __init__(self, x, y, size, attack_power):
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.transform.scale(monster_image, (size, size))
        self.dx, self.dy = 0, 0
        self.angle = random.uniform(0, 2 * math.pi)

    def move_towards_player(self, player, other_monsters):
        if random.random() < 0.15:  # Slight chance to adjust direction towards the player
            direction = math.atan2(player.y - self.y, player.x - self.x)
            self.angle = 0.9 * self.angle + 0.1 * direction
        
        # Handle repulsion from other monsters
        for other in other_monsters:
            if other != self:
                distance = math.hypot(other.x - self.x, other.y - self.y)
                if distance < 50:  # arbitrary repulsion distance
                    repulsion_angle = math.atan2(self.y - other.y, self.x - other.x)
                    self.angle = 0.9 * self.angle + 0.1 * repulsion_angle

        speed = 1
        self.dx = speed * math.cos(self.angle)
        self.dy = speed * math.sin(self.angle)
        self.x += self.dx
        self.y += self.dy

        # Boundary checking
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.size))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.size))

    def attack(self, character):
        character.take_damage(self.attack_power)

    def draw(self):
        window.blit(self.image, (self.x, self.y))

# Create monsters
monsters = [Monster(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 30) for _ in range(5)]

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    window.fill(WHITE)
    draw_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    character.move(keys)
    character.draw()

    distance = math.sqrt((monster.x - character.x) ** 2 + (monster.y - character.y) ** 2)

    if distance < 10:
        monster.attack(character)
        print(f"Character health: {character.health}")
    for mon in monsters:
        mon.move_towards_player(character, monsters)  
        mon.draw()

    pygame.display.flip()
    clock.tick(FPS)
    if character.health <= 0:
        running = false

pygame.quit()

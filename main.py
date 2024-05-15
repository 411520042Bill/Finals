import pygame
import random
import math
import time

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

potus_idle = pygame.image.load('POTUS\POTUS (2).png')
potus_creep = pygame.image.load('POTUS\Creepy_POTUS (2).png')
potus_left_up = pygame.image.load('POTUS\POTUS_lup.png')
potus_right_up = pygame.image.load('POTUS\POTUS_rup.png')

megaman_idle_left = pygame.image.load('megaman\megaman_idle_left.png')
megaman_run_left_0 = pygame.image.load('megaman\megaman_run_left_0.png')
megaman_run_left_1 = pygame.image.load('megaman\megaman_run_left_1.png')
megaman_run_left_2 = pygame.image.load('megaman\megaman_run_left_2.png')

megaman_idle_right = pygame.image.load('megaman\megaman_idle_right.png')
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
        self.base_speed = speed
        self.speed = speed
        self.size = size
        self.health = health
        self.image = girl_idle_left  # Start facing left
        self.rect = self.image.get_rect(center=(x, y))
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100  # Frame rate in milliseconds
        self.last_direction = 'left'  # Keep track of the last movement direction

        # Animation frames for left and right movements
        self.left_frames = [girl_walk_left_1, girl_walk_left_2, girl_walk_left_1, girl_walk_left_2]
        self.right_frames = [girl_walk_right_1, girl_walk_right_2, girl_walk_right_1, girl_walk_right_2]
        self.current_frame = 0
        self.walking = False

        self.invincible = False  # Whether the character is invincible
        self.invincible_time = 0  # Time at which the character became invincible
        self.invincible_duration = 3000  # Duration of invincibility in milliseconds

    def adjust_speed(self, is_creepy_active):
        if is_creepy_active:
            self.speed = self.base_speed * 0.5  # Reduce speed by 30%
        else:
            self.speed = self.base_speed  # Reset to normal speed

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
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.size * 2))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.size * 2))

        # Update animation frames
        self.update_animation()

        # Check invincibility duration
        if self.invincible and pygame.time.get_ticks() - self.invincible_time > self.invincible_duration:
            self.invincible = False

    def take_damage(self, damage):
        if not self.invincible:
            self.health -= damage
            if self.health <= 0:
                self.die()
            else:
                self.invincible = True
                self.invincible_time = pygame.time.get_ticks()

    def die(self):
        print("Character has died.")

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
    def __init__(self, x, y, size, attack_power=1):
        self.x = x
        self.y = y
        self.size = size * 3.3
        self.attack_power = attack_power
        self.idle_image = pygame.transform.scale(potus_idle, (self.size, self.size))
        self.creepy_image = pygame.transform.scale(potus_creep, (self.size, self.size))
        self.image = self.idle_image
        self.rect = self.image.get_rect(center=(x, y))
        self.move_active = True
        self.last_toggle = time.time()
        self.toggle_interval = random.randint(1, 2)
        self.last_animation_change = time.time()
        self.current_frame = 0
        self.animation_frames = [
            pygame.transform.scale(potus_left_up, (self.size, self.size)),
            pygame.transform.scale(potus_right_up, (self.size, self.size))
        ]
        self.dialog = "I'll lick you all over..."
        self.show_dialog = False
        self.creepy_active = False

    def move_towards_player(self, player):
        if (time.time() - self.last_toggle) > self.toggle_interval:
            self.move_active = not self.move_active
            self.last_toggle = time.time()

            if not self.move_active:  # Only decide when the monster goes idle
                if random.random() < 1:  # 10% chance
                    self.image = self.creepy_image
                    self.dialog = "Give me a piece"
                    self.show_dialog = True
                    self.toggle_interval = 3  # Extended idle time for creepy version
                    self.creepy_active = True
                else:
                    self.image = self.idle_image
                    self.show_dialog = False
                    self.toggle_interval = random.randint(1, 2)
                    self.creepy_active = False
            else:
                self.creepy_active = False

        if self.move_active:
            if time.time() - self.last_animation_change > 0.1:
                self.current_frame = (self.current_frame + 1) % 2
                self.image = self.animation_frames[self.current_frame]
                self.last_animation_change = time.time()

            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            distance = math.hypot(dx, dy)

            if distance < 5:
                self.rect.center = player.rect.center
                self.attack(player)
            else:
                dx, dy = dx / distance, dy / distance
                self.rect.centerx += dx * 2.5
                self.rect.centery += dy * 2.5
            self.show_dialog = False  # Hide dialog when moving

    def attack(self, character):
        character.take_damage(self.attack_power)

    def draw_dialog(self, window):
        if self.show_dialog:
            # Set the font for the text
            font = pygame.font.Font(None, 24)
            text = font.render(self.dialog, True, pygame.Color('black'))
            
            # Get the text rectangle and adjust the size for padding
            text_rect = text.get_rect()
            padding = 10
            bubble_width = text_rect.width + 2 * padding
            bubble_height = text_rect.height + 2 * padding
            
            # Calculate the bubble's position to be above the monster
            bubble_rect = pygame.Rect(self.rect.centerx - bubble_width / 2, self.rect.top - bubble_height - 10, bubble_width, bubble_height)
            
            # Draw the text within the bubble
            text_rect.center = bubble_rect.center
            
            # Draw the bubble
            pygame.draw.ellipse(window, pygame.Color('white'), bubble_rect)
            pygame.draw.ellipse(window, pygame.Color('black'), bubble_rect, 2)  # Bubble border

            # Drawing the tail of the bubble
            tail_width = 15
            tail_height = 20
            tail = [(self.rect.centerx, self.rect.top - 10), 
                    (self.rect.centerx - tail_width / 2, bubble_rect.bottom), 
                    (self.rect.centerx + tail_width / 2, bubble_rect.bottom)]
            pygame.draw.polygon(window, pygame.Color('white'), tail)
            pygame.draw.polygon(window, pygame.Color('black'), tail, 2)  # Tail border
            
            # Blit the text last so it's on top of the bubble
            window.blit(text, text_rect)

    def draw(self):
        window.blit(self.image, self.rect.topleft)


monster = Monster(random.randint(0, WINDOW_WIDTH - 30), random.randint(0, WINDOW_HEIGHT - 30), 30)


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
    character.adjust_speed(monster.creepy_active)  # Adjust speed based on monster state
    character.move(keys)
    
    if character.health > 0:
        character.draw()
        monster.move_towards_player(character)
        monster.draw()
        monster.draw_dialog(window)
        
        # Calculate distance between the monster and the character
        distance = math.sqrt((monster.rect.centerx - character.rect.centerx) ** 2 + 
                             (monster.rect.centery - character.rect.centery) ** 2)
        
        # If distance is less than a certain value, the character takes damage
        if distance < 50:  # Adjust this value as needed
            monster.attack(character)
            print(f"Character health: {character.health}")
    else:
        # Draw black screen and "FAILED" text
        window.fill(BLACK)
        font = pygame.font.Font(pygame.font.get_default_font(), 74)  # You can change the font here if needed
        text = font.render("FAILED", True, (255, 0, 0))  # Red color for "FAILED"
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

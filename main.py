import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants for the game window
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 530
FPS = 60  # Frames per second

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel Style Game")

# Define colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)

# Load tile images
white_tile = pygame.image.load('_white_tile1.jpg')
lpink_tile = pygame.image.load('light_pink_tile1.jpg')
dpink_tile = pygame.image.load('dark_pink_tile1.jpg')
monster_image = pygame.image.load('monster.jpg')
girl_idle_left = pygame.image.load('girl/girl_idle_left.png')
girl_idle_right = pygame.image.load('girl/girl_idle_right.png')

girl_walk_left_1 = pygame.image.load('girl/girl_walk_left_1.png')
girl_walk_left_2 = pygame.image.load('girl/girl_walk_left_2.png')
girl_walk_right_1 = pygame.image.load('girl/girl_walk_right_1.png')
girl_walk_right_2 = pygame.image.load('girl/girl_walk_right_2.png')

potus_idle = pygame.image.load('POTUS/POTUS (2).png')
potus_creep = pygame.image.load('POTUS/Creepy_POTUS (2).png')
potus_left_up = pygame.image.load('POTUS/POTUS_lup.png')
potus_right_up = pygame.image.load('POTUS/POTUS_rup.png')

diddy_idle = pygame.image.load('Diddy/Diddy.png')
diddy_gun = pygame.image.load('Diddy/Diddy_gun.png')
diddy_left_up = pygame.image.load('Diddy/Diddy_lup.png')
diddy_right_up = pygame.image.load('Diddy/Diddy_rup.png')

megaman_idle_left = pygame.image.load('megaman/megaman_idle_left.png')
megaman_run_left_0 = pygame.image.load('megaman/megaman_run_left_0.png')
megaman_run_left_1 = pygame.image.load('megaman/megaman_run_left_1.png')
megaman_run_left_2 = pygame.image.load('megaman/megaman_run_left_2.png')

megaman_idle_right = pygame.image.load('megaman/megaman_idle_right.png')
megaman_run_right_0 = pygame.image.load('megaman/megaman_run_right_0.png')
megaman_run_right_1 = pygame.image.load('megaman/megaman_run_right_1.png')
megaman_run_right_2 = pygame.image.load('megaman/megaman_run_right_2.png')

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
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
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
        self.flash_time = 100  # Flash interval in milliseconds
        self.visible = True  # To track visibility during flashing

    def adjust_speed(self, is_creepy_active):
        if is_creepy_active:
            self.speed = self.base_speed * 0.5  # Reduce speed by 30%
        else:
            self.speed = self.base_speed  # Reset to normal speed

    def move(self, keys):
        self.walking = False
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx -= 1
            self.last_direction = 'left'
        if keys[pygame.K_RIGHT]:
            dx += 1
            self.last_direction = 'right'
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1

        if dx != 0 or dy != 0:
            self.walking = True
            # Normalize the direction vector
            length = (dx ** 2 + dy ** 2) ** 0.5
            if length != 0:
                dx, dy = dx / length, dy / length

            if self.last_direction == 'left':
                self.image = self.left_frames[self.current_frame]
            else:
                self.image = self.right_frames[self.current_frame]

        self.x += dx * self.speed
        self.y += dy * self.speed

        if not self.walking:
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

        # Update flashing effect
        if self.invincible:
            self.update_flash()

    def take_damage(self, damage):
        if not self.invincible:
            self.health -= damage
            if self.health <= 0:
                self.die()
            else:
                self.invincible = True
                self.invincible_time = pygame.time.get_ticks()
                self.visible = True  # Reset visibility at the start of invincibility

    def die(self):
        print("Character has died.")

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if self.walking:
                self.current_frame = (self.current_frame + 1) % 4

    def update_flash(self):
        now = pygame.time.get_ticks()
        if now - self.invincible_time < self.invincible_duration:
            if (now - self.invincible_time) // self.flash_time % 2 == 0:
                self.visible = False
            else:
                self.visible = True

    def draw(self):
        if self.visible or not self.invincible:
            window.blit(self.image, self.rect.topleft)


character = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

class Monster:
    def __init__(self, x, y, size, idle_image, creepy_image, left_up_image, right_up_image, dialog_text, attack_power=1):
        self.x = x
        self.y = y
        self.size = size
        self.attack_power = attack_power
        self.idle_image = idle_image
        self.creepy_image = creepy_image
        self.image = self.idle_image
        self.rect = self.image.get_rect(center=(x, y))
        self.move_active = True
        self.last_toggle = time.time()
        self.toggle_interval = random.randint(1, 2)
        self.last_animation_change = time.time()
        self.current_frame = 0
        self.animation_frames = [
            pygame.transform.scale(left_up_image, (self.size, self.size)),
            pygame.transform.scale(right_up_image, (self.size, self.size))
        ]
        self.dialog = dialog_text
        self.show_dialog = False
        self.creepy_active = False

    def move_towards_player(self, player, other_monster):
        if (time.time() - self.last_toggle) > self.toggle_interval:
            self.move_active = not self.move_active
            self.last_toggle = time.time()

            if not self.move_active:  # Only decide when the monster goes idle
                if random.random() < 1 and not other_monster.creepy_active:  # 10% chance and ensure other monster is not in creepy state
                    self.image = self.creepy_image
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

            # Adjust direction slightly if too close to the other monster
            if is_too_close(self, other_monster, 50):
                dx += random.choice([-20, 20])
                dy += random.choice([-20, 20])

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
            font = pygame.font.Font(None, 24)
            text = font.render(self.dialog, True, pygame.Color('black'))
            text_rect = text.get_rect()
            padding = 10
            bubble_width = text_rect.width + 2 * padding
            bubble_height = text_rect.height + 2 * padding
            bubble_rect = pygame.Rect(self.rect.centerx - bubble_width / 2, self.rect.top - bubble_height - 10, bubble_width, bubble_height)
            text_rect.center = bubble_rect.center
            pygame.draw.ellipse(window, pygame.Color('white'), bubble_rect)
            pygame.draw.ellipse(window, pygame.Color('black'), bubble_rect, 2)
            tail_width = 15
            tail_height = 20
            tail = [(self.rect.centerx, self.rect.top - 10), 
                    (self.rect.centerx - tail_width / 2, bubble_rect.bottom), 
                    (self.rect.centerx + tail_width / 2, bubble_rect.bottom)]
            pygame.draw.polygon(window, pygame.Color('white'), tail)
            pygame.draw.polygon(window, pygame.Color('black'), tail, 2)
            window.blit(text, text_rect)

    def draw(self):
        window.blit(self.image, self.rect.topleft)

# Function to check distance between two monsters
def is_too_close(monster1, monster2, min_distance=100):
    distance = math.sqrt((monster1.rect.centerx - monster2.rect.centerx) ** 2 + 
                         (monster1.rect.centery - monster2.rect.centery) ** 2)
    return distance < min_distance

# Initialize the first monster
potus = Monster(
    random.randint(0, WINDOW_WIDTH - 30), random.randint(0, WINDOW_HEIGHT - 30), 90,
    pygame.transform.scale(potus_idle, (90, 90)),
    pygame.transform.scale(potus_creep, (90, 90)),
    pygame.transform.scale(potus_left_up, (90, 90)),
    pygame.transform.scale(potus_right_up, (90, 90)),
    "I like to lick... Ice cream."
)

# Initialize the second monster ensuring it doesn't spawn too close to the first one
while True:
    diddy_x = random.randint(0, WINDOW_WIDTH - 30)
    diddy_y = random.randint(0, WINDOW_HEIGHT - 30)
    diddy = Monster(
        diddy_x, diddy_y, 90,
        pygame.transform.scale(diddy_idle, (90, 90)),
        pygame.transform.scale(diddy_gun, (90, 90)),
        pygame.transform.scale(diddy_left_up, (90, 90)),
        pygame.transform.scale(diddy_right_up, (90, 90)),
        "Say! You're a friend of Biber?"
    )
    if not is_too_close(potus, diddy):
        break

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
    character.adjust_speed(potus.creepy_active or diddy.creepy_active)  # Adjust speed based on monster state
    character.move(keys)
    
    if character.health > 0:
        character.draw()
        potus.move_towards_player(character, diddy)
        potus.draw()
        potus.draw_dialog(window)

        diddy.move_towards_player(character, potus)
        diddy.draw()
        diddy.draw_dialog(window)
        
        # Calculate distance between the monsters and the character
        distance_potus = math.sqrt((potus.rect.centerx - character.rect.centerx) ** 2 + 
                                   (potus.rect.centery - character.rect.centery) ** 2)
        distance_diddy = math.sqrt((diddy.rect.centerx - character.rect.centerx) ** 2 + 
                                   (diddy.rect.centery - character.rect.centery) ** 2)
        
        # If distance is less than a certain value, the character takes damage
        if distance_potus < 30:  # Adjust this value as needed
            potus.attack(character)
            print(f"Character health: {character.health}")
        if distance_diddy < 30:  # Adjust this value as needed
            diddy.attack(character)
            print(f"Character health: {character.health}")
    else:
        window.fill(BLACK)
        font = pygame.font.Font(pygame.font.get_default_font(), 74)
        text = font.render("FAILED", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

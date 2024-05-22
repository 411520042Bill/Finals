import pygame
import random
import math
import time
from chatbot import get_chatbot_response

# Initialize Pygame
pygame.init()

# Initialize cursor variables
cursor_visible = True
cursor_blink_time = pygame.time.get_ticks()

# Constants for the game window
WINDOW_WIDTH = 575  # Increased width
WINDOW_HEIGHT = 505  # Increased height
FPS = 60  # Frames per second

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel Style Game")

# Define colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
CHAT_BG_COLOR = (204, 255, 204)  # Light green color for chat history section

# Load images
white_tile = pygame.image.load('_white_tile1.jpg')
lpink_tile = pygame.image.load('light_pink_tile1.jpg')
dpink_tile = pygame.image.load('dark_pink_tile1.jpg')
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
heart = pygame.image.load('heart.png')
heart_grey = pygame.image.load('heart_grey.png')
pause_icon = pygame.image.load('pause_icon.png')
resume_icon = pygame.image.load('resume_icon.png')

# Resize the icons
pause_icon = pygame.transform.scale(pause_icon, (60, 60))
resume_icon = pygame.transform.scale(resume_icon, (60, 60))

# Define new dimensions for the character image
char_width, char_height = 216, 108
walk_width, walk_height = 216, 108
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
        self.x, self.y = x, y
        self.base_speed, self.speed = speed, speed
        self.size, self.health = size, health
        self.image = girl_idle_left
        self.rect = self.image.get_rect(center=(x, y))
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.last_direction = 'left'
        self.left_frames = [girl_walk_left_1, girl_walk_left_2] * 2
        self.right_frames = [girl_walk_right_1, girl_walk_right_2] * 2
        self.current_frame, self.walking = 0, False
        self.invincible, self.invincible_time = False, 0
        self.invincible_duration, self.flash_time = 3000, 100
        self.visible = True
        self.alive = Ture
        self.heart_image = pygame.transform.scale(heart, (30, 30))
        self.heart_grey_image = pygame.transform.scale(heart_grey, (30, 30))

    def adjust_speed(self, is_creepy_active):
        self.speed = self.base_speed * 0.5 if is_creepy_active else self.base_speed

    def move(self, keys):
        self.walking, dx, dy = False, 0, 0
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
            length = (dx ** 2 + dy ** 2) ** 0.5
            dx, dy = dx / length, dy / length
            self.image = self.left_frames[self.current_frame] if self.last_direction == 'left' else self.right_frames[self.current_frame]
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.size * 2))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.size * 2))
        self.rect.center = (self.x, self.y)
        if not self.walking:
            self.image = girl_idle_left if self.last_direction == 'left' else girl_idle_right
        self.update_animation()
        if self.invincible and pygame.time.get_ticks() - self.invincible_time > self.invincible_duration:
            self.invincible = False
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
                self.visible = True

    def die(self):
        self.alive = False
        print("Character has died.")

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if self.walking:
                self.current_frame = (self.current_frame + 1) % 4

    def update_flash(self):
        now = pygame.time.get_ticks()
        self.visible = (now - self.invincible_time) // self.flash_time % 2 == 1

    def draw(self):
        if self.visible or not self.invincible:
            window.blit(self.image, self.rect.topleft)
        self.draw_health()

    def draw_health(self):
        for i in range(3):
            if i < self.health:
                window.blit(self.heart_image, (455 + i * 40, 10))
            else:
                window.blit(self.heart_grey_image, (455 + i * 40, 10))

character = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

class Monster:
    def __init__(self, x, y, size, idle_image, creepy_image, left_up_image, right_up_image, dialog_text, attack_power=1):
        self.x, self.y, self.size, self.attack_power = x, y, size, attack_power
        self.idle_image, self.creepy_image = idle_image, creepy_image
        self.image = self.idle_image
        self.rect = self.image.get_rect(center=(x, y))
        self.move_active = True
        self.last_toggle = time.time()
        self.toggle_interval = random.randint(1, 2)
        self.last_animation_change = time.time()
        self.current_frame = 0
        self.animation_frames = [pygame.transform.scale(left_up_image, (self.size, self.size)),
                                 pygame.transform.scale(right_up_image, (self.size, self.size))]
        self.dialog, self.show_dialog, self.creepy_active = dialog_text, False, False

    def move_towards_player(self, player, other_monster):
        if time.time() - self.last_toggle > self.toggle_interval:
            self.move_active = not self.move_active
            self.last_toggle = time.time()
            if not self.move_active and random.random() < 0.1 and not other_monster.creepy_active:
                self.image = self.creepy_image
                self.show_dialog = True
                self.toggle_interval = 3
                self.creepy_active = True
            else:
                self.image = self.idle_image
                self.show_dialog = False
                self.toggle_interval = random.randint(1, 2)
                self.creepy_active = False
        if self.move_active:
            if time.time() - self.last_animation_change > 0.1:
                self.current_frame = (self.current_frame + 1) % 2
                self.image = self.animation_frames[self.current_frame]
                self.last_animation_change = time.time()
            dx, dy = player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery
            distance = math.hypot(dx, dy)
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
            self.show_dialog = False

    def attack(self, character):
        character.take_damage(self.attack_power)

    def draw_dialog(self, window):
        if self.show_dialog:
            font = pygame.font.Font(None, 24)
            text = font.render(self.dialog, True, pygame.Color('black'))
            text_rect = text.get_rect()
            padding = 10
            bubble_rect = pygame.Rect(self.rect.centerx - (text_rect.width + 2 * padding) / 2, 
                                      self.rect.top - (text_rect.height + 2 * padding) - 10, 
                                      text_rect.width + 2 * padding, text_rect.height + 2 * padding)
            text_rect.center = bubble_rect.center
            pygame.draw.ellipse(window, pygame.Color('white'), bubble_rect)
            pygame.draw.ellipse(window, pygame.Color('black'), bubble_rect, 2)
            tail = [(self.rect.centerx, self.rect.top - 10), 
                    (self.rect.centerx - 7.5, bubble_rect.bottom), 
                    (self.rect.centerx + 7.5, bubble_rect.bottom)]
            pygame.draw.polygon(window, pygame.Color('white'), tail)
            pygame.draw.polygon(window, pygame.Color('black'), tail, 2)
            window.blit(text, text_rect)

    def draw(self):
        window.blit(self.image, self.rect.topleft)

def is_too_close(monster1, monster2, min_distance=100):
    distance = math.sqrt((monster1.rect.centerx - monster2.rect.centerx) ** 2 + 
                         (monster1.rect.centery - monster2.rect.centery) ** 2)
    return distance < min_distance

potus = Monster(random.randint(0, WINDOW_WIDTH - 30), random.randint(0, WINDOW_HEIGHT - 30), 90,
                pygame.transform.scale(potus_idle, (90, 90)),
                pygame.transform.scale(potus_creep, (90, 90)),
                pygame.transform.scale(potus_left_up, (90, 90)),
                pygame.transform.scale(potus_right_up, (90, 90)),
                "I like to lick... Ice cream.")

while True:
    diddy_x, diddy_y = random.randint(0, WINDOW_WIDTH - 30), random.randint(0, WINDOW_HEIGHT - 30)
    diddy = Monster(diddy_x, diddy_y, 90,
                    pygame.transform.scale(diddy_idle, (90, 90)),
                    pygame.transform.scale(diddy_gun, (90, 90)),
                    pygame.transform.scale(diddy_left_up, (90, 90)),
                    pygame.transform.scale(diddy_right_up, (90, 90)),
                    "Say! You're a friend of Biber?")
    if not is_too_close(potus, diddy):
        break

# Initialize pause state
paused, countdown, countdown_start_ticks = False, 0, 0
scroll_y, scroll_speed, max_scroll = 0, 10, 0
font_small = pygame.font.Font(None, 20)
input_box = pygame.Rect(WINDOW_WIDTH // 2 - 228, WINDOW_HEIGHT // 2 + 100, 450, 32)  # Wider input box
chat_history_rect = pygame.Rect(WINDOW_WIDTH // 2 - 228, WINDOW_HEIGHT // 2 - 200, 450, 280)  # Wider chat history
chat_history, input_text, input_active = [], '', False
font = pygame.font.Font(None, 32)
input_font = pygame.font.Font(None, 24)  # Smaller font for input bar


def draw_pause_button():
    if character.alive:
        icon = resume_icon if paused else pause_icon
        window.blit(icon, (-5, -5))
        return pygame.Rect(10, 10, icon.get_width(), icon.get_height())

def draw_pause_screen():
    global scroll_y, max_scroll
    window.fill((189, 252, 201))
    text = pygame.font.Font(None, 74).render("Paused", True, BLACK)
    window.blit(text, text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 150)))
    pygame.draw.rect(window, WHITE, input_box)
    pygame.draw.rect(window, CHAT_BG_COLOR, chat_history_rect)
    chat_surface = pygame.Surface((chat_history_rect.width, chat_history_rect.height))
    chat_surface.fill(CHAT_BG_COLOR)
    y_offset = -scroll_y

    content_height = 0
    for user, bot in chat_history:
        user_text_lines = wrap_text(f'You: {user}', font_small, chat_history_rect.width - 20)
        bot_text_lines = wrap_text(f'Bot: {bot}', font_small, chat_history_rect.width - 20)
        for line in user_text_lines + bot_text_lines:
            content_height += font_small.size(line)[1] * 1.5
        content_height += 20

    max_scroll = max(0, content_height - chat_history_rect.height)
    y_offset = -scroll_y

    for i, (user, bot) in enumerate(reversed(chat_history)):
        user_text_lines = wrap_text(f'You: {user}', font_small, chat_history_rect.width - 20)
        bot_text_lines = wrap_text(f'Bot: {bot}', font_small, chat_history_rect.width - 20)
        for line in user_text_lines:
            user_text = font_small.render(line, True, BLACK)
            user_text_rect = user_text.get_rect(topleft=(10, y_offset))
            chat_surface.blit(user_text, user_text_rect)
            y_offset += user_text.get_height()
        y_offset += 5
        for line in bot_text_lines:
            bot_text = font_small.render(line, True, BLACK)
            bot_text_rect = bot_text.get_rect(topleft=(10, y_offset))
            chat_surface.blit(bot_text, bot_text_rect)
            y_offset += bot_text.get_height()
        y_offset += 20

    window.blit(chat_surface, chat_history_rect.topleft)

    if max_scroll > 0:
        scrollbar_height = chat_history_rect.height * chat_history_rect.height / content_height
        scrollbar_rect = pygame.Rect(chat_history_rect.right + 5, chat_history_rect.top + (scroll_y * chat_history_rect.height / content_height), 15, scrollbar_height)
        pygame.draw.rect(window, BLACK, scrollbar_rect)

    txt_surface = input_font.render(input_text, True, BLACK)
    window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    if input_active:
        cursor = pygame.Rect(input_box.x + 5 + input_font.size(input_text)[0], input_box.y + 5, 2, input_font.size(input_text)[1])
        if cursor_visible:
            pygame.draw.rect(window, BLACK, cursor)


def wrap_text(text, font, max_width):
    """Wrap text into a list of lines that fit within max_width."""
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines

def draw_countdown(number):
    text = pygame.font.Font(None, 74).render(str(number), True, BLACK)
    window.blit(text, text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)))


running = True
clock = pygame.time.Clock()
pause_rect = draw_pause_button()

while running:
    window.fill(WHITE)
    draw_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if pause_rect.collidepoint(mouse_pos):
                if paused:
                    paused, countdown = False, 3
                    countdown_start_ticks = pygame.time.get_ticks()
                else:
                    paused = True
            elif paused and input_box.collidepoint(mouse_pos):
                input_active = True
        elif event.type == pygame.MOUSEWHEEL:
            scroll_y = min(max_scroll, max(0, scroll_y - event.y * scroll_speed))
        elif event.type == pygame.KEYDOWN:
            if paused and input_active:
                if event.key == pygame.K_RETURN:
                    if input_text:
                        chat_history.insert(0, (input_text, get_chatbot_response(input_text)))  # Use chatbot response
                        input_text, input_active = '', False
                        max_scroll = max(0, len(chat_history) * 30 - chat_history_rect.height)
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    if pygame.time.get_ticks() - cursor_blink_time > 500:
        cursor_visible = not cursor_visible
        cursor_blink_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    if not paused:
        if countdown > 0:
            elapsed_time = (pygame.time.get_ticks() - countdown_start_ticks) // 1000
            draw_countdown(countdown - elapsed_time)
            if elapsed_time >= 3:
                countdown = 0
        else:
            character.adjust_speed(potus.creepy_active or diddy.creepy_active)
            character.move(keys)
            if character.health > 0:
                character.draw()
                potus.move_towards_player(character, diddy)
                potus.draw()
                potus.draw_dialog(window)
                diddy.move_towards_player(character, potus)
                diddy.draw()
                diddy.draw_dialog(window)
                if math.sqrt((potus.rect.centerx - character.rect.centerx) ** 2 + (potus.rect.centery - character.rect.centery) ** 2) < 30:
                    potus.attack(character)
                    print(f"Character health: {character.health}")
                if math.sqrt((diddy.rect.centerx - character.rect.centerx) ** 2 + (diddy.rect.centery - character.rect.centery) ** 2) < 30:
                    diddy.attack(character)
                    print(f"Character health: {character.health}")
            else:
                window.fill(BLACK)
                text = pygame.font.Font(pygame.font.get_default_font(), 74).render("FAILED", True, (255, 0, 0))
                window.blit(text, text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)))
    else:
        draw_pause_screen()
    pause_rect = draw_pause_button()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

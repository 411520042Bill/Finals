import pygame
import random
import math
import time
from utils import is_within_boundary, is_colliding, is_too_close, find_valid_spawn_position, astar_pathfinding

class Monster:
    def __init__(self, x, y, size, idle_image, creepy_image, left_up_image, right_up_image, dialog_text, attack_power=1, attack_range=50):
        self.x, self.y, self.size, self.attack_power = x, y, size, attack_power
        self.attack_range = attack_range  # Added attack range
        self.idle_image = pygame.transform.scale(idle_image, (self.size, self.size))
        self.creepy_image = pygame.transform.scale(creepy_image, (self.size, self.size))
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
        self.dialog, self.show_dialog, self.creepy_active = dialog_text, False, False
        self.path = []

    def move_towards_player(self, player, other_monster, layout, tile_size):
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

            if not self.path:
                self.path = astar_pathfinding(layout, (self.rect.centerx, self.rect.centery), player.rect.center, tile_size)

            if self.path:
                next_step = self.path[0]
                dx, dy = next_step[0] - self.rect.centerx, next_step[1] - self.rect.centery
                distance = math.hypot(dx, dy)
                if distance < 2:
                    self.path.pop(0)
                if distance != 0:
                    dx, dy = dx / distance, dy / distance
                new_rect = self.rect.copy()
                new_rect.centerx += dx * 2.5
                new_rect.centery += dy * 2.5
                tile_x = int(new_rect.centerx // tile_size)
                tile_y = int(new_rect.centery // tile_size)
                if is_within_boundary(tile_x, tile_y, layout) and not is_colliding(new_rect, layout, tile_size):
                    self.rect = new_rect

            if math.hypot(self.rect.centerx - player.rect.centerx, self.rect.centery - player.rect.centery) < self.attack_range:
                self.attack(player)
            self.show_dialog = False

    def attack(self, character):
        distance = math.hypot(self.rect.centerx - character.rect.centerx, self.rect.centery - character.rect.centery)
        if distance < self.attack_range:
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

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

def spawn_monster(monster_type, layout, tile_size):
    if monster_type == 'POTUS':
        return Monster(*find_valid_spawn_position(layout, tile_size), 90,
                       pygame.image.load('POTUS/POTUS (2).png'),
                       pygame.image.load('POTUS/Creepy_POTUS (2).png'),
                       pygame.image.load('POTUS/POTUS_lup.png'),
                       pygame.image.load('POTUS/POTUS_rup.png'),
                       "I like to lick... Ice cream.")
    elif monster_type == 'Diddy':
        return Monster(*find_valid_spawn_position(layout, tile_size), 90,
                       pygame.image.load('Diddy/Diddy.png'),
                       pygame.image.load('Diddy/Diddy_gun.png'),
                       pygame.image.load('Diddy/Diddy_lup.png'),
                       pygame.image.load('Diddy/Diddy_rup.png'),
                       "Say! You're a friend of Biber?")

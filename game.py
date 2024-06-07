import pygame
import random
import time
from character import Character
from monster import spawn_monster
from utils import (
    draw_map, draw_pause_button, draw_pause_screen,
    draw_countdown, is_within_boundary, is_colliding,
    check_boost, spawn_random_booster
)
from chatbot import get_chatbot_response

class Game:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pixel Style Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.countdown = 3
        self.countdown_start_ticks = 0
        self.scroll_y = 0
        self.scroll_speed = 10
        self.max_scroll = 0
        self.cursor_visible = True
        self.cursor_blink_time = pygame.time.get_ticks()
        self.last_booster_spawn_time = pygame.time.get_ticks()
        self.booster_spawn_interval = 8000
        self.font_small = pygame.font.Font(None, 20)
        self.input_box = pygame.Rect(self.width // 2 - 228, self.height // 2 + 100, 450, 32)
        self.chat_history_rect = pygame.Rect(self.width // 2 - 228, self.height // 2 - 200, 450, 280)
        self.chat_history = []
        self.input_text = ''
        self.input_active = False
        self.font = pygame.font.Font(None, 32)
        self.input_font = pygame.font.Font(None, 24)

        # Load images and other resources
        self.load_resources()

        # Initialize character and monsters
        self.character = Character(self.width // 2, self.height // 2)
        self.potus = spawn_monster('POTUS', self.layout, self.tile_size)
        self.diddy = spawn_monster('Diddy', self.layout, self.tile_size)

    def load_resources(self):
        # Load images and other resources here
        self.white_tile = pygame.image.load('_white_tile1.jpg')
        self.lpink_tile = pygame.image.load('light_pink_tile1.jpg')
        self.dpink_tile = pygame.image.load('dark_pink_tile1.jpg')
        self.pause_icon = pygame.image.load('pause_icon.png')
        self.resume_icon = pygame.image.load('resume_icon.png')
        self.desk = pygame.image.load('prop/desk.png')
        self.chair = pygame.image.load('new_chair_resized.png')
        self.tile_size = self.white_tile.get_width()
        self.desk = pygame.transform.scale(self.desk, (self.tile_size, 3 * self.tile_size))
        self.pause_icon = pygame.transform.scale(self.pause_icon, (60, 60))
        self.resume_icon = pygame.transform.scale(self.resume_icon, (60, 60))

        # Define the layout of the area
        self.layout = [
            # Shelf 10-17
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 7, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 7, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 7, 0, 7, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 7, 0, 7, 0, 2, 0, 3],
            [3, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 3],
            [3, 0, 2, 7, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 7, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 3],
            [3, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 3],
            [3, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if self.pause_rect.collidepoint(mouse_pos):
                    if self.paused:
                        self.paused, self.countdown = False, 3
                        self.countdown_start_ticks = pygame.time.get_ticks()
                    else:
                        self.paused = True
                elif self.paused and self.input_box.collidepoint(mouse_pos):
                    self.input_active = True
            elif event.type == pygame.MOUSEWHEEL:
                self.scroll_y = min(self.max_scroll, max(0, self.scroll_y - event.y * self.scroll_speed))
            elif event.type == pygame.KEYDOWN:
                if self.paused and self.input_active:
                    if event.key == pygame.K_RETURN:
                        if self.input_text:
                            self.chat_history.insert(0, (self.input_text, get_chatbot_response(self.input_text)))
                            self.input_text, self.input_active = '', False
                            self.max_scroll = max(0, len(self.chat_history) * 30 - self.chat_history_rect.height)
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

    def update(self):
        if pygame.time.get_ticks() - self.cursor_blink_time > 500:
            self.cursor_visible = not self.cursor_visible
            self.cursor_blink_time = pygame.time.get_ticks()

        if not self.paused:
            if self.countdown > 0:
                elapsed_time = (pygame.time.get_ticks() - self.countdown_start_ticks) // 1000
                if elapsed_time >= 1:
                    self.countdown -= 1
                    self.countdown_start_ticks = pygame.time.get_ticks()
            else:
                self.character.adjust_speed(self.potus.creepy_active or self.diddy.creepy_active)
                keys = pygame.key.get_pressed()
                self.character.move(keys, self.layout, self.tile_size, self.width, self.height)
                check_boost(self.character, self.layout, self.tile_size)
                current_time = pygame.time.get_ticks()
                if current_time - self.last_booster_spawn_time > self.booster_spawn_interval:
                    spawn_random_booster(self.layout)
                    self.last_booster_spawn_time = current_time
                if self.character.health > 0:
                    self.potus.move_towards_player(self.character, self.diddy, self.layout, self.tile_size)
                    self.diddy.move_towards_player(self.character, self.potus, self.layout, self.tile_size)
                    if self.character.rect.colliderect(self.potus.rect):
                        self.potus.attack(self.character)
                    if self.character.rect.colliderect(self.diddy.rect):
                        self.diddy.attack(self.character)

    def draw(self):
        self.window.fill((255, 255, 255))
        draw_map(self.window, self.layout, self.white_tile, self.lpink_tile, self.dpink_tile, self.desk, self.chair, self.tile_size)
        if not self.paused:
            if self.countdown > 0:
                draw_countdown(self.window, self.countdown)
            else:
                if self.character.health > 0:
                    self.character.draw(self.window)
                    self.potus.draw(self.window)
                    self.potus.draw_dialog(self.window)
                    self.diddy.draw(self.window)
                    self.diddy.draw_dialog(self.window)
                else:
                    self.window.fill((0, 0, 0))
                    text = pygame.font.Font(pygame.font.get_default_font(), 74).render("FAILED", True, (255, 0, 0))
                    self.window.blit(text, text.get_rect(center=(self.width // 2, self.height // 2)))
        else:
            self.max_scroll = draw_pause_screen(self.window, self.chat_history, self.input_box, self.chat_history_rect, self.input_font, self.input_text, self.input_active, self.cursor_visible, self.scroll_y, self.max_scroll, self.font_small)
        self.pause_rect = draw_pause_button(self.window, self.character, self.paused, self.resume_icon, self.pause_icon)
        pygame.display.flip()

    def run(self):
        self.countdown_start_ticks = pygame.time.get_ticks()  # Start the countdown timer when the game starts
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

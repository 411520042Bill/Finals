import pygame
from utils import is_colliding, is_within_boundary

class Character:
    def __init__(self, x, y, width=216, height=108, speed=3, size=30, health=3):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.base_speed, self.speed = speed, speed
        self.size, self.health = size, health
        self.image = pygame.image.load('girl/girl_idle_left.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Scale the character image
        self.rect = self.image.get_rect(center=(x, y))
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.last_direction = 'left'
        self.left_frames = [pygame.image.load('girl/girl_walk_left_1.png'), pygame.image.load('girl/girl_walk_left_2.png')] * 2
        self.right_frames = [pygame.image.load('girl/girl_walk_right_1.png'), pygame.image.load('girl/girl_walk_right_2.png')] * 2
        self.left_frames = [pygame.transform.scale(frame, (self.width, self.height)) for frame in self.left_frames]
        self.right_frames = [pygame.transform.scale(frame, (self.width, self.height)) for frame in self.right_frames]
        self.current_frame, self.walking = 0, False
        self.invincible, self.invincible_time = False, 0
        self.invincible_duration, self.flash_time = 3000, 100
        self.visible = True
        self.alive = True
        self.heart_image = pygame.transform.scale(pygame.image.load('prop/heart.png'), (30, 30))
        self.heart_grey_image = pygame.transform.scale(pygame.image.load('prop/heart_grey.png'), (30, 30))

    def adjust_speed(self, is_creepy_active):
        self.speed = self.base_speed * 0.5 if is_creepy_active else self.base_speed

    def move(self, keys, layout, tile_size, window_width, window_height):
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

        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        new_rect = self.rect.copy()
        new_rect.center = (new_x, new_y)

        collision_box = pygame.Rect(new_rect.centerx - tile_size // 2, new_rect.centery - tile_size // 2, tile_size, tile_size)
        tile_x = int(new_rect.centerx // tile_size)
        tile_y = int(new_rect.centery // tile_size)

        if is_within_boundary(tile_x, tile_y, layout) and not is_colliding(collision_box, layout, tile_size):
            self.x, self.y = new_x, new_y

        self.x = max(0, min(self.x, window_width - self.size * 2))
        self.y = max(0, min(self.y, window_height - self.size * 2))
        self.rect.center = (self.x, self.y)

        if not self.walking:
            self.image = pygame.image.load('girl/girl_idle_left.png') if self.last_direction == 'left' else pygame.image.load('girl/girl_idle_right.png')
            self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Scale the idle image

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

    def draw(self, window):
        if self.visible or not self.invincible:
            window.blit(self.image, self.rect.topleft)
        self.draw_health(window)

    def draw_health(self, window):
        for i in range(3):
            if i < self.health:
                window.blit(self.heart_image, (455 + i * 40, 10))
            else:
                window.blit(self.heart_grey_image, (455 + i * 40, 10))

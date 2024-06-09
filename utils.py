import pygame
import random
import math
import heapq

def draw_map(window, layout, white_tile, lpink_tile, dpink_tile, desk, chair, tile_size):
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile == 0:
                window.blit(white_tile, (x * tile_size, y * tile_size))
            elif tile == 2:
                window.blit(lpink_tile, (x * tile_size, y * tile_size))
            elif tile == 3:
                window.blit(dpink_tile, (x * tile_size, y * tile_size))
            elif tile == 4:
                desk_x = x * tile_size
                desk_y = y * tile_size - desk.get_height() + tile_size
                window.blit(desk, (desk_x, desk_y))
            elif tile == 7:
                window.blit(chair, (x * tile_size, y * tile_size))

def draw_pause_button(window, character, paused, resume_icon, pause_icon):
    if character.alive:
        icon = resume_icon if paused else pause_icon
        window.blit(icon, (-5, -5))
        return pygame.Rect(10, 10, icon.get_width(), icon.get_height())

def draw_pause_screen(window, chat_history, input_box, chat_history_rect, input_font, input_text, input_active, cursor_visible, scroll_y, max_scroll, font_small):
    window.fill((189, 252, 201))
    text = pygame.font.Font(None, 74).render("Paused", True, (0, 0, 0))
    window.blit(text, text.get_rect(center=(window.get_width() // 2, window.get_height() // 2 - 150)))
    pygame.draw.rect(window, (255, 255, 255), input_box)
    pygame.draw.rect(window, (204, 255, 204), chat_history_rect)
    chat_surface = pygame.Surface((chat_history_rect.width, chat_history_rect.height))
    chat_surface.fill((204, 255, 204))
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
            user_text = font_small.render(line, True, (0, 0, 0))
            user_text_rect = user_text.get_rect(topleft=(10, y_offset))
            chat_surface.blit(user_text, user_text_rect)
            y_offset += user_text.get_height()
        y_offset += 5
        for line in bot_text_lines:
            bot_text = font_small.render(line, True, (0, 0, 0))
            bot_text_rect = bot_text.get_rect(topleft=(10, y_offset))
            chat_surface.blit(bot_text, bot_text_rect)
            y_offset += bot_text.get_height()
        y_offset += 20

    window.blit(chat_surface, chat_history_rect.topleft)

    if max_scroll > 0:
        scrollbar_height = chat_history_rect.height * chat_history_rect.height / content_height
        scrollbar_rect = pygame.Rect(chat_history_rect.right + 5, chat_history_rect.top + (scroll_y * chat_history_rect.height / content_height), 15, scrollbar_height)
        pygame.draw.rect(window, (0, 0, 0), scrollbar_rect)

    txt_surface = input_font.render(input_text, True, (0, 0, 0))
    window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    if input_active and cursor_visible:
        cursor = pygame.Rect(input_box.x + 5 + input_font.size(input_text)[0], input_box.y + 5, 2, input_font.size(input_text)[1])
        pygame.draw.rect(window, (0, 0, 0), cursor)

    return max_scroll  # Return the updated max_scroll value

def draw_countdown(window, number):
    text = pygame.font.Font(None, 74).render(str(number), True, (0, 0, 0))
    window.blit(text, text.get_rect(center=(window.get_width() // 2, window.get_height() // 2)))

def wrap_text(text, font, max_width):
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

def is_within_boundary(x, y, layout):
    if 0 <= y < len(layout) and 0 <= x < len(layout[y]) and layout[y][x] != 3:
        return True
    return False

def is_colliding(rect, layout, tile_size):
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile in (3, 4, 5, 6, 7):  # Only check for specific obstacle tiles
                obstacle_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                # Adjusted smaller collision box
                collision_box = pygame.Rect(rect.centerx - tile_size // 2, rect.centery - tile_size // 2, tile_size, tile_size)
                if collision_box.colliderect(obstacle_rect):
                    print(f"Collision detected at: {x}, {y}")  # Debugging line
                    return True
    return False


def is_too_close(monster1, monster2, min_distance=100):
    distance = math.sqrt((monster1.rect.centerx - monster2.rect.centerx) ** 2 +
                         (monster1.rect.centery - monster2.rect.centery) ** 2)
    return distance < min_distance

def find_valid_spawn_position(layout, tile_size):
    valid_positions = []
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile != 3:
                valid_positions.append((x * tile_size, y * tile_size))
    return random.choice(valid_positions)

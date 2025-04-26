import pygame
import random

# Definindo o personagem principal
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Função para desenhar o personagem


def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

# Função para movimentação do personagem


def move_player(keys, x, y):
    if keys[pygame.K_LEFT]:
        x -= player_speed
    if keys[pygame.K_RIGHT]:
        x += player_speed
    if keys[pygame.K_UP]:
        y -= player_speed
    if keys[pygame.K_DOWN]:
        y += player_speed
    return x, y

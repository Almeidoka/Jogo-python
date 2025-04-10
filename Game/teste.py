import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Binding of Isaac - Simplificado")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Definindo o personagem principal
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Função para desenhar o personagem
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

# Função para desenhar inimigos
def draw_enemy(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)

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

# Função principal do jogo
def game_loop():
    player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    enemies = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(5)]

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player_x, player_y = move_player(keys, player_x, player_y)

        # Desenhando o jogador e os inimigos
        draw_player(player_x, player_y)
        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Rodando o jogo
game_loop()

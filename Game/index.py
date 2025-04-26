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

# Função para desenhar inimigos
def draw_enemy(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)


# Função principal do jogo
def game_loop():
    # player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    enemies = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(5)]

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        

        # keys = pygame.key.get_pressed()
        # player_x, player_y = move_player(keys, player_x, player_y)

        # # Desenhando o jogador e os inimigos
        # draw_player(player_x, player_y)
         for enemy in enemies:
             draw_enemy(enemy[0], enemy[1])

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Rodando o jogo
game_loop()

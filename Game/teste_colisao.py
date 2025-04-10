def check_collision(player_x, player_y, enemy_x, enemy_y):
    # Checando colisão com um círculo (inimigo)
    if (player_x < enemy_x + 20 and player_x + player_width > enemy_x - 20 and
            player_y < enemy_y + 20 and player_y + player_height > enemy_y - 20):
        return True
    return False


/// 
movimentação do enimigo 


def move_enemy(enemy):
    direction = random.choice(['left', 'right', 'up', 'down'])
    if direction == 'left':
        enemy[0] -= 2
    elif direction == 'right':
        enemy[0] += 2
    elif direction == 'up':
        enemy[1] -= 2
    elif direction == 'down':
        enemy[1] += 2
    return enemy

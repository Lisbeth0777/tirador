# main.py
import pygame
from player import Player
from enemy import Enemy
from utils import show_scores, show_lives, show_game_over
from settings import WIDTH, HEIGHT, FPS, WHITE, RED, LEVELS

# Inicializar Pygame
pygame.init()

def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de Tirador")
    clock = pygame.time.Clock()

    # Cargar imágenes de fondo
    backgrounds = {
        1: pygame.image.load(LEVELS[1]["background"]),
        2: pygame.image.load(LEVELS[2]["background"]),
        3: pygame.image.load(LEVELS[3]["background"])
    }
    current_background = backgrounds[1]  # Fondo inicial

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Jugador 1 (Blanco, controla con flechas y dispara con Enter)
    player1 = Player(x=WIDTH // 4, y=HEIGHT - 50, move_left=pygame.K_LEFT, move_right=pygame.K_RIGHT, shoot_key=pygame.K_RETURN, color=WHITE)
    all_sprites.add(player1)

    # Jugador 2 (Rojo, controla con A, D y dispara con Espacio)
    player2 = Player(x=3 * WIDTH // 4, y=HEIGHT - 50, move_left=pygame.K_a, move_right=pygame.K_d, shoot_key=pygame.K_SPACE, color=RED)
    all_sprites.add(player2)

    # Crear enemigos iniciales
    enemy_speed = LEVELS[1]["enemy_speed"]  # Velocidad de los enemigos al iniciar
    for i in range(5):
        enemy = Enemy(speed=enemy_speed)  # Iniciar enemigos con la velocidad del nivel 1
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Variables del juego
    score1 = 0  # Puntaje del jugador 1
    score2 = 0  # Puntaje del jugador 2
    running = True
    game_over = False
    current_level = 1  # Nivel inicial

    # Bucle principal del juego
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                # Jugador 1 dispara con Enter
                if event.key == player1.shoot_key:
                    bullet = player1.fire()
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                # Jugador 2 dispara con Espacio
                elif event.key == player2.shoot_key:
                    bullet = player2.fire()
                    all_sprites.add(bullet)
                    bullets.add(bullet)
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    run_game()  # Reiniciar el juego
                    return

        if not game_over:
            # Actualizar sprites
            all_sprites.update()

            # Colisiones entre balas y enemigos
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                if hit.rect.centerx < WIDTH // 2:  # Enemigos a la izquierda (Jugador 2)
                    score2 += 1
                else:  # Enemigos a la derecha (Jugador 1)
                    score1 += 1
                # Crear nuevo enemigo con la velocidad actual
                enemy = Enemy(speed=enemy_speed)
                all_sprites.add(enemy)
                enemies.add(enemy)

            # Colisiones entre los jugadores y los enemigos
            player1_hits = pygame.sprite.spritecollide(player1, enemies, False)
            player2_hits = pygame.sprite.spritecollide(player2, enemies, False)

            if player1_hits:
                player1.lose_life()
                if player1.lives == 0:
                    game_over = True  # Jugador 1 ha perdido todas sus vidas

            if player2_hits:
                player2.lose_life()
                if player2.lives == 0:
                    game_over = True  # Jugador 2 ha perdido todas sus vidas

            # Verificar si el puntaje alcanza el siguiente nivel
            total_score = score1 + score2
            for level, level_data in LEVELS.items():
                if total_score >= level_data["score_threshold"] and level > current_level:
                    current_level = level
                    current_background = backgrounds[level]  # Cambiar el fondo
                    enemy_speed = level_data["enemy_speed"]  # Cambiar la velocidad de los enemigos

        # Dibujar en pantalla el fondo y sprites
        screen.blit(current_background, (0, 0))
        all_sprites.draw(screen)
        show_scores(screen, score1, score2)  # Mostrar los puntajes
        show_lives(screen, player1.lives, player2.lives)  # Mostrar las vidas restantes

        # Si el jugador ha perdido, mostrar el mensaje de "Has perdido"
        if game_over:
            button_rect = show_game_over(screen, score1, score2)  # Mostrar mensaje y botón

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(FPS)

    pygame.quit()

# Iniciar el juego
run_game()

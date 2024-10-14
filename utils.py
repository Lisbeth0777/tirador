import pygame
from settings import WHITE, WIDTH

# Mostrar el puntaje de ambos jugadores
def show_scores(screen, score1, score2):
    font = pygame.font.Font(None, 36)
    text1 = font.render(f"Jugador 1 (Blanco): {score1}", True, WHITE)
    text2 = font.render(f"Jugador 2 (Rojo): {score2}", True, WHITE)
    
    # Mostrar los puntajes en diferentes posiciones
    screen.blit(text1, (10, 10))  # Jugador 1 a la izquierda
    screen.blit(text2, (WIDTH - 300, 10))  # Jugador 2 a la derecha

# Mostrar las vidas de ambos jugadores
def show_lives(screen, lives1, lives2):
    font = pygame.font.Font(None, 36)
    lives_text1 = font.render(f"Vidas Jugador 1: {lives1}", True, WHITE)
    lives_text2 = font.render(f"Vidas Jugador 2: {lives2}", True, WHITE)
    
    # Mostrar las vidas en diferentes posiciones
    screen.blit(lives_text1, (10, 50))  # Jugador 1 a la izquierda
    screen.blit(lives_text2, (WIDTH - 300, 50))  # Jugador 2 a la derecha

# Mostrar mensaje de "Has perdido" y el botón "Jugar de nuevo"
def show_game_over(screen, score1, score2):
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("¡Has perdido!", True, WHITE)
    score_text = font.render(f"Puntaje Jugador 1: {score1} | Puntaje Jugador 2: {score2}", True, WHITE)

    # Posicionar el texto en el centro de la pantalla
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - 100))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, screen.get_height() // 2 - 50))

    # Crear el botón "Jugar de nuevo"
    button_font = pygame.font.Font(None, 50)
    button_text = button_font.render("Jugar de nuevo", True, WHITE)
    button_rect = button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    
    # Dibujar el botón en la pantalla
    pygame.draw.rect(screen, (0, 0, 0), button_rect.inflate(20, 20))  # Fondo del botón
    screen.blit(button_text, button_rect)  # Texto del botón
    
    return button_rect  # Retorna la posición y tamaño del botón para detectar clics

import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dibujar Cartas en la Ventana")

# Colores
WHITE = (255, 255, 255)

# Variables para la cuadrícula de cartas
ROWS, COLS = 4, 4
GAP = 10
CARD_WIDTH = (WIDTH - (COLS + 1) * GAP) // COLS
CARD_HEIGHT = (HEIGHT - (ROWS + 1) * GAP) // ROWS

# Clase para representar las cartas
class Card:
    def __init__(self, rect):
        self.rect = rect

# Crear una lista de cartas
cards = []
for row in range(ROWS):
    for col in range(COLS):
        x = col * (CARD_WIDTH + GAP) + GAP
        y = row * (CARD_HEIGHT + GAP) + GAP
        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        card = Card(rect)
        cards.append(card)

# Bucle principal del juego
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((0, 0, 0))
    
    # Dibujar las cartas
    for card in cards:
        pygame.draw.rect(WIN, WHITE, card.rect)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

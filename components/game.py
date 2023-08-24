import pygame
import random

from .core import Card

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PokeMemorama")

# Colores
WHITE = (255, 255, 255)
BGWIN = (249, 102, 200)

# Variables para la cuadrícula de cartas
ROWS, COLS = 4, 4
GAP = 10
CARD_WIDTH = (WIDTH - (COLS + 1) * GAP) // COLS
CARD_HEIGHT = (HEIGHT - (ROWS + 1) * GAP) // ROWS


# Clase principal del juego     
class Pokememorama:
    def __init__(self):
        self.cards = self.load_cards()
        self.flipped_cards = []
        self.matches = 0

    def load_cards(self):
        # Cargamos las imagenes
        images = self.load_images()
        # Duplicamos las imagenes
        images *=2
        
        # Hacer Random las imagenes
        random.shuffle(images)
        cards = []
        for row in range(ROWS):
            for col in range(COLS):
                index = len(cards)
                x = col * (CARD_WIDTH + GAP) + GAP
                y = row * (CARD_HEIGHT + GAP) + GAP
                rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
                image = images[index]
                card = Card(image, rect)
                cards.append(card)
                
        return cards
    
    def load_images(self):
        pictures = [
            "chikorita.jpg", 
            "snorlax.jpg", 
            "voltorb.jpg", 
            "gengar.jpg", 
            "poliwhirl.jpg", 
            "vulpix.jpg", 
            "charmeleon.jpg", 
            "ivysaur.jpg"
        ]
        images = []
        for i, imname in enumerate(pictures):
            picture = pygame.image.load(f"./images/{imname}")
            picture = pygame.transform.scale(picture, (CARD_WIDTH, CARD_HEIGHT))
            images.append(picture)

        return images
    
    def draw_board(self):
        for card in self.cards:
            if card.flipped or card.matched:
                WIN.blit(card.image, card.rect.topleft)
            else:
                pygame.draw.rect(WIN, WHITE, card.rect)

    def check_match(self):
        # Verificamos si tenemos 2 tarjetas para comprar
        if len(self.flipped_cards) == 2:
            # Verficamos si es la misma imagen
            if self.flipped_cards[0].image == self.flipped_cards[1].image:
                print("match")
                # Marcamos como matched las tarjetas de la cuadricula
                for card in self.flipped_cards:
                    card.matched = True
                    
                # Aumentamos el contador
                self.matches += 1
            else:
                print("no match")
                # Regresamos las tarjetas volteadas
                for card in self.flipped_cards:
                    card.flipped = False

            self.flipped_cards.clear()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                # Eventos
                # Salir
                if event.type == pygame.QUIT:
                    running = False

                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for card in self.cards:
                        if card.rect.collidepoint(mouseX, mouseY) and not card.flipped and not card.matched:
                            card.flipped = True
                            self.flipped_cards.append(card)
                            self.check_match()
                            
            # Rellenar la pantalla de color
            WIN.fill(BGWIN)
            # Dibujamos la cuadricula
            self.draw_board()
            
            pygame.display.update()
            
            # Finalizamos el juego
            if self.matches == len(self.cards) // 2:
                running = False
                
            clock.tick(30)
            
        pygame.quit()
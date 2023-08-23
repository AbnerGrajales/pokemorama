import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PokéMemorama")

# Variables para la cuadrícula de cartas
ROWS, COLS = 4, 4
GAP = 10
CARD_WIDTH = (WIDTH - (COLS + 1) * GAP) // COLS
CARD_HEIGHT = (HEIGHT - (ROWS + 1) * GAP) // ROWS

# Colores
WHITE = (255, 255, 255)

# Clase para representar las cartas del juego
class Card:
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect
        self.flipped = False
        self.matched = False

# Clase principal del juego
class Pokememorama:
    def __init__(self):
        self.cards = self.load_cards()
        self.flipped_cards = []
        self.matches = 0

    def load_cards(self):
        images = []
        pokemon_images = self.fetch_pokemon_images()
        random.shuffle(pokemon_images)
        for i, imname in enumerate(pokemon_images):
            picture = pygame.image.load(f"./images/{imname}")
            picture = pygame.transform.scale(picture, (CARD_WIDTH, CARD_HEIGHT))
            images.append(picture)

        # Duplicamos las imagenes
        images *=2

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
    
    def fetch_pokemon_images(self):
        return ["chikorita.jpg", "snorlax.jpg", "voltorb.jpg", "gengar.jpg", "poliwhirl.jpg", "vulpix.jpg", "charmeleon.jpg", "ivysaur.jpg"]

    def draw_board(self):
        for card in self.cards:
            if card.flipped or card.matched:
                WIN.blit(card.image, card.rect.topleft)
            else:
                pygame.draw.rect(WIN, WHITE, card.rect)

    def check_match(self):
        if len(self.flipped_cards) == 2:
            if self.flipped_cards[0].image == self.flipped_cards[1].image:
                print("match")
                for card in self.flipped_cards:
                    card.matched = True
                self.matches += 1
            else:
                print("no match")
                for card in self.flipped_cards:
                    card.flipped = False
                    # pygame.draw.rect(WIN, WHITE, card.rect)

            self.flipped_cards.clear()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for card in self.cards:
                        if card.rect.collidepoint(mouseX, mouseY) and not card.flipped and not card.matched:
                            card.flipped = True
                            self.flipped_cards.append(card)
                            self.check_match()

            WIN.fill((0, 0, 0))
            self.draw_board()
            pygame.display.update()
            if self.matches == len(self.cards) // 2:
                running = False

            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Pokememorama()
    game.run()

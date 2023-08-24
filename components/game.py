import pygame

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("¡Hola, Mundo!")

# Colores
WHITE = (255, 255, 255)

# Clase principal del juego     
class Pokememorama:
    def __init__(self):
        self.cards = []
        self.flipped_cards = []
        self.matches = 0

    def load_cards(self):
        pass
    
    def load_images(self):
        pass

    def draw_board(self):
        pass

    def check_match(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                # Eventos
                if event.type == pygame.QUIT:
                    running = False

            WIN.fill(WHITE)  # Rellenar la pantalla con el color blanco
            
            # Mostrar "¡Hola, mundo!" en el centro de la pantalla
            font = pygame.font.Font(None, 36)
            text = font.render("¡Hola, mundo!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(text, text_rect)

            pygame.display.update()
            clock.tick(30)
            
        pygame.quit()
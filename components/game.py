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
            # picture = pygame.transform.scale(picture, (WIDTH, HEIGHT))
            images.append(picture)

        return images
    
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
            
            # Cargar la imagen en la pantalla
            first_image = self.load_images()[0]
            image_rect = first_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(first_image, image_rect)
                
            pygame.display.update()
            clock.tick(30)
            
        pygame.quit()
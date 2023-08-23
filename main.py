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
        print("Hola mundo")
        pass

if __name__ == "__main__":
    game = Pokememorama()
    game.run()

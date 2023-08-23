# Clase para representar las cartas del juego
class Card:
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect
        self.flipped = False
        self.matched = False


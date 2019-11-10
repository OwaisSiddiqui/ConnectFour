import pygame

DISC_PIXEL_DIAMETER = 67.258


class Disc:
    """
    A disc for the ConnectFour board.

    === Attributes ===
    x:
        - x CENTRE coordinate of the disc image (NOT the TOP LEFT coordinate)
    y:
        - y CENTRE coordinate of the disc image (NOT the TOP LEFT coordinate)
    """
    disc_image: pygame.image
    x: int
    y: int

    def __init__(self, colour: str):
        """
        Initialize the disc with an image according to the given colour. Set initial coordinates to (0, 0).
        """
        if colour == 'Red':
            self.disc_image = pygame.image.load('connect4_red_disc.png')
        elif colour == 'Yellow':
            self.disc_image = pygame.image.load('connect4_yellow_disc.png')
        self.x = 0
        self.y = 0

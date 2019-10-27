import pygame


class Disc:

    disc_image: pygame.image
    x: int
    y: int

    def __init__(self, colour: str):
        if colour == 'Red':
            self.disc_image = pygame.image.load('connect4_red_disc.png')
        elif colour == 'Yellow':
            self.disc_image = pygame.image.load('connect4_yellow_disc.png')
        self.x = 0
        self.y = 0

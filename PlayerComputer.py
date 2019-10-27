import pygame
from Player import *

class PlayerComputer(Player):

    def __init__(self, connect4, player) -> None:
        """
        Initialize a player
        """
        super(connect4, player)
    
    def get_move(self, col: int) -> int:
        """
        Uses minmax strategy to make the best possible move
        """
        pass

    
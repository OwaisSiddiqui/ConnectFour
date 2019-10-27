import pygame
from Player import *

class PlayerHuman(Player):

    def __init__(self, connect4, player) -> None:
        """
        Initialize a player
        """
        super(connect4, player)
    
    def get_move(self, col: int) -> int:
        """
        Gets column number after player chooses and clicks on a column
        """
        return col 

    
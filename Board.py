import pygame
import numpy as np
from typing import Union, Tuple

BOARD_PIXEL_LENGTH = 544.668
BOARD_PIXEL_WIDTH = 625.348
LEFT_BOARD_SPACE = 37.326
TOP_BOARD_SPACE = 77.666
X_SPACE_BETWEEN_LEFT_DISC = 22.236
X_SPACE_BETWEEN_DISCS = 18.344
Y_SPACE_BETWEEN_TOP_DISC = 21.953


class Board:
    """A board in a game of Connect Four.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the Game class, but not by client code.
    
    === Attributes ===
    board:
         The board that stores which chip is at which location.
    """
    
    board: np.array

    def __init__(self):
        """Initializes the Board Class"""
        self.board = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
                          ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
        self.board_image = pygame.image.load('connect4_board_image.png')

    def clear(self) -> None:
        """
        Clears the board.
        """
        for i in range(6):
            for j in range(7):
                self.board[i][j] = ""

    def move(self, col: int, player: str) -> None:
        """
        Makes a move based at the given location for a player 
        on the board.

        >>> x = Board()
        >>> x.move(1, "O")
        >>> print(x.board)
        [["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "",
        ["", "", "", "", "", "", ""],
        ["", "", "", "X", "", "", ""],
        ["", "O", "O", "O", "O", "", ""],
        ["", "X", "O", "O", "O", "X", "O"]]
        """
        # Checks if there is a chip on the lower row (if it exists)
        # And current position is not None
        # And makes a move if it is empty
        if self.get_position:
            self.board[self.get_position[0]][self.get_position[1]] = player

    def check_winner(self, player: str) -> bool:
        """
        Checks for a four in a row for a player

        Return True if finds a four in a row else return False

        >>> x = board()
        >>> print(x.check_winner("O", a))
        False
        >>> x.move(1, "O")
        >>> print(x.check_winner("O"))
        True
        """
        # Checks for horizontal four in a row
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == player and self.board[i][j + 1] == player and \
                self.board[i][j + 2] == player and self.board[i][j + 3] == player:
                    return True

        # Checks for vertiial four in a row
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == player and self.boardameboard[i + 1][j] == player and \
                self.board[i + 2][j] == player and self.board[i + 3][j] == player:
                    return True

        # For increasing slope diagonal four in a row
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == player and self.board[i+1][j+1] == player and \
                self.board[i+2][j+2] == player and self.board[i+3][j+3] == player:
                    return True

        # For decreasing slope diagonal four in a row
        for i in range(3, 6):
            for j in range(4):
                if self.board[i][j] == player and self.board[i-1][j+1] == player and \
                self.board[i-2][j+2] == player and self.board[i-3][j+3] == player:
                    return True

        return False
    
    def get_whose_turn(self) -> str:
        """
        Returns the player who will make the next move
        """
        if self.P1 == 'X':
            return self.P2
        else:
            return self.P1

    def get_position(self, col: int) -> Union[Tuple, bool]:
        """
        Retrieves the row in the column for the disc to drop, or returns False if board column is full
        """
        for row in range(6):
            if self.board[row][col] != "" and row == 0: # if all row spaces in column are full
                return False
            elif self.board[row][col] != "":
                return (row-1, col)
        return False
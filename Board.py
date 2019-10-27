import pygame
import numpy as np

class Board:
    """A board in a game of Connect Four.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the Game class, but not by client code.
    """
    # === Attributes ===
    # gameboard:
    #     The board that stores which chip is at which location.
    gameboard: np.array

    def __init__(self):
        """Initializes the Board Class"""
        self.gameboard = [
                    ["", "", "", "", "", "", ""],
					["", "", "", "", "", "", ""],
					["", "", "", "", "", "", ""],
					["", "", "", "", "", "", ""],
					["", "", "", "", "", "", ""],
					["", "", "", "", "", "", ""]
                    ]
        self.board_image = pygame.image.load('connect4_board_image.png')


    def clear(self) -> None:
        """
        Clears the gameboard.
        """
        for i in range(6):
            for j in range(7):
                self.gameboard[i][j] = ""


    def move(self, col: int, player: str) -> None:
        """
        Makes a move based at the given location for a player 
        on the gameboard.

        >>> x = board()
        >>> x.move(1, "O")
        >>> print(x.gameboard)
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
            self.gameboard[self.get_position[0]][self.get_position[1]] = player
			
	
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
                if self.gameboard[i][j] == player and self.gameboard[i][j + 1] == player and \
                self.gameboard[i][j + 2] == player and self.gameboard[i][j + 3] == player:
                    return True

        # Checks for vertiial four in a row
        for i in range(3):
            for j in range(7):
                if self.gameboard[i][j] == player and self.gameboardameboard[i + 1][j] == player and \
                self.gameboard[i + 2][j] == player and self.gameboard[i + 3][j] == player:
                    return True

        # For increasing slope diagonal four in a row
        for i in range(3):
            for j in range(4):
                if self.gameboard[i][j] == player and self.gameboard[i+1][j+1] == player and \
                self.gameboard[i+2][j+2] == player and self.gameboard[i+3][j+3] == player:
                    return True

        # For decreasing slope diagonal four in a row
        for i in range(3, 6):
            for j in range(4):
                if self.gameboard[i][j] == player and self.gameboard[i-1][j+1] == player and \
                self.gameboard[i-2][j+2] == player and self.gameboard[i-3][j+3] == player:
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
            if self.gameboard[row][col] != "" and row == 0: # if all row spaces in column are full
                return False
            elif self.gameboard[row][col] != "":
                return (row-1, col)
        return False
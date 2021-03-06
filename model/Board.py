import pygame
import numpy as np
from typing import Union, Tuple
from model import Disc

BOARD_PIXEL_LENGTH = 544.668
BOARD_PIXEL_WIDTH = 669.098

# Default display height and width is 1366 by 768 pixels, it is changed for different resolutions in Board
# initialization
LEFT_BOARD_SPACE = 1366/2 - BOARD_PIXEL_WIDTH / 2
TOP_BOARD_SPACE = 768/2 - BOARD_PIXEL_LENGTH / 2
X_SPACE_BETWEEN_LEFT_DISC = 25.072
X_SPACE_BETWEEN_DISCS = 2.008
Y_SPACE_BETWEEN_DISCS = 0
Y_SPACE_BETWEEN_TOP_DISC = 12.232
# Column borders (to determine which column the mouse is on)
FIRST_COLUMN_LEFT_BORDER = LEFT_BOARD_SPACE + X_SPACE_BETWEEN_LEFT_DISC
FIRST_COLUMN_RIGHT_BORDER = LEFT_BOARD_SPACE + X_SPACE_BETWEEN_LEFT_DISC + Disc.DISC_PIXEL_DIAMETER + \
                            X_SPACE_BETWEEN_DISCS / 2
SECOND_COLUMN_LEFT_BORDER = FIRST_COLUMN_RIGHT_BORDER
SECOND_COLUMN_RIGHT_BORDER = SECOND_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
THIRD_COLUMN_LEFT_BORDER = SECOND_COLUMN_RIGHT_BORDER
THIRD_COLUMN_RIGHT_BORDER = THIRD_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
FOURTH_COLUMN_LEFT_BORDER = THIRD_COLUMN_RIGHT_BORDER
FOURTH_COLUMN_RIGHT_BORDER = FOURTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
FIFTH_COLUMN_LEFT_BORDER = FOURTH_COLUMN_RIGHT_BORDER
FIFTH_COLUMN_RIGHT_BORDER = FIFTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
SIXTH_COLUMN_LEFT_BORDER = FIFTH_COLUMN_RIGHT_BORDER
SIXTH_COLUMN_RIGHT_BORDER = SIXTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
SEVENTH_COLUMN_LEFT_BORDER = SIXTH_COLUMN_RIGHT_BORDER
SEVENTH_COLUMN_RIGHT_BORDER = SEVENTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2

FIRST_ROW_TOP_BORDER = TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC
FIRST_ROW_BOTTOM_BORDER = FIRST_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
SECOND_ROW_TOP_BORDER = FIRST_ROW_BOTTOM_BORDER
SECOND_ROW_BOTTOM_BORDER = SECOND_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
THIRD_ROW_TOP_BORDER = SECOND_ROW_BOTTOM_BORDER
THIRD_ROW_BOTTOM_BORDER = THIRD_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
FOURTH_ROW_TOP_BORDER = THIRD_ROW_BOTTOM_BORDER
FOURTH_ROW_BOTTOM_BORDER = FOURTH_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
FIFTH_ROW_TOP_BORDER = FOURTH_ROW_BOTTOM_BORDER
FIFTH_ROW_BOTTOM_BORDER = FIFTH_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
SIXTH_ROW_TOP_BORDER = FIFTH_ROW_BOTTOM_BORDER
SIXTH_ROW_BOTTOM_BORDER = SIXTH_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER

P1 = 'X'
P2 = 'O'
EMPTY = ''


class Board:
    """A board in a game of Connect Four.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the Game class, but not by client code.
    
    === Attributes ===
    board:
         The board that stores which chip is at which location.
    """
    
    board: np.array

    def __init__(self, display_width, display_height):
        """Initializes the Board Class"""
        self.board = [["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", ""]]
        self.board_image = pygame.image.load('viewcontroller\connect4_board_image.png')

        global LEFT_BOARD_SPACE
        global TOP_BOARD_SPACE
        global X_SPACE_BETWEEN_LEFT_DISC
        global X_SPACE_BETWEEN_DISCS
        global Y_SPACE_BETWEEN_DISCS
        global Y_SPACE_BETWEEN_TOP_DISC
        # Column borders (to determine which column the mouse is on)
        global FIRST_COLUMN_LEFT_BORDER
        global FIRST_COLUMN_RIGHT_BORDER
        global SECOND_COLUMN_LEFT_BORDER
        global SECOND_COLUMN_RIGHT_BORDER
        global THIRD_COLUMN_LEFT_BORDER
        global THIRD_COLUMN_RIGHT_BORDER
        global FOURTH_COLUMN_LEFT_BORDER
        global FOURTH_COLUMN_RIGHT_BORDER
        global FIFTH_COLUMN_LEFT_BORDER
        global FIFTH_COLUMN_RIGHT_BORDER
        global SIXTH_COLUMN_LEFT_BORDER
        global SIXTH_COLUMN_RIGHT_BORDER
        global SEVENTH_COLUMN_LEFT_BORDER
        global SEVENTH_COLUMN_RIGHT_BORDER

        global FIRST_ROW_TOP_BORDER
        global FIRST_ROW_BOTTOM_BORDER
        global SECOND_ROW_TOP_BORDER
        global SECOND_ROW_BOTTOM_BORDER
        global THIRD_ROW_TOP_BORDER
        global THIRD_ROW_BOTTOM_BORDER
        global FOURTH_ROW_TOP_BORDER
        global FOURTH_ROW_BOTTOM_BORDER
        global FIFTH_ROW_TOP_BORDER
        global FIFTH_ROW_BOTTOM_BORDER
        global SIXTH_ROW_TOP_BORDER
        global SIXTH_ROW_BOTTOM_BORDER

        LEFT_BOARD_SPACE = 1366 / 2 - BOARD_PIXEL_WIDTH / 2
        TOP_BOARD_SPACE = 768 / 2 - BOARD_PIXEL_LENGTH / 2
        X_SPACE_BETWEEN_LEFT_DISC = 25.072
        X_SPACE_BETWEEN_DISCS = 2.008
        Y_SPACE_BETWEEN_DISCS = 0
        Y_SPACE_BETWEEN_TOP_DISC = 12.232
        # Column borders (to determine which column the mouse is on)
        FIRST_COLUMN_LEFT_BORDER = LEFT_BOARD_SPACE + X_SPACE_BETWEEN_LEFT_DISC
        FIRST_COLUMN_RIGHT_BORDER = LEFT_BOARD_SPACE + X_SPACE_BETWEEN_LEFT_DISC + Disc.DISC_PIXEL_DIAMETER + \
                                           X_SPACE_BETWEEN_DISCS / 2
        SECOND_COLUMN_LEFT_BORDER = FIRST_COLUMN_RIGHT_BORDER
        SECOND_COLUMN_RIGHT_BORDER = SECOND_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
        THIRD_COLUMN_LEFT_BORDER = SECOND_COLUMN_RIGHT_BORDER
        THIRD_COLUMN_RIGHT_BORDER = THIRD_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
        FOURTH_COLUMN_LEFT_BORDER = THIRD_COLUMN_RIGHT_BORDER
        FOURTH_COLUMN_RIGHT_BORDER = FOURTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
        FIFTH_COLUMN_LEFT_BORDER = FOURTH_COLUMN_RIGHT_BORDER
        FIFTH_COLUMN_RIGHT_BORDER = FIFTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
        SIXTH_COLUMN_LEFT_BORDER = FIFTH_COLUMN_RIGHT_BORDER
        SIXTH_COLUMN_RIGHT_BORDER = SIXTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2
        SEVENTH_COLUMN_LEFT_BORDER = SIXTH_COLUMN_RIGHT_BORDER
        SEVENTH_COLUMN_RIGHT_BORDER = SEVENTH_COLUMN_LEFT_BORDER + Disc.DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_DISCS / 2

        FIRST_ROW_TOP_BORDER = TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC
        FIRST_ROW_BOTTOM_BORDER = FIRST_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
        SECOND_ROW_TOP_BORDER = FIRST_ROW_BOTTOM_BORDER
        SECOND_ROW_BOTTOM_BORDER = SECOND_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
        THIRD_ROW_TOP_BORDER = SECOND_ROW_BOTTOM_BORDER
        THIRD_ROW_BOTTOM_BORDER = THIRD_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
        FOURTH_ROW_TOP_BORDER = THIRD_ROW_BOTTOM_BORDER
        FOURTH_ROW_BOTTOM_BORDER = FOURTH_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
        FIFTH_ROW_TOP_BORDER = FOURTH_ROW_BOTTOM_BORDER
        FIFTH_ROW_BOTTOM_BORDER = FIFTH_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER
        SIXTH_ROW_TOP_BORDER = FIFTH_ROW_BOTTOM_BORDER
        SIXTH_ROW_BOTTOM_BORDER = SIXTH_ROW_TOP_BORDER + Disc.DISC_PIXEL_DIAMETER

    def clear(self) -> None:
        """
        Clears the board.
        """
        for row in range(6):
            for col in range(7):
                self.board[row][col] = EMPTY

    def move(self, col: int, player: str) -> None:
        """
        Makes a move based at the given location for a player 
        on the board.

        Checks if there is a chip on the lower row (if it exists)
        And current position is not None
        And makes a move if it is empty

        >>> board = Board()
        >>> board.move(1, 1, "O")
        >>> print(board.board)
        [["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "",
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""]]
        """
        move = self.get_position(col)
        if move:
            self.board[move[0]][move[1]] = player


    def check_winner(self, player: str) -> bool:
        """
        Checks for a four in a row for a player

        Return True if finds a four in a row else return False

        >>> x = Board()
        >>> print(x.check_winner(P2))
        False
        >>> x.move(1, "O")
        >>> print(x.check_winner(P2))
        True
        """
        # Checks for horizontal four in a row
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == player and self.board[i][j + 1] == player and \
                        self.board[i][j + 2] == player and self.board[i][j + 3] == player:
                    return True

        # Checks for vertical four in a row
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == player and self.board[i + 1][j] == player and \
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

    def get_winner(self):
        is_X_winner, is_O_winner = self.check_winner('X'), self.check_winner('O')
        if is_X_winner:
            return 'X'
        elif is_O_winner:
            return 'O'
        else:
            return False

    @staticmethod
    def get_whose_turn(player: str) -> str:
        """
        Returns the player who will make the next move
        """
        if player == P1:
            return P2
        elif player == P2:
            return P1
        else:
            return EMPTY

    def get_position(self, col: int) -> Union[Tuple[int, int], bool]:
        """
        Retrieves the row in the column for the disc to drop, or returns False if board column is full
        """
        col -= 1
        for row in range(6):
            # If all row spaces in column are full
            if self.board[row][col] != EMPTY and row == 0:
                return False
            elif self.board[row][col] != EMPTY:
                return row - 1, col
        return 5, col

    def get(self, row, col):
        """
        Retrieves the exact coordinate of a row/col space
        """
        return self.board[row][col]

    def __str__(self):
        board_str = ""
        for row in range(6):
            board_str += "[" + str(self.get(row, 0)) + ", " + str(self.get(row, 1)) + \
                         ", " + str(self.get(row, 2)) + ", " + str(self.get(row, 3)) + ", " + \
                         str(self.get(row, 4)) + ", " + str(self.get(row, 5)) + ", " + str(self.get(row, 6)) + "] \n"

        return board_str

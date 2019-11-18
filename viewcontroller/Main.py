"""
ConnectFour | CSC290
"""
import pygame
from model import Board, Disc
from typing import Union, Tuple

# Initializes the pygame modules
pygame.init()

# Initialize the board and discs
board = Board.Board()
disc_array = [Disc.Disc("Red") if i % 2 == 0 else Disc.Disc("Yellow") for i in range(42)]
disc_used_array = []
move = (0, 0)

# Disc number in the array
disc_number = 0

# The window of the game
display = pygame.display.set_mode((700, 700))
pygame.display.set_caption('ConnectFour')

# Variable for when mouse is pressed down
is_disc_dropping = False

# Column choice
column = None

# Velocity and acceleration for dropping disc
velocity = 3
acceleration = 0

# Frames per minute controller
clock = pygame.time.Clock()
FPS = 60


def get_move(mouse_pos: Tuple[int, int], player: str) -> Union[Tuple[int, int], bool]:
    move_to_make = [0, 0]
    if Board.FIRST_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.FIRST_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 1
    elif Board.SECOND_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.SECOND_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 2
    elif Board.THIRD_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.THIRD_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 3
    elif Board.FOURTH_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.FOURTH_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 4
    elif Board.FIFTH_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.FIFTH_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 5
    elif Board.SIXTH_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.SIXTH_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 6
    elif Board.SEVENTH_COLUMN_LEFT_BORDER <= mouse_pos[0] <= Board.SEVENTH_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 7
    possible_move = board.get_position(move_to_make[1])
    if possible_move:
        return possible_move[0], move_to_make[1]


def set_disc_to_column(disc: Disc, mouse_pos: Tuple[int, int]):
    if Board.FIRST_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.FIRST_COLUMN_RIGHT_BORDER:
        disc.x = (Board.FIRST_COLUMN_LEFT_BORDER + Board.FIRST_COLUMN_RIGHT_BORDER) / 2
    elif Board.SECOND_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.SECOND_COLUMN_RIGHT_BORDER:
        disc.x = (Board.SECOND_COLUMN_LEFT_BORDER + Board.SECOND_COLUMN_RIGHT_BORDER) / 2
    elif Board.THIRD_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.THIRD_COLUMN_RIGHT_BORDER:
        disc.x = (Board.THIRD_COLUMN_LEFT_BORDER + Board.THIRD_COLUMN_RIGHT_BORDER) / 2
    elif Board.FOURTH_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.FOURTH_COLUMN_RIGHT_BORDER:
        disc.x = (Board.FOURTH_COLUMN_LEFT_BORDER + Board.FOURTH_COLUMN_RIGHT_BORDER) / 2
    elif Board.FIFTH_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.FIFTH_COLUMN_RIGHT_BORDER:
        disc.x = (Board.FIFTH_COLUMN_LEFT_BORDER + Board.FIFTH_COLUMN_RIGHT_BORDER) / 2
    elif Board.SIXTH_COLUMN_LEFT_BORDER <= mouse_pos[0] < Board.SIXTH_COLUMN_RIGHT_BORDER:
        disc.x = (Board.SIXTH_COLUMN_LEFT_BORDER + Board.SIXTH_COLUMN_RIGHT_BORDER) / 2
    elif Board.SEVENTH_COLUMN_LEFT_BORDER <= mouse_pos[0] <= Board.SEVENTH_COLUMN_RIGHT_BORDER:
        disc.x = (Board.SEVENTH_COLUMN_LEFT_BORDER + Board.SEVENTH_COLUMN_RIGHT_BORDER) / 2
    disc.y = Board.TOP_BOARD_SPACE - Disc.DISC_PIXEL_DIAMETER / 2 - 5


if __name__ == '__main__':
    # Keep the window running forever until you cross the window
    while True:
        # Gets all the events on the window (e.g. mouse movement, keyboard presses)
        events = pygame.event.get()
        # Get mouse coordinates
        mouse_pos = pygame.mouse.get_pos()

        # Go through the events and do something for a specific one
        for event in events:
            # Close the window and stop the code from running if the cross button on the window is pressed
            if event.type == pygame.QUIT:
                quit()

            if not is_disc_dropping:
                # Set disc x-cor to middle of column the mouse_pos is in between, set disc y-cor to above board
                set_disc_to_column(disc_array[disc_number], mouse_pos)

            if event.type == pygame.KEYDOWN:
                print(board)

            # Set mouse is down if the user does a right click
            if event.type == pygame.MOUSEBUTTONDOWN and not is_disc_dropping:
                is_disc_dropping = True
                move = get_move(mouse_pos, disc_array[disc_number].player)

        # If mouse is down and mouse clicked, show the disc falling down
        if is_disc_dropping:
            is_disc_dropping = True
            disc_array[disc_number].y = min(Board.BOARD_PIXEL_LENGTH + Board.TOP_BOARD_SPACE - Disc.DISC_PIXEL_DIAMETER / 2 -
                                            Board.Y_SPACE_BETWEEN_TOP_DISC, disc_array[disc_number].y + velocity)
            velocity += acceleration

            # When disc reaches the end of the board set is_disc_dropping to False so the mouse can track the disc
            # again
            if disc_array[disc_number].y == Board.BOARD_PIXEL_LENGTH + Board.TOP_BOARD_SPACE - Disc.DISC_PIXEL_DIAMETER / 2 - \
                    Board.Y_SPACE_BETWEEN_TOP_DISC:
                board.move(move[1], disc_array[disc_number].player)
                is_disc_dropping = False
                disc_used_array.append(disc_array[disc_number])
                disc_number += 1

        # FPS Controller
        dt = clock.tick(FPS)
        dt /= 1000

        # Display the background, board, and discs
        display.fill((255, 255, 255))
        for disc in disc_used_array:
            display.blit(disc.disc_image, (disc.x - Disc.DISC_PIXEL_DIAMETER / 2, disc.y - Disc.DISC_PIXEL_DIAMETER / 2))
        display.blit(disc_array[disc_number].disc_image, (disc_array[disc_number].x - Disc.DISC_PIXEL_DIAMETER / 2,
                                                          disc_array[disc_number].y - Disc.DISC_PIXEL_DIAMETER / 2))
        display.blit(board.board_image, (350 - Board.BOARD_PIXEL_WIDTH / 2, 350 - Board.BOARD_PIXEL_LENGTH / 2))
        
        # Update the pygame window to show the changes
        pygame.display.update()
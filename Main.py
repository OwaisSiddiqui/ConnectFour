"""
Connect4 game | CSC290
"""

from Board import *
from Disc import *

if __name__ == '__main__':
    # Initializes the pygame modules
    pygame.init()

    # Initialize the board and disc
    board = Board()
    disc = Disc("Red")

    # Board and Disc dimensions for mouse positioning
    BOARD_PIXEL_LENGTH = 625.348
    BOARD_PIXEL_WIDTH = 544.668
    DISC_PIXEL_DIAMETER = 69.252

    # The window of the game
    display_surface = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('ConnectFour')

    # Fill the background of the game in white
    display_surface.fill((255, 255, 255))

    # Display the board image
    display_surface.blit(board.board_image, (350 - 625.348 / 2, (300 - 544.668 / 2) + 50))

    # Variable for when mouse is pressed down
    is_mouse_down = False

    # Main game while loop
    while True:

        # Iterates through the pygame events on the window (e.g. mouse movement, keyboard presses)
        for event in pygame.event.get():

            # If the mouse is on the top of the board, display the disc with the mouse position
            if pygame.mouse.get_pos()[1] <= (300 - BOARD_PIXEL_WIDTH/2) + 50 and not is_mouse_down:

                # Get position of the mouse and set it to disc coordinates
                disc.x = pygame.mouse.get_pos()[0]
                disc.y = pygame.mouse.get_pos()[1]

                display_surface.fill((255, 255, 255))
                # Setting the centre of the disc to the mouse position
                display_surface.blit(board.board_image, (350 - BOARD_PIXEL_LENGTH/2,
                                                         (300 - BOARD_PIXEL_WIDTH / 2) + 50))
                display_surface.blit(disc.disc_image, (disc.x - DISC_PIXEL_DIAMETER/2, disc.y - DISC_PIXEL_DIAMETER/2))

        # Set mouse is down when mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_down = True

        # If mouse is down and mouse clicked, show the disc falling down
        if event.type == pygame.MOUSEBUTTONDOWN or is_mouse_down:
            is_mouse_down = True
            disc.y += 3

            # Re-display the background and board so the disc doesn't have a trail
            display_surface.fill((255, 255, 255))
            display_surface.blit(disc.disc_image, (disc.x - 69.252 / 2, disc.y - 69.252 / 2))
            display_surface.blit(board.board_image, (350 - 625.348 / 2, (300 - 544.668 / 2) + 50))

            # When disc reaches the end of the board set is_mouse_down to False so the mouse can track the disc again
            if disc.y >= 570:
                is_mouse_down = False

        # Update the pygame window to show the changes
        pygame.display.update()

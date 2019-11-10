"""
ConnectFour | CSC290
"""
from Board import *
from Disc import *
from SATCollisionDetectionCircleRectangle import *

if __name__ == '__main__':
    # Initializes the pygame modules
    pygame.init()

    # Initialize the board and discs
    board = Board()
    disc_array = [Disc("Red") if i % 2 == 0 else Disc("Yellow") for i in range(21)]
    disc_used_array = []

    # Disc number in the array
    i = 0

    # Boundary rectangles between columns so that if discs were dropped they would go into one of the columns
    rectangles = [[(LEFT_BOARD_SPACE, TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC - 10),
                   (LEFT_BOARD_SPACE + X_SPACE_BETWEEN_LEFT_DISC, TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC),
                   (LEFT_BOARD_SPACE + X_SPACE_BETWEEN_LEFT_DISC, TOP_BOARD_SPACE + BOARD_PIXEL_LENGTH - Y_SPACE_BETWEEN_TOP_DISC * 2),
                   (LEFT_BOARD_SPACE, TOP_BOARD_SPACE + BOARD_PIXEL_LENGTH - Y_SPACE_BETWEEN_TOP_DISC * 2)],
                  [(LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_LEFT_DISC, TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC - 10),
                   (LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_LEFT_DISC + X_SPACE_BETWEEN_DISCS, TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC),
                   (LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_LEFT_DISC + X_SPACE_BETWEEN_DISCS, TOP_BOARD_SPACE + BOARD_PIXEL_LENGTH - Y_SPACE_BETWEEN_TOP_DISC * 2),
                   (LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER + X_SPACE_BETWEEN_LEFT_DISC, TOP_BOARD_SPACE + BOARD_PIXEL_LENGTH - Y_SPACE_BETWEEN_TOP_DISC * 2)],
                  [(LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER*2 + X_SPACE_BETWEEN_LEFT_DISC + X_SPACE_BETWEEN_DISCS, TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC - 10),
                   (LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER*2 + X_SPACE_BETWEEN_LEFT_DISC + X_SPACE_BETWEEN_DISCS*2, TOP_BOARD_SPACE + Y_SPACE_BETWEEN_TOP_DISC),
                   (LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER*2 + X_SPACE_BETWEEN_LEFT_DISC + X_SPACE_BETWEEN_DISCS*2, TOP_BOARD_SPACE + BOARD_PIXEL_LENGTH - Y_SPACE_BETWEEN_TOP_DISC * 2),
                   (LEFT_BOARD_SPACE + DISC_PIXEL_DIAMETER*2 + X_SPACE_BETWEEN_LEFT_DISC + X_SPACE_BETWEEN_DISCS, TOP_BOARD_SPACE + BOARD_PIXEL_LENGTH - Y_SPACE_BETWEEN_TOP_DISC * 2)]]

    # The window of the game
    display = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('ConnectFour')

    # Fill the background of the game in white
    display.fill((255, 255, 255))

    # Display the board image
    display.blit(board.board_image, (350 - BOARD_PIXEL_WIDTH / 2, 350 - BOARD_PIXEL_LENGTH / 2))

    # Variable for when mouse is pressed down
    is_mouse_down = False

    # Velocity and acceleration for dropping disc
    velocity = 0
    acceleration = 1

    # Frames per minute controller
    clock = pygame.time.Clock()
    FPS = 60

    # Keep the window running forever until you cross the window
    while True:

        # Iterates through the pygame events on the window (e.g. mouse movement, keyboard presses)
        for event in pygame.event.get():

            # Close the window and stop the code from running if the cross button on the window is pressed
            if event.type == pygame.QUIT:
                quit()

            # If the mouse is on the top of the board, move the disc center to the mouse position
            if pygame.mouse.get_pos()[1] <= TOP_BOARD_SPACE - DISC_PIXEL_DIAMETER/2 and not is_mouse_down:

                # Get position of the mouse and set it to disc coordinates
                mouse_cor = pygame.mouse.get_pos()
                disc_array[i].x = mouse_cor[0]
                disc_array[i].y = mouse_cor[1]
            elif not is_mouse_down:

                # Get position of the mouse and set it to disc coordinates
                disc_array[i].x = pygame.mouse.get_pos()[0]
                disc_array[i].y = TOP_BOARD_SPACE - DISC_PIXEL_DIAMETER/2

        # Set mouse is down when mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_down = True

        # If mouse is down and mouse clicked, show the disc falling down
        if event.type == pygame.MOUSEBUTTONDOWN or is_mouse_down:
            is_mouse_down = True
            for rectangle in rectangles:
                if is_collision((disc_array[i].x, disc_array[i].y), DISC_PIXEL_DIAMETER / 2, rectangle):
                    print("COLLISION IS LIKELY CHANGING THIS")
                    minimum_translation_vector_main = get_minimum_translation_vector(
                        (disc_array[i].x, disc_array[i].y), DISC_PIXEL_DIAMETER / 2, rectangle)
                    dx = -minimum_translation_vector_main.magnitude * minimum_translation_vector_main.direction_x
                    dy = -minimum_translation_vector_main.magnitude * minimum_translation_vector_main.direction_y
                    disc_array[i].x, disc_array[i].y = (int(disc_array[i].x + dx), int(disc_array[i].y + dy))

            # Re-display the background and board so the disc doesn't have a trail
            display.fill((255, 255, 255))
            display.blit(disc_array[i].disc_image, (disc_array[i].x - DISC_PIXEL_DIAMETER / 2,
                                                    disc_array[i].y - DISC_PIXEL_DIAMETER / 2))
            for disc in disc_used_array:
                display.blit(disc.disc_image, (disc.x, disc.y))
            display.blit(board.board_image, (350 - BOARD_PIXEL_WIDTH / 2, 350 - BOARD_PIXEL_LENGTH / 2))

            disc_array[i].y = min(BOARD_PIXEL_LENGTH + TOP_BOARD_SPACE - DISC_PIXEL_DIAMETER / 2 -
                                  Y_SPACE_BETWEEN_TOP_DISC, disc_array[i].y + velocity)
            velocity += acceleration
            print(disc_array[i].y)

            # When disc reaches the end of the board set is_mouse_down to False so the mouse can track the disc again
            if disc_array[i].y == BOARD_PIXEL_LENGTH + TOP_BOARD_SPACE - DISC_PIXEL_DIAMETER/2 - \
                    Y_SPACE_BETWEEN_TOP_DISC:
                print(disc_array[i].x, disc_array[i].y)
                disc_array[i].x = disc_array[i].x - DISC_PIXEL_DIAMETER / 2
                disc_array[i].y = disc_array[i].y - DISC_PIXEL_DIAMETER / 2
                is_mouse_down = False
                disc_used_array.append(disc_array[i])
                i += 1

                # Reset velocity to 0 for new disc to be dropped
                velocity = 0

        # FPS Controller
        dt = clock.tick(FPS)
        dt /= 1000

        display.fill((255, 255, 255))
        display.blit(disc_array[i].disc_image, (disc_array[i].x - DISC_PIXEL_DIAMETER / 2,
                                                disc_array[i].y - DISC_PIXEL_DIAMETER / 2))
        for disc in disc_used_array:
            display.blit(disc.disc_image, (disc.x, disc.y))
        display.blit(board.board_image, (350 - BOARD_PIXEL_WIDTH / 2, 350 - BOARD_PIXEL_LENGTH / 2))

        # Update the pygame window to show the changes
        pygame.display.update()

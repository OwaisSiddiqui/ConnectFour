"""
ConnectFour | CSC290
"""
import pygame
from model import Board, Disc
from model import Scoreboard
from typing import Union, Tuple


def get_move(mouse_pos: Tuple[int, int]) -> Union[Tuple[int, int], bool]:
    move_to_make = [0, 0]
    if mouse_pos[0] < Board.FIRST_COLUMN_RIGHT_BORDER:
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
    elif mouse_pos[0] >= Board.SIXTH_COLUMN_RIGHT_BORDER:
        move_to_make[1] = 7
    possible_move = board.get_position(move_to_make[1])
    if possible_move:
        return possible_move[0], move_to_make[1]


def set_disc_to_column(disc: Disc, mouse_pos: Tuple[int, int]):
    if mouse_pos[0] < Board.FIRST_COLUMN_RIGHT_BORDER:
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
    elif mouse_pos[0] > Board.SIXTH_COLUMN_RIGHT_BORDER:
        disc.x = (Board.SEVENTH_COLUMN_LEFT_BORDER + Board.SEVENTH_COLUMN_RIGHT_BORDER) / 2
    disc.y = Board.TOP_BOARD_SPACE - Disc.DISC_PIXEL_DIAMETER / 2 - 5


def get_row_position(row: int):
    if row == 0:
        return (Board.FIRST_ROW_TOP_BORDER + Board.FIRST_ROW_BOTTOM_BORDER) / 2
    if row == 1:
        return (Board.SECOND_ROW_TOP_BORDER + Board.SECOND_ROW_BOTTOM_BORDER) / 2
    if row == 2:
        return (Board.THIRD_ROW_TOP_BORDER + Board.THIRD_ROW_BOTTOM_BORDER) / 2
    if row == 3:
        return (Board.FOURTH_ROW_TOP_BORDER + Board.FOURTH_ROW_BOTTOM_BORDER) / 2
    if row == 4:
        return (Board.FIFTH_ROW_TOP_BORDER + Board.FIFTH_ROW_BOTTOM_BORDER) / 2
    if row == 5:
        return (Board.SIXTH_ROW_TOP_BORDER + Board.SIXTH_ROW_BOTTOM_BORDER) / 2


# Initializes the pygame modules
pygame.init()

# The window of the game
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display_width, display_height = pygame.display.get_surface().get_size()
pygame.display.set_caption('ConnectFour')

# Initialize the board and discs
board = Board.Board(display_width, display_height)
disc_array = [Disc.Disc("Red") if i % 2 == 0 else Disc.Disc("Yellow") for i in range(42)]
for disc in disc_array:
    disc.x = (Board.FIRST_COLUMN_LEFT_BORDER + Board.FIRST_COLUMN_RIGHT_BORDER) / 2
    disc.y = Board.TOP_BOARD_SPACE - Disc.DISC_PIXEL_DIAMETER / 2 - 5
disc_used_array = []
move = (0, 0)
row_position = None

# Disc number in the array
disc_number = 0

# Create a scoreboard and set its position to the right of the board
scoreboard = Scoreboard.Scoreboard(100, 100)

# Variable for when mouse is pressed down
is_disc_dropping = False

# Column choice
column = None

# Velocity and acceleration for dropping disc
velocity = 0
acceleration = 0.7

# Frames per minute controller
clock = pygame.time.Clock()
FPS = 60

possible_winner = ""

# Homepage initializations

# load the images and assign variables name
bg = pygame.image.load(r'model\images\bg_image.jpeg')
bg = pygame.transform.scale(bg, (1000, 800))

play_button = pygame.image.load(r"model\images\play_button.png")
play_button = pygame.transform.scale(play_button, (400, 400))

pve_button = pygame.image.load(r"model\images\pve_button.png")
pve_button = pygame.transform.scale(pve_button, (450, 75))

pvp_button = pygame.image.load(r"model\images\pvp_button.png")
pvp_button = pygame.transform.scale(pvp_button, (450, 75))

current = "home"

leaderboard_button = pygame.image.load(r"model\images\leaderboard_button.png")
leaderboard_button = pygame.transform.scale(leaderboard_button, (200, 50))


if __name__ == '__main__':
    # Keep the window running forever until you cross the window
    while True:
        # Gets all the events on the window (e.g. mouse movement, keyboard presses)
        events = pygame.event.get()
        # Get mouse coordinates
        mouse_pos = pygame.mouse.get_pos()
        is_clicked = False

        if not is_disc_dropping:
            # Set disc x-cor to middle of column the mouse_pos is in between, set disc y-cor to above board
            set_disc_to_column(disc_array[disc_number], mouse_pos)

        # Go through the events and do something for a specific one
        for event in events:
            # Close the window and stop the code from running if the cross button on the window is pressed
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                scoreboard.stop_timer()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                print(board)

            # Set mouse is down if the user does a left click
            if event.type == pygame.MOUSEBUTTONDOWN and not is_disc_dropping:
                move = get_move(mouse_pos)
                if move:
                    is_disc_dropping = True
                    row_position = get_row_position(move[0])
                    scoreboard.run()
                else:
                    row_position = None
                    is_disc_dropping = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_clicked = True

        if current == "game":
            # If mouse is down and mouse clicked, show the disc falling down
            if is_disc_dropping and row_position is not None:
                is_disc_dropping = True
                disc_array[disc_number].y = min(row_position, disc_array[disc_number].y + velocity)
                velocity += acceleration

                # When disc reaches the end of the board set is_disc_dropping to False so the mouse can track the disc
                # again
                if disc_array[disc_number].y == row_position:
                    velocity = 0
                    board.move(move[1], disc_array[disc_number].player)
                    is_disc_dropping = False
                    disc_used_array.append(disc_array[disc_number])
                    disc_number += 1
                    scoreboard.stop_timer()
                possible_winner = board.get_winner()
                if possible_winner:
                    pass

            # FPS Controller
            dt = clock.tick(FPS)
            dt /= 1000

        if current == "home":
            display.fill((28, 63, 94))
            display.blit(bg, (0, 0))
            display.blit(play_button, (300, 600))
            display.blit(leaderboard_button, (25, 25))
            if 325 < mouse_pos[0] < 325 + 355 and 600 < mouse_pos[1] < 600 + 80 and is_clicked:
                current = "mode"
                is_clicked = False
        elif current == "mode":
            display.blit(bg, (0, 0))
            display.blit(pve_button, (300, 550))
            display.blit(pvp_button, (300, 675))
            if 300 < mouse_pos[0] < 300 + 450 and 550 < mouse_pos[1] < 550 + 75 and is_clicked:
                current = "disc colour"
                is_clicked = False
            if 300 < mouse_pos[0] < 300 + 450 and 675 < mouse_pos[1] < 675 + 75 and is_clicked:
                current = "disc colour"
                is_clicked = False
        elif current == "disc colour":
            display.blit(bg, (0, 0))
            display.blit(pygame.image.load(r"viewcontroller\connect4_red_disc.png"), (300, 600))
            display.blit(pygame.image.load(r"viewcontroller\connect4_yellow_disc.png"), (400, 600))
            if 300 < mouse_pos[0] < 300+Disc.DISC_PIXEL_DIAMETER and 600 < mouse_pos[1] < 600 + Disc.DISC_PIXEL_DIAMETER and is_clicked:
                current = "game"
                is_clicked = False
            if 400 < mouse_pos[0] < 400+Disc.DISC_PIXEL_DIAMETER and 600 < mouse_pos[1] < 600 + Disc.DISC_PIXEL_DIAMETER and is_clicked:
                current = "game"
                is_clicked = False
        elif current == "game":
            display.fill((255, 255, 255))
            for disc in disc_used_array:
                display.blit(disc.disc_image,
                             (disc.x - Disc.DISC_PIXEL_DIAMETER / 2, disc.y - Disc.DISC_PIXEL_DIAMETER / 2))
            display.blit(disc_array[disc_number].disc_image, (disc_array[disc_number].x - Disc.DISC_PIXEL_DIAMETER / 2,
                                                              disc_array[disc_number].y - Disc.DISC_PIXEL_DIAMETER / 2))
            display.blit(board.board_image, (display_width / 2 - Board.BOARD_PIXEL_WIDTH / 2, display_height / 2 -
                                             Board.BOARD_PIXEL_LENGTH / 2))
            pygame.draw.rect(display, scoreboard.colour, scoreboard.scoreboard_display)
            time_display_rendered = scoreboard.time_display.render(str(scoreboard.get_current_time()), True, (0, 0, 0))
            display.blit(time_display_rendered, (scoreboard.x + (scoreboard.scoreboard_display[2] / 2 -
                                                                 time_display_rendered.get_width() / 2),
                                                 scoreboard.y + (scoreboard.scoreboard_display[3] / 2 -
                                                                 time_display_rendered.get_height() / 2)))
        # Update the pygame window to show the changes
        pygame.display.update()

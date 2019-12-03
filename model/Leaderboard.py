import pygame
from collections import Counter

pygame.init()

# display size
display_width = 800
display_height = 600

# colour setting
black = (0, 0, 0)
white = (255, 255, 255)

# screen setting
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('LeaderBoard')
clock = pygame.time.Clock()

# top10 players list
player_dict = {"player 1": 1000000, "player 2": 10, "player 3": 100000000, "player 4": 100, "player 5": 1000000000,
               "player 6": 10000, "player 7": 10000000000, "player 8": 100000, "player 9": 1000, "player 10": 10000000}


# transfer players' data from dict to list with top10 score
def player_list(dic):
    lst = []
    k = Counter(dic)
    high = k.most_common(10)
    for i in high:
        lst.append([i[0], i[1]])
    return lst


# basic text setting
def text_objects(text, font):
    text = font.render(text, True, black)
    return text, text.get_rect()


# set up the display texts
def display_text():
    # background colour
    gameDisplay.fill(white)

    # big title "LeaderBoard"
    title, title_rect = text_objects("LeaderBoard", pygame.font.Font('freesansbold.ttf', 50))
    title_rect.center = ((display_width / 2), 50)
    gameDisplay.blit(title, title_rect)

    # sub title "player" and "score"
    player_title, player_title_rect = text_objects("Player", pygame.font.Font('freesansbold.ttf', 33))
    player_title_rect.center = (200, 120)
    gameDisplay.blit(player_title, player_title_rect)

    score_title, score_title_rect = text_objects("Score", pygame.font.Font('freesansbold.ttf', 33))
    score_title_rect.center = (600, 120)
    gameDisplay.blit(score_title, score_title_rect)

    # list top10 players and their score
    for i in range(0, 10):
        player, player_rect = text_objects(str((i + 1)) + ". " + player_list(player_dict)[i][0],
                                           pygame.font.Font('freesansbold.ttf', 30))
        player_rect.center = (200, 120 + 44 * (i + 1))
        gameDisplay.blit(player, player_rect)

        score, score_title_rect = text_objects(str(player_list(player_dict)[i][1]),
                                               pygame.font.Font('freesansbold.ttf', 30))
        score_title_rect.center = (600, 120 + 44 * (i + 1))
        gameDisplay.blit(score, score_title_rect)


# making the window
def board():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_text()
        pygame.display.update()
        clock.tick(15)


if __name__ == "__main__":
    board()
    pygame.quit()
    quit()

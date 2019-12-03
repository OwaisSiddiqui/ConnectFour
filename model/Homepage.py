import pygame
from Player import *
from PlayerComputer import *
from PlayerHuman import *

# Initializes the pygame modules
pygame.init()

size = width, height = 1000, 800
screen = pygame.display.set_mode(size) # set up the window of game
pygame.display.set_caption("ConnectFour") # name the window of game
clock = pygame.time.Clock() # set up the game refresh speed

# load the images and assign variables name
bg = pygame.image.load("images/bg_image.jpeg")
bg = pygame.transform.scale(bg, (1000, 800))

play_button = pygame.image.load("images/play_button.png")
play_button = pygame.transform.scale(play_button, (400, 400))

pve_button = pygame.image.load("images/pve_button.png")
pve_button = pygame.transform.scale(pve_button, (450, 75))

pvp_button = pygame.image.load("images/pvp_button.png")
pvp_button = pygame.transform.scale(pvp_button, (450, 75))

leaderboard_button = pygame.image.load("images/leaderboard_button.png")
leaderboard_button = pygame.transform.scale(leaderboard_button, (200, 50))

# The following is the mouse detection structure of home page
#pygame.mouse.set_visible(0)
n1 = True
current = "home"

if __name__ == "__main__":
    while n1:
        clock.tick(30)
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        print(mouse)
        if (325 < mouse[0] < 325 + 355 and 600 < mouse[1] < 600 + 80 and click[0]) and current == "home":
            screen.blit(bg, (0, 0))
            screen.blit(play_button, (300, 600))
            screen.blit(leaderboard_button, (25, 25))
            current = "mode"
        elif current == "mode":
            screen.blit(bg, (0, 0))
            screen.blit(pve_button, (300, 550))
            screen.blit(pvp_button, (300, 675))
            #if 300 < mouse[0] < 300 + 450 and 550 < mouse[1] < 550 + 75:

            #if 300 < mouse[0] < 300 + 450 and 675 < mouse[1] < 675 + 75:

        else:
            screen.blit(bg, (0, 0))
            screen.blit(play_button, (300, 600))
            screen.blit(leaderboard_button, (25, 25))
        #   if 25 < mouse[0] < 25 + 200 and 25 and 25 < mouse[1] < 25 + 45:

        # elif 25 < mouse[0] < 25 + 200 and 25 and 25 < mouse[1] < 25 + 45:
        #     if click[0]:
        #         n1 = False

        # Monitor event
        for event in pygame.event.get():
            # checks if the Event object’s type is equal to the constant QUIT
            if event.type == pygame.QUIT:
                # quit() uninstall all modules
                pygame.quit()
                # exit() directly terminate the current program
                exit()

        pygame.display.update()

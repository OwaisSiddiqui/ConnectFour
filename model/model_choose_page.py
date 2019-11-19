import pygame
import sys


pygame.init()
# Open a window
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
# title
pygame.display.set_caption("Model_choose_page")
# background

bg = pygame.image.load("images/bg_image.jpeg")
bg = pygame.transform.scale(bg, (1000, 800))

pve_button = pygame.image.load("images/pve_button.png")
pve_button = pygame.transform.scale(pve_button, (450, 75))

pvp_button = pygame.image.load("images/pvp_button.png")
pvp_button = pygame.transform.scale(pvp_button, (450, 75))

leaderboard_button = pygame.image.load("images/leaderboard_button.png")
leaderboard_button = pygame.transform.scale(leaderboard_button, (200, 50))


pygame.mouse.set_visible(0)

while True:
    screen.blit(bg, (0, 0))
    screen.blit(pve_button, (300, 550))
    screen.blit(pvp_button, (300, 675))
    screen.blit(leaderboard_button, (25, 25))

    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #elif event.type == pygame.MOUSEBUTTONUP:
            #print(x,y)

    pygame.display.update()
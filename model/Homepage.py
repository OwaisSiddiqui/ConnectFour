import pygame
import sys


pygame.init()
# Open a window
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
# title
pygame.display.set_caption("Home_page")
# background

bg = pygame.image.load("images/bg_image.jpeg")
bg = pygame.transform.scale(bg, (1000, 800))

play_button = pygame.image.load("images/play_button.png")
play_button = pygame.transform.scale(play_button, (400, 400))

leaderboard_button = pygame.image.load("images/leaderboard_button.png")
leaderboard_button = pygame.transform.scale(leaderboard_button, (200, 50))


pygame.mouse.set_visible(0)

while True:
    screen.blit(bg, (0, 0))
    screen.blit(play_button, (300, 600))
    screen.blit(leaderboard_button, (25, 25))

    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #elif event.type == pygame.MOUSEBUTTONUP:
            #print(x,y)

    pygame.display.update()
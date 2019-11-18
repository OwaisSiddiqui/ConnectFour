import pygame
import time
import threading


class Scoreboard:
    """
    Scoreboard involves two parts: Timer & Score
    Timer: 15 seconds to limit player's each move time
    Score: After player(s) finishes the move, the timer would stop and the rest
    of time is player's score

    """
    def __init__(self, player, score):
        self.player = player
        self.score = score
        self.has_move = False


class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sec = 15
        self.has_move = False

    def run(self):
        self.has_move = True
        while self.has_move and self.sec > 0:
            screen.fill(bg)
            display_time = str(player.get_sec())
            self.sec -= 1
            screen.blit(my_font.render(display_time, True, (0, 0, 0)), (10, position))
            pygame.display.update()
            time.sleep(1)

    def moved(self):
        self.has_move = False
        return self.sec

    def get_sec(self):
        return self.sec


# initialize the pygame
pygame.init()
# size
size = width, height = 200, 150
screen = pygame.display.set_mode(size)
# title
pygame.display.set_caption("Timer")
# background
bg = (255, 215, 0)
# font
my_font = pygame.font.Font(None, 100)
# line height
line_height = my_font.get_linesize()
position = 15
screen.fill(bg)

player1 = Scoreboard("name", 0)
while True:
    screen.fill(bg)
    player = Timer()
    player.start()
    e = input("Press Enter")
    player1.score += player.moved()
    print("You got {} score".format(player1.score))

pygame.quit()



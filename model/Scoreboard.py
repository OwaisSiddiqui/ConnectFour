import pygame
import time
from threading import Thread
import threading

SCORE_PLAYER1 = 0
SCORE_PLAYER2 = 0


class Scoreboard:
    """
    Scoreboard involves two parts: Timer & Score
    Timer: 15 seconds to limit player's each move time
    Score: After player(s) finishes the move, the timer would stop and the rest
    of time is player's score

    """
    def __init__(self, x, y):
        self.has_move = False
        self.x = x
        self.y = y
        self.scoreboard_display = pygame.Rect(x, y, 100, 100)
        self.time_display = pygame.font.Font(None, 100)
        self.colour = (255, 215, 0)
        self.total_time = 15
        self.current_time = 15
        self.timer = Timer(self.current_time)
        self.has_move = False
        self.player1_score = 0
        self.player2_score = 0

    def run(self):
        self.timer.run()

    def moved(self):
        self.has_move = False
        return self.current_time

    def get_current_time(self):
        self.update_timer()
        return self.current_time

    def update_timer(self):
        self.current_time = self.timer.get_current_time()

    def stop_timer(self):
        self.timer.stop_timer()

    def get_player_score(self, player):
        if player == "X":
            return self.player1_score
        elif player == "O":
            return self.player2_score


class Timer(Thread):

    def __init__(self, current_time):
        super().__init__()
        self.current_time = current_time
        self.timer_thread = threading.Thread(target=self._run)
        self.is_program_ended = False

    def _run(self):
        while self.current_time > 0 and not self.is_program_ended:
            self.current_time -= 1
            time.sleep(1)

    def run(self):
        self.timer_thread.start()

    def get_current_time(self):
        return self.current_time

    def stop_timer(self):
        self.is_program_ended = True


if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((200, 150))
    scoreboard = Scoreboard(100, 100)
    pygame.display.set_caption("Timer")
    scoreboard.run()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                scoreboard.stop_timer()
                pygame.quit()
                exit()
        display.fill((255, 215, 0))
        display.blit(scoreboard.time_display.render(str(scoreboard.get_current_time()), True, (0, 0, 0)), (10, 15))
        pygame.display.update()

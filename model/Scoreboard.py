import pygame


class Scoreboard:
    """
    Scoreboard involves two parts: Timer & Score
    Timer: 15 seconds to limit player's each move time
    Score: After player(s) finishes the move, the timer would stop and the rest
    of time is player's score

    """
    def __init__(self, player, score):
        self.current_time = pygame.time.Clock()
        # self.total_time =


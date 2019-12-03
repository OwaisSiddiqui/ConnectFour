import Disc


class Player:

    def __init__(self, connect4, player, disc):
        self.connect4 = connect4
        self.player = player
        self.disc = disc

    def get_move(self):
        raise NotImplementedError

    def set_disc(self, color):
        self.disc = Disc(color)
class Player:

    def __init__(self, connect4, player):
        self.connect4 = connect4
        self.player = player

    def get_move(self):
        raise NotImplementedError
class MiniMax:
    def __init__(self, cut_time = -0.01, lim = float("inf")):
        """Initializes variables to help calculate best move"""
        self.cut_time, self.memo, self.lim = cut_time, {}, lim
    
    def play_game(self, game, player):
        return self.mini_max(game, player)[0]
    
    def mini_max(self, game, player, num_moves=0):
        "Function to return best move and score for player in game state"
        if player not in self.memo:
            self.memo[player] = {}
        
        p1_memo = self.memo[player]

        if game not in p1_memo:
            if Board.check_winner(player):
                best_move, best_score = None, Board(player)
            elif num_moves > self.lim:
                best_move, best_score = game.get_moves()[0], 0
            else:
                other_player = [other_player for other_player in game if other_player != player][0]
                valid_moves = game.get_possible_moves()
                best_score = float("-inf")
                sum = 0
                for move in valid_moves:
                    clone = game.copy()
                    clone.move(player, move)
                    player, score = self.mini_max(clone, player=other_player, num_moves=num_moves+1)
                    score *= -1
                    score += self.cut_time * num_moves
                    sum += score

                    if score > best_score:
                        best_score, best_move = score, move
                sum -= best_score # Remove the best score from window sum
                alternate_sum = sum / len(valid_moves) 
                best_score = ((1 - self.weight) * best_score) + (self.weight * alternate_sum)
            self.memo[player][game] = (best_score, best_score)
        return self.memo[player][game] 
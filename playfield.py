import player
import random 

def role_dice():
    return random.randint(1, 6)

class Playfield():
    
    def __init__(self):
        self.index_of_player_to_move = 0
        self.players = []
    
    def add_player_to_playfield(self, player :player.Player):
        self.players.append(player)
    
    def move_to_next_player(self):
        self.index_of_player_to_move = (self.index_of_player_to_move + 1) %len(self.players)
        
    def return_player_to_move(self):
        return self.players[self.index_of_player_to_move]

import player
import random 

class Playfield():
    
    def __init__(self, player_count: int):
        self.player_to_move = 0
        self.player_count = player_count
        self.player_ids = []
    
    def add_player_to_playfield(self, player :player.Player):
        self.player_ids.append(player)
    
    def return_player_how_is_in_charge_to_move(self):
        return self.player_to_move
    
    def role_dice(self):
        return random.randintnd(1, 6)
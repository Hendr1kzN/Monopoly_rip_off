

class Player:
    def __init__(self, player_name, player_model):
        self.player_model = player_model
        self.player_position = 0
        self.money = 1500
        self.bought_items = []
        self.player_name = player_name
    
    def add_money(self, money_added: int):
        self.money += money_added
        
    def give_money(self, money_removed: int):
        self.money -= money_removed
    
    def player_moves(self, number_of_moves: int):
        new_playerpositon = self.player_position + number_of_moves
        if new_playerpositon >= 40:
            self.add_money(200)
        self.player_position = new_playerpositon%40
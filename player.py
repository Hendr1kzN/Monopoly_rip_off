

class Player:
    def __init__(self, player_name, player_model):
        self.player_model = player_model
        self.player_position = 0
        self.money = 1500
        self.bought_items = []
        self.player_name = player_name
        self.rounds_in_jail = 0
    
    def add_money(self, money_added: int):
        self.money += money_added
        
    def pay_money(self, money_removed: int):
        self.money -= money_removed
    
    def player_moves(self, number_of_moves: int):
        if self.player_position == 40:
            self.player_position = 10
        new_playerpositon = self.player_position + number_of_moves
        if new_playerpositon >= 40:
            self.add_money(200)
        self.player_position = new_playerpositon%40
    
    def go_to_jail(self):
        self.player_position = 40
        
    def do_action_on_current_field(self):
        pass
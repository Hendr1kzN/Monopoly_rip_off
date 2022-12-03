

class Player:
    def __init__(self, player_id, player_name):
        self.money = 1,500
        self.bought_items = []
        self.player_id = player_id
        self.player_name = player_name
    
    def do_transaction(self, money_added :int):
        self.money += money_added
    
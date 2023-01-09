class Square:
    def __init__(self, name, square_type, price, cordx, cordy):
        self.name = name
        self.type = square_type
        self.price = price
        self.owner = None
        self.cordx = cordx
        self.cordy = cordy

    def land_on(self, player):
        if self.type == "property":
            if self.owner is None:
                # Offer to buy property
                pass
            elif self.owner == player:
                # You already own this property
                pass
            else:
                # Pay rent
                pass
        elif self.type == "payment":
            # player needs to pay price
            pass
        elif self.type == "chance":
            # Draw a chance card
            pass
        elif self.type == "community chest":
            # Draw a community chest card
            pass
        elif self.type == "go to jail":
            # Go to jail
            pass
    
    def __str__(self):
        return "name: "+ self.name + ", type: " + str(self.type) + ", price: " + str(self.price) + ", owner: " + str(self.owner)
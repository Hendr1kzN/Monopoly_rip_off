# importing pygame module
import pygame
import playfield
import player
import positions
import sys

class Monopoly_bord:
    def __init__(self):
        pygame.init()
        self.list_of_texts = []
        self.list_of_textRects = []
        self.count_doubles = 0
        self.white = (255, 255, 255)
        self.blue = (0, 0, 128)
        self.playfield = playfield.Playfield()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.__create_display()
        self.__init_the_static_texts()
        self.__init_flexible_text()

    def __create_display(self):
        self.display = pygame.display
        pygame.display.set_caption('The Capitalism Game')
        self.surface = self.display.set_mode((1200, 1000))
        self.backgroud_pickture = pygame.image.load("images\The_Capitalism_game_board_1000x1000.png")
        
    def add_players(self, list_of_players):
        for user in list_of_players:
            player_avatar = pygame.image.load(f"Avatars/{user}_avatar.jpg")
            player = player.Player(user.name, player_avatar)
            self.playfield.add_player_to_playfield(player)

    def __render_text_in_blue(self, text: str, x_coord: int, y_coord: int):
        text_with_font = self.font.render(text, True, self.blue)
        textRect = text_with_font.get_rect()
        textRect.center = (x_coord, y_coord)
        return text_with_font, textRect

    def __render_all_texts(self):
        if len(self.list_of_texts) == len(self.list_of_textRect):
            for i in len(self.list_of_texts):
                self.surface.blit(self.list_of_texts[i], self.list_of_textRect[i])
        else:
            raise Exception(f"The list_of_text and list_of_textRect have differet sizes. list_of_text size: {len(self.list_of_texts)}, listof_textRect: {len(self.list_of_textRect)}")

    def __add_text_and_textRect(self, tupel_of_text_and_textRect):
        self.list_of_texts.append(tupel_of_text_and_textRect[0]) 
        self.list_of_textRects.append(tupel_of_text_and_textRect[1])
    
    def __init_the_static_texts(self):
        self.__add_text_and_textRect(self.__render_text_in_blue('', 330, 170))
        self.__add_text_and_textRect(self.__render_text_in_blue('Player in', 1100, 16))
        self.__add_text_and_textRect(self.__render_text_in_blue('charge:', 1100, 50))
        self.__add_text_and_textRect(self.__render_text_in_blue('money:', 1100, 152))

    def __init_flexible_text(self):
        self.__add_text_and_textRect(self.__render_text_in_blue("", 1100, 84))
        self.__add_text_and_textRect(self.__render_text_in_blue('€', 1100, 186))
        
    def start_turn_by_rolling_dice(self):
        dice1 = playfield.role_dice()
        dice2 = playfield.role_dice()
        self.list_of_texts[0] = self.font.render(('you roled a: ' + str(dice1) + ' + '+ str(dice2) +' = ' + str (dice1+dice2)), True, self.blue)
        return dice1, dice2
    
    def dice_roll(self):
            dice1, dice2= self.start_turn_by_rolling_dice()
                
            if self.playfield.return_player_to_move().player_position == 40:
                if dice1 == dice2:
                    self.playfield.return_player_to_move().player_moves(dice1+dice2)
                    
                elif self.playfield.return_player_to_move().rounds_in_jail >= 2:
                    self.playfield.return_player_to_move().pay_money(50)
                    self.playfield.return_player_to_move().player_moves(dice1+dice2)
                        
                else:
                    self.playfield.return_player_to_move().rounds_in_jail += 1
                    self.playfield.move_to_next_player()
                
            else:
                if self.count_doubles >= 2 and dice1 == dice2:
                    self.playfield.return_player_to_move().go_to_jail()
                    self.playfield.move_to_next_player()
                else:
                    self.playfield.return_player_to_move().player_moves(dice1+ dice2)
                
                    if dice1 != dice2:
                        self.count_doubles = 0
                        self.playfield.move_to_next_player()
                    else:
                        self.count_doubles += 1
                self.list_of_texts[-1], self.list_of_textRects[-1] = self.__render_text_in_blue(str(self.playfield.return_player_to_move().money) + '€', 1100, 186)

    def set_flexible_text(self):
        self.list_of_texts[-2], self.list_of_textRects[-2] = (self.__render_text_in_blue(self.playfield.return_player_to_move().player_name, 1100, 84))
        self.list_of_texts[-1], self.list_of_textRects[-1] = (self.__render_text_in_blue(str(self.playfield.return_player_to_move().money) + '€', 1100, 186))
    
    def put_current_player_in_jail(self):
        self.playfield.return_player_to_move().go_to_jail()
        self.playfield.move_to_next_player()
    
    def __render_all_texts(self):
        if len(self.list_of_texts) == len(self.list_of_textRects):
            for i in range(len(self.list_of_texts)):
                self.surface.blit(self.list_of_texts[i], self.list_of_textRects[i])
        else:
            raise Exception(f"The list_of_text and list_of_textRect have differet sizes. list_of_text size: {len(self.list_of_texts)}, listof_textRect: {len(self.list_of_textRects)}")
         
    def create_the_visual_playfield(self):
        self.surface.fill(self.white)
        self.surface.blit(self.backgroud_pickture, (0, 0))
        self.__render_all_texts()
        if len(self.playfield.players) > 0:
            for player_on_playfield in self.playfield.players:
                self.surface.blit(player_on_playfield.player_model, positions.positions[player_on_playfield.player_position])
    
    def update_board(self):
        self.display.update()
            
    def create_an_image_of_the_playfield(self):
        pygame.image.save(self.surface, "GameStates/current_Playfield.png")



#shows me that it works
male1 = pygame.image.load("images\Character\8Pixel_gamecharacter_male1.png")
female2 = pygame.image.load("images\Character\8Pixel_gamecharacter_female2.png")
p1 = player.Player("1", male1)
p2 = player.Player("Player", female2)
list_of_player = [p1, p2]

board = Monopoly_bord()
board.playfield.add_player_to_playfield(p1)
board.playfield.add_player_to_playfield(p2)
# gameloop
while True:
    board.set_flexible_text()
    # handel events
    for event in pygame.event.get():
		
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_UP:
                board.dice_roll()
            
            if event.key == pygame.K_DOWN:
                board.put_current_player_in_jail()
    
    board.create_the_visual_playfield()
    
    board.create_an_image_of_the_playfield()
    
    board.update_board()
# importing pygame module
import pygame
import playfield
import player
import positions
import sys



pygame.init()

white = (255, 255, 255)
blue = (0, 0, 128)

# creating display
display = pygame.display
pygame.display.set_caption('The Capitalism Game')
surface = display.set_mode((1200, 1000))
backgroud_pickture = pygame.image.load("images\The_Capitalism_game_board_1000x1000.png")

font = pygame.font.Font('freesansbold.ttf', 32)

#gamecharacter_female1 = pygame.image.load("images\Character\8Pixel_gamecharacter_female1.png")
#gamecharacter_female2 = pygame.image.load("images\Character\8Pixel_gamecharacter_female2.png")
#gamecharacter_female3 = pygame.image.load("images\Character\8Pixel_gamecharacter_female3.png")
#gamecharacter_male1 = pygame.image.load("images\Character\8Pixel_gamecharacter_male1.png")
#gamecharacter_male2 = pygame.image.load("images\Character\8Pixel_gamecharacter_male2.png")
#gamecharacter_male3 = pygame.image.load("images\Character\8Pixel_gamecharacter_male3.png")

def render_text_in_blue(text: str, x_coord: int, y_coord: int):
    text_with_font = font.render(text, True, blue)
    textRect = text_with_font.get_rect()
    textRect.center = (x_coord, y_coord)
    return text_with_font, textRect

def add_to_lists(list1, list2, object1, object2):
    list1.append(object1)
    list2.append(object2)


def render_all_texts(list_of_texts, list_of_textRect):
    if len(list_of_texts) == len(list_of_textRect):
        for i in len(list_of_texts):
            surface.blit(list_of_texts[i], list_of_textRect[i])
    else:
        raise Exception(f"The list_of_text and list_of_textRect have differet sizes. list_of_text size: {len(list_of_texts)}, listof_textRect: {len(list_of_textRect)}")
        
list_of_text = []
list_of_textRect = []

text_dice_role, textRect_dice_role = render_text_in_blue('', 330, 170)

text_player_in_charge, textRect_player_in_charge = render_text_in_blue('Player in', 1100, 16)

text_player_in_charge_pt2, textRect_player_in_charge_pt2 = render_text_in_blue('charge:', 1100, 50)

text_money_to_see_how_much_money_set_player_has, textRect_money_to_see_how_much_money_set_player_has = render_text_in_blue('money:', 1100, 152)


def add_players_to_playfield(list_of_players):
    playfield_to_add_players_to = playfield.Playfield()
    for user in list_of_players:
        player_avatar = pygame.image.load(f"Avatars/{user}_avatar.jpg")
        player = player.Player(user.name, player_avatar)
        playfield_to_add_players_to.add_player_to_playfield(player)
    return playfield_to_add_players_to

#current_playfield = add_players_to_playfield()# the discord bot needs to fill in the players
current_playfield = playfield.Playfield()

count_doubles = 0

# gameloop
while True:
    # set text on the right of playfield
    text_player_name, textRect_player_name = render_text_in_blue(current_playfield.return_player_to_move().player_name, 1100, 84)
    
    text_money_of_player, textRect_money_of_player = render_text_in_blue(str(current_playfield.return_player_to_move().money) + '€', 1100, 186)
    
    # handel events
    for event in pygame.event.get():
		
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
        # creating dice role
            if event.key == pygame.K_UP:
                dice1 = playfield.role_dice()
                dice2 = playfield.role_dice()
                text_to_show_dice_role = font.render(('you roled a: ' + str(dice1) + ' + '+ str(dice2) +' = ' + str (dice1+dice2)), True, blue)
                
                
                if current_playfield.return_player_to_move().player_position == 40:
                    if dice1 == dice2:
                        current_playfield.return_player_to_move().player_moves(dice1+dice2)
                    
                    elif current_playfield.return_player_to_move().rounds_in_jail >= 2:
                        current_playfield.return_player_to_move().pay_money(50)
                        current_playfield.return_player_to_move().player_moves(dice1 +dice2)
                        
                    else:
                        current_playfield.return_player_to_move().rounds_in_jail += 1
                    current_playfield.move_to_next_player()
                
                else:
                    if count_doubles >= 2 and dice1 == dice2:
                        current_playfield.return_player_to_move().go_to_jail()
                        current_playfield.move_to_next_player()
                    else:
                        current_playfield.return_player_to_move().player_moves(dice1+ dice2)
                
                    if dice1 != dice2:
                        count_doubles = 0
                        current_playfield.move_to_next_player()
                    else:
                        count_doubles += 1
                text_money_of_player = font.render(str(current_playfield.return_player_to_move().money) + '€', True, blue)
                
            if event.key == pygame.K_DOWN:
                current_playfield.return_player_to_move().go_to_jail()
                current_playfield.move_to_next_player()
    
    surface.fill(white)
    surface.blit(backgroud_pickture, (0, 0))
    surface.blit(text_to_show_dice_role, textRect_dice_role)
    surface.blit(text_player_in_charge, textRect_player_in_charge)
    surface.blit(text_player_in_charge_pt2, textRect_player_in_charge_pt2)
    surface.blit(text_player_name, textRect_player_name)
    surface.blit(text_money_to_see_how_much_money_set_player_has, textRect_money_to_see_how_much_money_set_player_has)
    surface.blit(text_money_of_player, textRect_money_of_player)
    for player in current_playfield.players:
        surface.blit(player.player_model, positions.positions[player.player_position])
    
    pygame.image.save(surface, "GameStates/current_Playfield.png")
    
    display.update()
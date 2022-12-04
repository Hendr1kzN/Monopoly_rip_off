# importing pygame module
import pygame
import playfield
import player
import positions

# importing sys module
import sys

# initialising pygame
pygame.init()

white = (255, 255, 255)
blue = (0, 0, 128)

# creating display
display = pygame.display
pygame.display.set_caption('The Capitalism Game')
surface = display.set_mode((1200, 1000))
backgroud_pickture = pygame.image.load("images\The_Capitalism_game_board_1000x1000.png")

font = pygame.font.Font('freesansbold.ttf', 32)

gamecharacter_female1 = pygame.image.load("images\Character\8Pixel_gamecharacter_female1.png")
gamecharacter_female2 = pygame.image.load("images\Character\8Pixel_gamecharacter_female2.png")
gamecharacter_female3 = pygame.image.load("images\Character\8Pixel_gamecharacter_female3.png")
gamecharacter_male1 = pygame.image.load("images\Character\8Pixel_gamecharacter_male1.png")
gamecharacter_male2 = pygame.image.load("images\Character\8Pixel_gamecharacter_male2.png")
gamecharacter_male3 = pygame.image.load("images\Character\8Pixel_gamecharacter_male3.png")


text_to_show_dice_role = font.render('', True, blue)
textRect_dice_role = text_to_show_dice_role.get_rect()
textRect_dice_role.center = (330, 170)

text_player_in_charge = font.render('Player in', True, blue)
textRect_player_in_charge = text_player_in_charge.get_rect()
textRect_player_in_charge.center = (1100, 16)

text_player_in_charge_pt2 = font.render('charge:', True, blue)
textRect_player_in_charge_pt2 = text_player_in_charge_pt2.get_rect()
textRect_player_in_charge_pt2.center = (1100, 50)

text_money_to_see_how_much_money_set_player_has = font.render('money:', True, blue)
textRect_money_to_see_how_much_money_set_player_has = text_money_to_see_how_much_money_set_player_has.get_rect()
textRect_money_to_see_how_much_money_set_player_has.center = (1100, 118)

current_playfield = playfield.Playfield()
p1 = player.Player('p1', gamecharacter_female1)
p2 = player.Player('player2', gamecharacter_male1)
current_playfield.add_player_to_playfield(p1)
current_playfield.add_player_to_playfield(p2)


# gameloop
while True:
    # set text on the right of playfield
    text_player_name = font.render(current_playfield.return_player_to_move().player_name, True, blue)
    textRect_player_name = text_player_name.get_rect()
    textRect_player_name.center = (1100, 84)
    
    text_money_of_player = font.render(str(current_playfield.return_player_to_move().money) + '€', True, blue)
    textRect_money_of_player = text_money_of_player.get_rect()
    textRect_money_of_player.center = (1100, 152)
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
                
                text_to_show_dice_role = font.render(('you roled a: '+str(dice1) + ' + '+ str(dice2) +' = ' + str (dice1+dice2)), True, blue)
                
                current_playfield.players[current_playfield.player_to_move].player_moves(dice1+ dice2)
                text_money_of_player = font.render(str(current_playfield.return_player_to_move().money) + '€', True, blue)
                
                current_playfield.move_to_next_player()
                
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
    
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
    
    display.update()
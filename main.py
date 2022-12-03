# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# gameloop
while True:


    for event in pygame.event.get():
        
		
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
		# checking if keydown event happened or not
            if event.key == pygame.K_UP:
		
			# if keydown event happened
			# than printing a string to output
                print("A key has been pressed")
            if event.key == pygame.K_DOWN:
                pass
        
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass

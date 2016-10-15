import pygame
import sys
from pygame.locals import *

pygame.init()

# game screen init
scr_w = 800
scr_h = 500
screen = pygame.display.set_mode((scr_w, scr_h))

def draw_game():
	' Draws the main components of the game '
	
	


def main():
	' Loops the game until user quits '

	game_loop = True

	# running game
	while game_loop:
		# keyboard, mouse & misc events
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				game_loop = False

			if e.type == pygame.KEYDOWN:
				pass

		# draw the game
		draw_game()
    

	# game exit
	pygame.quit()
	sys.exit()


# this is to just test the program
# the main will be called from
# other program
main()

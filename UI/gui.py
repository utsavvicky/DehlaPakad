import pygame
import sys
from pygame.locals import *
from pygame import *

pygame.init()

# game screen init
scr_w = 800
scr_h = 500
screen = pygame.display.set_mode((scr_w, scr_h))

def draw_game():
	' Draws the main components of the game '
	
	# drawing 'Score & Info' at right top
	font = pygame.font.SysFont('dejavuserif', 20)
	score_label = font.render("Score", True, (255,255,255))
	screen.blit(score_label, (600, 10))

	# drawing 'Card Table' in the center
	draw.rect(screen, (200, 0, 0), (100, 100, 600, 300), 10)
	draw.rect(screen, (0, 200, 0), (110, 110, 580, 280))

	pygame.display.update()


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

#* ==========================================================================
#* Universidade Federal de Sao Carlos - Campus Sorocaba
#*
#* Project Name - Snake Game
#*
#* Name: Gabriel Stankevix 
#* email: gabriel.soares@dcomp.sor.ufscar.br
#* ========================================================================== */

# ======================IMPORT=============================

import pygame
import random
# ===================INIT MODULES========================

#initiate all the module
pygame.init()

# =======================SETUP==============================
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

#Change the title of the window
pygame.display.set_caption('Snake Game')

snakeImage = pygame.image.load('snake.png')
foodImage = pygame.image.load('Food.png')

clock = pygame.time.Clock()
crashed = False

x = (display_width * 0.45)
y = (display_height * 0.8)

# =======================FUNCTIONS==============================

def food():
	x = random.uniform(0,600)
	y = random.uniform(0,800)
	gameDisplay.blit(foodImage,(x,y))


def snake(x,y):
	#drawing background stuffs
	gameDisplay.blit(snakeImage,(x,y))


def eventKeyboard(x,y):
	if event.type == pygame.KEYDOWN:
		##if event.key == pygame.K_DOWN:
			#y=y-5
		#elif event.key == pygame.K_UP:
			#y=y+5
		if event.key == pygame.K_LEFT:
			x-=5
		elif event.key == pygame.K_RIGHT:
			x+=5

while not crashed:
	#get any event (click/keyboard)
	#create a list of events per frame
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-=5
			elif event.key == pygame.K_RIGHT:
				x+=5

		
	gameDisplay.fill(white)
	snake(x,y)
	#food()
	pygame.display.update()
	#define the number of frame per second
	clock.tick(60)

pygame.quit()
quit()










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


x = (display_width * 0.45)
y = (display_height * 0.8)
x_food = random.uniform(0,600)
y_food = random.uniform(0,800)

crashed = False
flag_Left = False
flag_Right = False
flag_Down = False
flag_UP = False
eat = False

# =======================FUNCTIONS==============================

def food():
	gameDisplay.blit(foodImage,(x_food,y_food))
	
def snake(x,y):
	#drawing background stuffs
	gameDisplay.blit(snakeImage,(x,y))

while not crashed:

	#get any event (click/keyboard)
	#create a list of events per frame
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-=1
				flag_UP = False
				flag_Left = True
				flag_Right = False
				flag_Down = False
			elif event.key == pygame.K_RIGHT:
				x+=1
				flag_UP = False
				flag_Left = False
				flag_Right = True
				flag_Down = False
			elif event.key == pygame.K_UP:
				y-=1
				flag_UP = True
				flag_Left = False
				flag_Right = False
				flag_Down = False
			elif event.key == pygame.K_DOWN:
				y+=1
				flag_UP = False
				flag_Left = False
				flag_Right = False
				flag_Down = True
	
	#Colision
	print int(x), int(y), int(x_food), int(y_food)
	if (int(x) <= int(x_food+1) or int(x)>= int(x_food-1)) and (int(y) <= int(y_food+1) and int(y) <= int(y_food-1)):
		print "Colid"
		x_food = random.uniform(0,600)
		y_food = random.uniform(0,800)

	gameDisplay.fill(white)
	food()
	snake(x,y)
	pygame.display.update()
	#define the number of frame per second
	clock.tick(60)

	#Movement of the snake
	if flag_UP == True:
		y-=1
	elif flag_Down == True:
		y+=1
	elif flag_Right == True:
		x+=1
	elif flag_Left == True:
		x-=1

	
		

pygame.quit()
quit()










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
import sys

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
background = pygame.image.load('background.jpg')

clock = pygame.time.Clock()
f = pygame.font.SysFont('comicsansms', 40);

#Size of snake
x = [290, 290]
y = [290, 270]


#x = (display_width * 0.45)
#y = (display_height * 0.8)
x_food = random.uniform(0,600)
y_food = random.uniform(0,800)

score = 0
speed = 1
crashed = False
flag_Left = False
flag_Right = False
flag_Down = False
flag_UP = False
eat = False

# =======================FUNCTIONS==============================

#This function draws the food :)
def food():
	gameDisplay.blit(foodImage,(x_food,y_food))

#This function draws the snake	
def snake(x,y):
	for i in range(0, len(x)):
		gameDisplay.blit(snakeImage,(x[i],y[i]))

#When the snake dies, this function shows the final scores and finish the game
def die(screen, score):
	f=pygame.font.SysFont('Arial', 30);
	t=f.render('Your score was: '+str(score), True, (0, 0, 0));
	screen.blit(t, (10, 270));
	pygame.display.update();
	pygame.time.wait(2000);
	sys.exit(0)


#Main Function, Loop Game and Collide
if __name__ == '__main__':

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
		#if (int(x) <= int(x_food+2) and int(x)>= int(x_food-2)) and (int(y) <= int(y_food+2) and int(y) <= int(y_food)):
			#x_food = random.uniform(0, 400)
			#y_food = random.uniform(0,400)
			#speed+=0.2

		#if int(x) >= 800 or int(y) >= 600 or int(x) <= 0 or int(y) <= 0:
			#crashed = True	


		#gameDisplay.fill(white)
		gameDisplay.blit(background,(0,0))
		food()
		snake(x,y)
		

		#define the number of frame per second
		clock.tick(60)

		#Movement of the snake
		if flag_UP == True:
			y-=(1*speed)
		elif flag_Down == True:
			y+=(1*speed)
		elif flag_Right == True:
			x+=(1*speed)
		elif flag_Left == True:
			x-=(1*speed)

		displayScore = f.render('SCORE: '+str(score), True, (0, 0, 0))
		gameDisplay.blit(displayScore, (10, 10))

		pygame.display.update()

pygame.quit()
quit()










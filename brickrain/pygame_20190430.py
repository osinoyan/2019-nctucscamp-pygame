import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

gameOver = False

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Source Code Pro for Powerline', 30)
textSur = myfont.render('How are you today?', False, (0, 200, 100))
screen.blit(textSur, (400, 300))

while not gameOver:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.update()
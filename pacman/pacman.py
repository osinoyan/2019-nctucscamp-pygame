import pygame
import sys

class player():
	def __init__(self, position):
		self.position = position
		self.image = pygame.image.load('pac.png')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.speed = 2
		self.collider = pygame.Rect((position[0], position[1]), (50, 50))
	def move(self, direction):
		if direction == 'left':
			self.position[0] -= self.speed
		elif direction == 'right':
			self.position[0] += self.speed
		elif direction == 'up':
			self.position[1] -= self.speed
		elif direction == 'down':
			self.position[1] += self.speed
		self.position = reachwall(self.position, direction)
		self.collider.top = self.position[0]
		self.collider.left = self.position[1]

class ghost():
	def __init__(self, position):
		self.position = position
		self.image = pygame.image.load('ghost.png')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.speed = 2
		self.collider = pygame.Rect((position[0], position[1]), (50, 50))
	def move(self, direction):
		if direction == 'left':
			self.position[0] -= self.speed
		elif direction == 'right':
			self.position[0] += self.speed
		elif direction == 'up':
			self.position[1] -= self.speed
		elif direction == 'down':
			self.position[1] += self.speed
		self.collider.top = self.position[0]
		self.collider.left = self.position[1]

def getmap(filename):
	f = open(filename, 'r')
	L = f.readlines()
	for i in L:
		x = []
		for j in i:
			x.append(j)
		Map.append(x)

def updateframe(A, B):
	if not (len(Map) == 0):
		for i in range(0, len(Map)):
			for j in range(0, len(Map[i])):
				if Map[i][j] == 'X':
					screen.blit(wall, (j*50, i*50))
				else:
					screen.blit(ground, (j*50, i*50))
	else:
		screen.fill((0, 0, 0))
	screen.blit(A.image, (A.position[0], A.position[1]))
	screen.blit(B.image, (B.position[0], B.position[1]))
	pygame.display.update()

def reachwall(position, direction):
	if direction == 'left':
		if Map[position[1]//50][position[0]//50] == 'X':
			return [(position[0]//50+1)*50, position[1]]
	if direction == 'right':
		if Map[position[1]//50][position[0]//50+1] == 'X':
			return [(position[0]//50)*50, position[1]]
	if direction == 'up':
		if Map[position[1]//50][position[0]//50] == 'X':
			return [position[0], (position[1]//50+1)*50]
	if direction == 'down':
		if Map[position[1]//50+1][position[0]//50] == 'X':
			return [position[0], (position[1]//50)*50]
	return [position[0], position[1]]

pygame.init()
Map = []
getmap('map.txt')
ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (50, 50))
wall = pygame.image.load('wall.png')
wall = pygame.transform.scale(wall, (50, 50))
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
A = player([400, 300])
B = ghost([100, 100])
game_over = False
left = False
right = False
down = False
up = False

while not game_over:
	if A.collider.colliderect(B.collider):
		game_over = True
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] and A.position[0] >= 0:
		A.move('left')
	elif key[pygame.K_RIGHT] and A.position[0] <= width-50:
		A.move('right')
	elif key[pygame.K_UP] and A.position[1] >= 0:
		A.move('up')
	elif key[pygame.K_DOWN] and A.position[1] <= height-50:
		A.move('down')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	updateframe(A, B)
print('Game Over')
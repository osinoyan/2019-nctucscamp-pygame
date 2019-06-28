import pygame
import random

class princess():
	def __init__(self):
		self.direction = 'down'
		self.count = 0

		self.frameUP = [0, 0, 0, 0]
		self.frameUP[0] = pygame.image.load('P_up0.png')
		self.frameUP[1] = pygame.image.load('P_up1.png')
		self.frameUP[2] = pygame.image.load('P_up0.png')
		self.frameUP[3] = pygame.image.load('P_up2.png')

		self.frameDOWN = [0, 0, 0, 0]
		self.frameDOWN[0] = pygame.image.load('P_down0.png')
		self.frameDOWN[1] = pygame.image.load('P_down1.png')
		self.frameDOWN[2] = pygame.image.load('P_down0.png')
		self.frameDOWN[3] = pygame.image.load('P_down2.png')

		self.frameLEFT = [0, 0, 0, 0]
		self.frameLEFT[0] = pygame.image.load('P_left0.png')
		self.frameLEFT[1] = pygame.image.load('P_left1.png')
		self.frameLEFT[2] = pygame.image.load('P_left0.png')
		self.frameLEFT[3] = pygame.image.load('P_left2.png')

		self.frameRIGHT = [0, 0, 0, 0]
		self.frameRIGHT[0] = pygame.image.load('P_right0.png')
		self.frameRIGHT[1] = pygame.image.load('P_right1.png')
		self.frameRIGHT[2] = pygame.image.load('P_right0.png')
		self.frameRIGHT[3] = pygame.image.load('P_right2.png')

		for f in self.frameUP:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
		for f in self.frameDOWN:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
		for f in self.frameLEFT:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
		for f in self.frameRIGHT:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()

	def animation(self, direction):
		if direction == self.direction:
			self.count = (self.count + 1) % 4
		else:
			self.direction = direction
			self.count = 0

		if self.direction == 'up':
			return self.frameUP[self.count]
		elif self.direction == 'down':
			return self.frameDOWN[self.count]
		elif self.direction == 'left':
			return self.frameLEFT[self.count]
		elif self.direction == 'right':
			return self.frameRIGHT[self.count]

class ghost():
	def __init__(self):
		self.direction = 'down'
		self.count = 0

		self.frameUP = [0, 0, 0, 0]
		self.frameUP[0] = pygame.image.load('G_up0.png')
		self.frameUP[1] = pygame.image.load('G_up1.png')
		self.frameUP[2] = pygame.image.load('G_up0.png')
		self.frameUP[3] = pygame.image.load('G_up2.png')

		self.frameDOWN = [0, 0, 0, 0]
		self.frameDOWN[0] = pygame.image.load('G_down0.png')
		self.frameDOWN[1] = pygame.image.load('G_down1.png')
		self.frameDOWN[2] = pygame.image.load('G_down0.png')
		self.frameDOWN[3] = pygame.image.load('G_down2.png')

		self.frameLEFT = [0, 0, 0, 0]
		self.frameLEFT[0] = pygame.image.load('G_left0.png')
		self.frameLEFT[1] = pygame.image.load('G_left1.png')
		self.frameLEFT[2] = pygame.image.load('G_left0.png')
		self.frameLEFT[3] = pygame.image.load('G_left2.png')

		self.frameRIGHT = [0, 0, 0, 0]
		self.frameRIGHT[0] = pygame.image.load('G_right0.png')
		self.frameRIGHT[1] = pygame.image.load('G_right1.png')
		self.frameRIGHT[2] = pygame.image.load('G_right0.png')
		self.frameRIGHT[3] = pygame.image.load('G_right2.png')

		for f in self.frameUP:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
		for f in self.frameDOWN:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
		for f in self.frameLEFT:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
		for f in self.frameRIGHT:
			f = pygame.transform.scale(f, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()

	def animation(self, direction):
		if direction == self.direction:
			self.count = (self.count + 1) % 4
		else:
			self.direction = direction
			self.count = 0

		if self.direction == 'up':
			return self.frameUP[self.count]
		elif self.direction == 'down':
			return self.frameDOWN[self.count]
		elif self.direction == 'left':
			return self.frameLEFT[self.count]
		elif self.direction == 'right':
			return self.frameRIGHT[self.count]

class player():
	def __init__(self, charactor):
		self.position = [0, 0]
		if charactor == 'princess':
			self.charactor = princess()
		elif charactor == 'ghost':
			self.charactor = ghost()
		self.image = self.charactor.frameDOWN[0]
		#self.image = pygame.image.load('pac.png')
		#self.image = pygame.transform.scale(self.image, (BLOCK_LENGTH, BLOCK_LENGTH))
		self.speed = 2
		self.collider = pygame.Rect((self.position[0], self.position[1]), (BLOCK_LENGTH, BLOCK_LENGTH))

	def setPos(self, position):
		self.position = position
		self.collider.top = self.position[0]
		self.collider.left = self.position[1]

	def move(self, direction):
		if direction == 'left':
			self.position[0] -= self.speed
		elif direction == 'right':
			self.position[0] += self.speed
		elif direction == 'up':
			self.position[1] -= self.speed
		elif direction == 'down':
			self.position[1] += self.speed
		self.position = reachwall(self.collider, self.position, direction)
		self.setPos()

class enemy():
	def __init__(self, charactor):
		self.position = [0, 0]
		if charactor == 'princess':
			self.charactor = princess()
		elif charactor == 'ghost':
			self.charactor = ghost()
		self.image = self.charactor.frameDOWN[0]
		#self.image = pygame.image.load('pac.png')
		#self.image = pygame.transform.scale(self.image, (BLOCK_LENGTH, BLOCK_LENGTH))
		self.speed = 2
		self.collider = pygame.Rect((self.position[0], self.position[1]), (BLOCK_LENGTH, BLOCK_LENGTH))

	def setPos(self):
		self.collider.top = self.position[0]
		self.collider.left = self.position[1]

	def move(self, direction):
		if direction == 'left':
			self.position[0] -= self.speed
		elif direction == 'right':
			self.position[0] += self.speed
		elif direction == 'up':
			self.position[1] -= self.speed
		elif direction == 'down':
			self.position[1] += self.speed
		self.setPos()		

def init():
	#載入地圖圖片
	ground = pygame.image.load('ground.png')
	ground = pygame.transform.scale(ground, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()
	wall = pygame.image.load('wall.png')
	wall = pygame.transform.scale(wall, (BLOCK_LENGTH, BLOCK_LENGTH)).convert()

	#繪製地圖
	if not (len(Map) == 0):
		for i in range(0, len(Map)):
			for j in range(0, len(Map[i])):
				if not(Map[i][j] == '.'):
					background.blit(wall, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
				else:
					background.blit(ground, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))

	#隨機生成玩家位置
	A_PosX, A_PosY = 0, 0
	while not Map[A_PosY][A_PosX] == '.':
		A_PosX = random.randint(1, len(Map[0])-2)
		A_PosY = random.randint(1, len(Map)-2)

	#隨機生成敵人位置
	B_PosX, B_PosY = 0, 0
	while (not Map[B_PosY][B_PosX] == '.') or (B_PosX == A_PosX and B_PosY == A_PosY):
		B_PosX = random.randint(1, len(Map[0])-2)
		B_PosY = random.randint(1, len(Map)-2)

	#更新玩家與敵人位置
	A.position = [A_PosX*BLOCK_LENGTH, A_PosY*BLOCK_LENGTH]
	A.setPos()
	B.position = [B_PosX*BLOCK_LENGTH, B_PosY*BLOCK_LENGTH]
	B.setPos()

def getmap(filename):
	f = open(filename, 'r')
	L = f.readlines()
	for i in range(0, len(L)):
		x = []
		for j in range(0, len(L[i])):
			if L[i][j] == 'X':
				c = pygame.Rect((i*BLOCK_LENGTH, j*BLOCK_LENGTH), (BLOCK_LENGTH, BLOCK_LENGTH))
				x.append(c)
			else:
				x.append(L[i][j])
		Map.append(x)

def inRect(position, rect):
	if position[0] in range(rect.left, rect.right) and position[1] in range(rect.top, rect.bottom):
		return True
	else:
		return False

def updateframe(A, B):
	screen.blit(background, (0, 0))
	screen.blit(A.image, (A.position[0], A.position[1]))
	screen.blit(B.image, (B.position[0], B.position[1]))
	pygame.display.update()

def reachwall(collider, position, direction):
	newpos = position
	x = [position[0]//BLOCK_LENGTH, position[1]//BLOCK_LENGTH]
	state = [0, 0, 0, 0]
	for i in range(0, 2):
		for j in range(0, 2):
			#print(x[1]+i, x[0]+j)
			if Map[x[1]+i][x[0]+j] == '.':
				pass
			elif collider.colliderect(Map[x[1]+i][x[0]+j]):
				state[i*2+j] = 1
	#print(state)
	if state[0] and state[1]:
		newpos[1] = (x[1]+1) * BLOCK_LENGTH
	if state[2] and state[3]:
		newpos[1] = x[1] * BLOCK_LENGTH
	if state[0] and state[2]:
		newpos[0] = (x[0]+1) * BLOCK_LENGTH
	if state[1] and state[3]:
		newpos[0] = x[0] * BLOCK_LENGTH

	if (sum(state)) <= 1:
		if (state[0] or state[2]) and direction == 'left':
			newpos[0] = (x[0]+1) * BLOCK_LENGTH
		if (state[0] or state[1]) and direction == 'up':
			newpos[1] = (x[1]+1) * BLOCK_LENGTH
		if (state[1] or state[3]) and direction == 'right':
			newpos[0] = x[0] * BLOCK_LENGTH
		if (state[2] or state[3]) and direction == 'down':
			newpos[1] = x[1] * BLOCK_LENGTH
	return newpos

def start():
	#起始畫面圖片
	startImg = pygame.image.load('start.jpg').convert()
	global running

	#顯示按鈕
	myfont = pygame.font.SysFont("Arial", 24)
	text_princess = myfont.render('Be a princess', True, (0, 0, 0))
	text_ghost = myfont.render('Be a ghost', True, (255, 0, 0))
	P_rect = pygame.Rect((620, 480), (300, 80))
	textP_rect = text_princess.get_rect( center = P_rect.center )
	G_rect = pygame.Rect((50, 50), (300, 80))
	textG_rect = text_ghost.get_rect( center = G_rect.center )

	#判斷
	while running:
		screen.blit(startImg, (0, 0))
		Mouse_pos = pygame.mouse.get_pos()
		Mouse_Key = pygame.mouse.get_pressed()

		#若選擇'princess'
		if inRect(Mouse_pos, P_rect):
			pygame.draw.rect(screen, (255, 255, 255), P_rect)
			screen.blit(text_princess, textP_rect)
			if Mouse_Key[0]:
				return 'princess'

		#若選擇'ghost'
		if inRect(Mouse_pos, G_rect):
			pygame.draw.rect(screen, (255, 255, 255), G_rect)
			screen.blit(text_ghost, textG_rect)
			if Mouse_Key[0]:
				return 'ghost'

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		pygame.display.update()

def gameover():
	endImg = pygame.image.load('bad.jpg').convert()
	global running
	myfont = pygame.font.SysFont("Arial", 24)
	text_again = myfont.render('Try Again', True, (255, 255, 255))
	screen.blit(endImg, (0, 0))
	screen.blit(text_again, (600, 320))
	rect = text_again.get_rect()
	pygame.display.update()
	again = False

	while running and not again:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 0 and inRect(event.pos, rect):
					again = True
	return again

#初始化
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#開始遊戲
gaming = True
while gaming:
	running = True

	#初始化地圖與角色宣告
	Map = []
	BLOCK_LENGTH = 64
	getmap('test_Map.txt')
	background = pygame.Surface((len(Map[0])*BLOCK_LENGTH, len(Map)*BLOCK_LENGTH)).convert()

	#開始畫面
	choose = start()

	#選擇角色
	A = player(choose)
	if choose == 'princess':
		choose = 'ghost'
	else:
		choose = 'princess'
	B = enemy(choose)

	#繪製地圖並隨機生成玩家與敵人位置
	init()

	#開始追逐戰
	while running:
		#若觸碰到敵人
		if A.collider.colliderect(B.collider):
			#遊戲結束畫面
			if gameover():
				init()
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			A.move('left')
		if key[pygame.K_RIGHT]:
			A.move('right')
		if key[pygame.K_UP]:
			A.move('up')
		if key[pygame.K_DOWN]:
			A.move('down')
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		updateframe(A, B)
	
pygame.quit()

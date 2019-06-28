import pygame
import random

class ImageButton():
	def __init__(self, position, image_false, image_true = None):
		self.Rect = image_false.get_rect( topleft = position )
		self.image_false = image_false
		self.image_true = image_true

		if self.image_true == None:
			self.image_true = image_false

	def getImage(self, position): #getImg(滑鼠座標), return 當時狀態的圖像
		if inRect(position, self.Rect):
			return self.image_true
		else:
			return self.image_false
#ImageButton(按鈕左上座標(必要), 預設圖片(必要), 觸發時的圖片)
class SimpleButton():
	def __init__(self, position, size, color_false = None, color_ture = None, text_false = None, text_true = None):
		self.Rect = pygame.Rect(position, size)

		self.image_false = pygame.Surface(size).convert()
		if not color_false == None:
			pygame.draw.rect(self.image_false, color_false, [0, 0, size[0], size[1]])
		if not text_false == None:
			text_rect = text_false.get_rect( center = (size[0]/2, size[1]/2))
			self.image_false.blit(text_false, text_rect)

		self.image_true = pygame.Surface(size).convert()
		if not color_ture == None:
			pygame.draw.rect(self.image_true, color_ture, [0, 0, size[0], size[1]])
		elif not color_false == None:
			pygame.draw.rect(self.image_true, color_false, [0, 0, size[0], size[1]])
		if not text_true == None:
			text_rect = text_true.get_rect( center = (size[0]/2, size[1]/2))
			self.image_true.blit(text_true, text_rect)
		elif not text_false == None:
			text_rect = text_false.get_rect( center = (size[0]/2, size[1]/2))
			self.image_true.blit(text_false, text_rect)

	def getImage(self, position): #getImg(滑鼠座標), return 當時狀態的圖像
		if inRect(position, self.Rect):
			return self.image_true
		else:
			return self.image_false
#SimpleButton(按鈕左上座標(必要), 按鈕大小(必要), 預設顏色, 觸發時的顏色, 預設文字, 觸發時的文字)
class pacman():
	def __init__(self):
		self.direction = 'down'
		self.count = 0
		self.frame_amount = 4

		self.frame_up = [0, 0, 0, 0]
		self.frame_up[0] = pygame.image.load('pac\\pac_up1.png')
		self.frame_up[1] = pygame.image.load('pac\\pac_up2.png')
		self.frame_up[2] = pygame.image.load('pac\\pac_up3.png')
		self.frame_up[3] = pygame.image.load('pac\\pac_up2.png')
		img_transform(self.frame_up)

		self.frame_down = [0, 0, 0, 0]
		self.frame_down[0] = pygame.image.load('pac\\pac_down1.png')
		self.frame_down[1] = pygame.image.load('pac\\pac_down2.png')
		self.frame_down[2] = pygame.image.load('pac\\pac_down3.png')
		self.frame_down[3] = pygame.image.load('pac\\pac_down2.png')
		img_transform(self.frame_down)

		self.frame_left = [0, 0, 0, 0]
		self.frame_left[0] = pygame.image.load('pac\\pac_left1.png')
		self.frame_left[1] = pygame.image.load('pac\\pac_left2.png')
		self.frame_left[2] = pygame.image.load('pac\\pac_left3.png')
		self.frame_left[3] = pygame.image.load('pac\\pac_left2.png')
		img_transform(self.frame_left)

		self.frame_right = [0, 0, 0, 0]
		self.frame_right[0] = pygame.image.load('pac\\pac_right1.png')
		self.frame_right[1] = pygame.image.load('pac\\pac_right2.png')
		self.frame_right[2] = pygame.image.load('pac\\pac_right3.png')
		self.frame_right[3] = pygame.image.load('pac\\pac_right2.png')
		img_transform(self.frame_right)
class player():
	def __init__(self, position_now = [0, 0]):
		self.position_now = position_now
		self.position_next = self.position_now
		self.position_frame = [self.position_now[0]*BLOCK_LENGTH, self.position_now[1]*BLOCK_LENGTH]
		self.frame_class = pacman()
		self.frame_now = animator(self.frame_class)
		self.speed = 15

	def move(self, direction = None):
		if direction == None:
			direction = self.frame_class.direction

		if direction == 'left':
			self.position_next = [self.position_now[0] - 1, self.position_now[1]]
		elif direction == 'right':
			self.position_next = [self.position_now[0] + 1, self.position_now[1]]
		elif direction == 'up':
			self.position_next = [self.position_now[0], self.position_now[1] - 1]
		elif direction == 'down':
			self.position_next = [self.position_now[0], self.position_now[1] + 1]

		if Map_background[self.position_next[1]][self.position_next[0]] == 'X':
			self.position_next = self.position_now

		self.frame_now = animator(self.frame_class, direction)
		if self.frame_class.count == 0:
			self.position_now = self.position_next

		var_now = (self.frame_class.frame_amount - self.frame_class.count) / self.frame_class.frame_amount
		var_next = self.frame_class.count / self.frame_class.frame_amount
		for i in range(0, len(self.position_now)):
			self.position_frame[i] = (var_now*self.position_now[i] + var_next*self.position_next[i]) * BLOCK_LENGTH
def inRect(position, rect):
	if position[0] in range(rect.left, rect.right) and position[1] in range(rect.top, rect.bottom):
		return True
	else:
		return False
def allocate(objects, DistanceRange = None, TargetPosition = None, symbol = None):
	check_list = Map
	distance_map = []
	if DistanceRange != None and TargetPosition != None:
		distance(TargetPosition, distance_map)
	for obj in objects:
		while True:
			obj.position[0] = random.randint(1, len(Map[0])-2)
			obj.position[1] = random.randint(1, len(Map)-2)
			if check_list[obj.position[1]][obj.position[0]] == '.':
				if DistanceRange == None or TargetPosition == None:
					break
				elif distance_map[obj.position[1]][obj.position[0]] >= DistanceRange[0] and distance_map[obj.position[1]][obj.position[0]] <= DistanceRange[1]:
					break
				else:
					check_list[obj.position[1]][obj.position[0]] = 'X'
		check_list[obj.position[1]][obj.position[0]] = symbol
		Map[obj.position[1]][obj.position[0]] = symbol
#allocate(要隨機散佈的物件們(必要), 與目標物距離限制[最短距離, 最長距離], 目標物位置, 地圖表格標記)
def distance(target_pos, check_list, step = 0):
	if check_list == []:
		for i in range(0, len(Map_background)):
			x = []
			for j in range(0, len(Map_background[i])):
				if Map_background[i][j] == 'X':
					x.append('X')
				else:
					x.append(10000)
			check_list.append(x)

	if check_list[target_pos[1]][target_pos[0]] != 'X':
		if check_list[target_pos[1]][target_pos[0]] >= step:
			check_list[target_pos[1]][target_pos[0]] = step
			step += 1

			distance([target_pos[0]-1, target_pos[1]], check_list, step)
			distance([target_pos[0]+1, target_pos[1]], check_list, step)
			distance([target_pos[0], target_pos[1]-1], check_list, step)
			distance([target_pos[0], target_pos[1]+1], check_list, step)
#distance(目標物位置(必要)), 生成最短步數表格, 每隔紀錄此格至目標位置的最短步數, 若目標物位置為牆, return None
def getMap(filename, have_dot = True):
	f = open(filename, 'r')
	L = f.readlines()
	for i in L:
		map_g = []
		map_p = []
		for j in i:
			# 若此格為'X', 視為牆壁, 否則一律視為地面
			if j == 'X':
				map_g.append('X')
				map_p.append(' ')
			elif j != '\n':
				map_g.append('_')

				# 若have_dot是True, Map_prop上會出現'.', 否則全為' '(空白鍵)
				if have_dot:
					map_p.append('.')
				else:
					map_p.append(' ')
		Map_background.append(map_g)
		Map_prop.append(map_p)
# getMap (地圖文字檔名(必要), 要不要加分數點), 將Map_background與Map_prop更新
def drawMap(Map, Surface, char_to_frame = None):
	# 將畫面淨空
	Surface.fill((255, 255, 255, 0))

	# 偵錯
	if len(Map) == 0:
		print("Map size = 0, can't draw map. [drawMap]")

	# 'X'代表牆壁, '_'代表地面, '.'代表分數點, ' '(空白鍵)代表透明
	elif char_to_frame == None:
		for i in range(0, len(Map)):
			for j in range(0, len(Map[i])):
				if Map[i][j] == 'X':
					Surface.blit(wall, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
				elif Map[i][j] == '_':
					Surface.blit(ground, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))

	# 若有字元與圖片的對應dictionary, 則對每格字元畫出相應圖片在相應位置上
	else:
		for i in range(0, len(Map)):
			for j in range(0, len(Map[i])):
				frame = char_to_frame.get(Map[i][j])
				if frame != None:
					Surface.blit(frame, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
# drawMap(地圖表格, 要畫的圖層), 將圖層依據表格的情況更新
def img_transform(frames):
	for i in range(0, len(frames)):
			frames[i] = pygame.transform.scale(frames[i], (BLOCK_LENGTH, BLOCK_LENGTH)).convert_alpha()
# img_transform (圖片list(必要)), 直接將圖片轉換為BLOCK_LENGTH的大小
def animator(frame_class, direction = None):
	if direction == None:
		direction = frame_class.direction
	if direction == frame_class.direction:
		frame_class.count = (frame_class.count + 1) % frame_class.frame_amount
	else:
		frame_class.direction = direction

	if frame_class.direction == 'up':
		return frame_class.frame_up[frame_class.count]
	elif frame_class.direction == 'down':
		return frame_class.frame_down[frame_class.count]
	elif frame_class.direction == 'left':
		return frame_class.frame_left[frame_class.count]
	elif frame_class.direction == 'right':
		return frame_class.frame_right[frame_class.count]
# animator (動畫class(必要), 方向), return 此方向的動畫更新圖片
def chasing_direct(Player, Enemies, index):
	# 獲得各格至目標物的最短步數
	Map_distance = []
	distance(Player.position_now, Map_distance)

	# l: 向左走的最短步數, r: 向右走的最短步數, u: 向上走的最短步數, d: 向下走的最短步數
	l = Map_distance[Enemies[index].position_now[1]][Enemies[index].position_now[0] - 1]
	r = Map_distance[Enemies[index].position_now[1]][Enemies[index].position_now[0] + 1]
	u = Map_distance[Enemies[index].position_now[1] - 1][Enemies[index].position_now[0]]
	d = Map_distance[Enemies[index].position_now[1] + 1][Enemies[index].position_now[0]]

	# 將所有可能方向做成direction_list, 去除會撞牆的方向
	direction_list = [[l, 'left'], [r, 'right'], [u, 'up'], [d, 'down']]
	direction_list = [ elem for elem in direction_list if elem[0] != 'X']

	# 若某方向會與其他追擊者撞到, 將此方向的最短步數 + 10000, 降低這個方向的優先度
	for i in range(0, index):
		for j in range(0, len(direction_list)):
			if direction_list[j][1] == 'left':
				if Enemies[i].position_next == [Enemies[index].position_now[0]-1, Enemies[index].position_now[1]]:
					direction_list[j][0] += 10000
			elif direction_list[j][1] == 'right':
				if Enemies[i].position_next == [Enemies[index].position_now[0]+1, Enemies[index].position_now[1]]:
					direction_list[j][0] += 10000
			elif direction_list[j][1] == 'up':
				if Enemies[i].position_next == [Enemies[index].position_now[0], Enemies[index].position_now[1]-1]:
					direction_list[j][0] += 10000
			elif direction_list[j][1] == 'down':
				if Enemies[i].position_next == [Enemies[index].position_now[0], Enemies[index].position_now[1]+1]:
					direction_list[j][0] += 10000

	# 排序後, direction_list[0] 即為 [最短步數, 方向]
	direction_list.sort()

	# 若有相同最短步數的方向, 隨機挑選方向行走
	direction_list = [ elem for elem in direction_list if elem[0] == direction_list[0][0]]
	x = random.randint(0, len(direction_list)-1)
	return direction_list[x][1]
# chasing_direct (目標物(必要), 敵人列表(必要), 敵人索引值(必要)), return 方向, 指定的敵人以此方向能最快追到目標物

pygame.init()

Map_background = []
Map_prop = []
getMap('map.txt', False)

BLOCK_LENGTH = 50
SCREEN_WIDTH = len(Map_background[0])*BLOCK_LENGTH
SCREEN_HEIGHT = len(Map_background)*BLOCK_LENGTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface(screen.get_size()).convert_alpha()
prop = pygame.Surface(screen.get_size()).convert_alpha()
charactor = pygame.Surface(screen.get_size()).convert_alpha()

wall = pygame.image.load('wall2.png')
ground = pygame.image.load('ground2.png')
#dot = pygame.image.load('dot.png')
img_transform([wall, ground])

drawMap(Map_background, background)
pygame.display.update()

Player = player((1, 1))
Player.speed = 10
charactor.fill((0, 0, 0, 0))
charactor.blit(Player.frame_now, Player.position_frame)

clock = pygame.time.Clock()
update_rate = 30
timer_Player = 0

screen.blit(background, (0, 0))
screen.blit(charactor, (0, 0))
pygame.display.update()

running = True
while running:
	
	clock.tick(update_rate)

	timer_Player += 1
	if Player.frame_class.count == 0:
		KEY = pygame.key.get_pressed()
		if KEY[pygame.K_LEFT]:
			Player.move('left')
		elif KEY[pygame.K_RIGHT]:
			Player.move('right')
		elif KEY[pygame.K_UP]:
			Player.move('up')
		elif KEY[pygame.K_DOWN]:
			Player.move('down')
		else:
			Player.move()

	elif timer_Player >= update_rate / Player.speed:
		timer_Player %= update_rate / Player.speed
		Player.move()
		charactor.fill((0, 0, 0, 0))
		charactor.blit(Player.frame_now, Player.position_frame)

		screen.blit(background, (0, 0))
		screen.blit(charactor, (0, 0))
		pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()

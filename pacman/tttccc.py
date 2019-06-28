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
		if color_false != None:
			pygame.draw.rect(self.image_false, color_false, [0, 0, size[0], size[1]])
		if text_false != None:
			text_rect = text_false.get_rect( center = (size[0]/2, size[1]/2))
			self.image_false.blit(text_false, text_rect)

		self.image_true = pygame.Surface(size).convert()
		if color_ture != None:
			pygame.draw.rect(self.image_true, color_ture, [0, 0, size[0], size[1]])
		elif color_false != None:
			pygame.draw.rect(self.image_true, color_false, [0, 0, size[0], size[1]])
		if text_true != None:
			text_rect = text_true.get_rect( center = (size[0]/2, size[1]/2))
			self.image_true.blit(text_true, text_rect)
		elif text_false != None:
			text_rect = text_false.get_rect( center = (size[0]/2, size[1]/2))
			self.image_true.blit(text_false, text_rect)

	def getImage(self, position): #getImg(滑鼠座標), return 當時狀態的圖像
		if inRect(position, self.Rect):
			return self.image_true
		else:
			return self.image_false
#SimpleButton(按鈕左上座標(必要), 按鈕大小(必要), 預設顏色, 觸發時的顏色, 預設文字, 觸發時的文字)
class princess():
	def __init__(self):
		# count: 動畫計數器, frame_amount: 動畫禎數
		self.count = 0
		self.frame_amount = 4

		# frame_up: 角色方向向上的圖組
		self.frame_up = [None] * self.frame_amount
		self.frame_up[0] = pygame.image.load('P\\P_up0.png')
		self.frame_up[1] = pygame.image.load('P\\P_up1.png')
		self.frame_up[2] = pygame.image.load('P\\P_up0.png')
		self.frame_up[3] = pygame.image.load('P\\P_up2.png')
		img_transform(self.frame_up)

		# frame_down: 角色方向向下的圖組
		self.frame_down = [None] * self.frame_amount
		self.frame_down[0] = pygame.image.load('P\\P_down0.png')
		self.frame_down[1] = pygame.image.load('P\\P_down1.png')
		self.frame_down[2] = pygame.image.load('P\\P_down0.png')
		self.frame_down[3] = pygame.image.load('P\\P_down2.png')
		img_transform(self.frame_down)

		# frame_left: 角色方向向左的圖組
		self.frame_left = [None] * self.frame_amount
		self.frame_left[0] = pygame.image.load('P\\P_left0.png')
		self.frame_left[1] = pygame.image.load('P\\P_left1.png')
		self.frame_left[2] = pygame.image.load('P\\P_left0.png')
		self.frame_left[3] = pygame.image.load('P\\P_left2.png')
		img_transform(self.frame_left)

		# frame_right: 角色方向向右的圖組
		self.frame_right = [None] * self.frame_amount
		self.frame_right[0] = pygame.image.load('P\\P_right0.png')
		self.frame_right[1] = pygame.image.load('P\\P_right1.png')
		self.frame_right[2] = pygame.image.load('P\\P_right0.png')
		self.frame_right[3] = pygame.image.load('P\\P_right2.png')
		img_transform(self.frame_right)

class ghost():
	def __init__(self):
		# count: 動畫計數器, frame_amount: 動畫禎數
		self.count = 0
		self.frame_amount = 4

		# frame_up: 角色方向向上的圖組
		self.frame_up = [None] * self.frame_amount
		self.frame_up[0] = pygame.image.load('ghost\\ghost_up0.png')
		self.frame_up[1] = pygame.image.load('ghost\\ghost_up1.png')
		self.frame_up[2] = pygame.image.load('ghost\\ghost_up2.png')
		self.frame_up[3] = pygame.image.load('ghost\\ghost_up3.png')
		img_transform(self.frame_up)

		# frame_down: 角色方向向下的圖組
		self.frame_down = [None] * self.frame_amount
		self.frame_down[0] = pygame.image.load('ghost\\ghost_down0.png')
		self.frame_down[1] = pygame.image.load('ghost\\ghost_down1.png')
		self.frame_down[2] = pygame.image.load('ghost\\ghost_down2.png')
		self.frame_down[3] = pygame.image.load('ghost\\ghost_down3.png')
		img_transform(self.frame_down)

		# frame_left: 角色方向向左的圖組
		self.frame_left = [None] * self.frame_amount
		self.frame_left[0] = pygame.image.load('ghost\\ghost_left0.png')
		self.frame_left[1] = pygame.image.load('ghost\\ghost_left1.png')
		self.frame_left[2] = pygame.image.load('ghost\\ghost_left2.png')
		self.frame_left[3] = pygame.image.load('ghost\\ghost_left3.png')
		img_transform(self.frame_left)

		# frame_right: 角色方向向右的圖組
		self.frame_right = [None] * self.frame_amount
		self.frame_right[0] = pygame.image.load('ghost\\ghost_right0.png')
		self.frame_right[1] = pygame.image.load('ghost\\ghost_right1.png')
		self.frame_right[2] = pygame.image.load('ghost\\ghost_right2.png')
		self.frame_right[3] = pygame.image.load('ghost\\ghost_right3.png')
		img_transform(self.frame_right)
		
class pacman():
	def __init__(self):
		# count: 動畫計數器, frame_amount: 動畫禎數
		self.count = 0
		self.frame_amount = 4

		# frame_up: 角色方向向上的圖組
		self.frame_up = [None] * self.frame_amount
		self.frame_up[0] = pygame.image.load('pac\\pac_up0.png')
		self.frame_up[1] = pygame.image.load('pac\\pac_up1.png')
		self.frame_up[2] = pygame.image.load('pac\\pac_up2.png')
		self.frame_up[3] = pygame.image.load('pac\\pac_up3.png')
		img_transform(self.frame_up)

		# frame_down: 角色方向向下的圖組
		self.frame_down = [None] * self.frame_amount
		self.frame_down[0] = pygame.image.load('pac\\pac_down0.png')
		self.frame_down[1] = pygame.image.load('pac\\pac_down1.png')
		self.frame_down[2] = pygame.image.load('pac\\pac_down2.png')
		self.frame_down[3] = pygame.image.load('pac\\pac_down3.png')
		img_transform(self.frame_down)

		# frame_left: 角色方向向左的圖組
		self.frame_left = [None] * self.frame_amount
		self.frame_left[0] = pygame.image.load('pac\\pac_left0.png')
		self.frame_left[1] = pygame.image.load('pac\\pac_left1.png')
		self.frame_left[2] = pygame.image.load('pac\\pac_left2.png')
		self.frame_left[3] = pygame.image.load('pac\\pac_left3.png')
		img_transform(self.frame_left)

		# frame_right: 角色方向向右的圖組
		self.frame_right = [None] * self.frame_amount
		self.frame_right[0] = pygame.image.load('pac\\pac_right0.png')
		self.frame_right[1] = pygame.image.load('pac\\pac_right1.png')
		self.frame_right[2] = pygame.image.load('pac\\pac_right2.png')
		self.frame_right[3] = pygame.image.load('pac\\pac_right3.png')
		img_transform(self.frame_right)

class player():
	def __init__(self):
		# position_now: 起步格位置, position_next: 目標格位置, 以此計算動畫更新後position_frame的位置(像素位置)
		self.position_now = [0, 0]
		self.position_next = self.position_now
		self.position_frame = [self.position_now[0]*BLOCK_LENGTH, self.position_now[1]*BLOCK_LENGTH]

		# frame_class: 動畫圖組, frame_now: 更新後角色圖像, direction: 角色行進方向, speed: 角色移動速率
		self.frame_class = pacman()
		self.frame_now = self.frame_class.frame_down[0]
		self.direction = 'down'
		self.speed = 20

	def move(self, direction = None):
		if direction != None:
			self.direction = direction

		if self.direction == 'left':
			self.position_next = [self.position_now[0] - 1, self.position_now[1]]
		elif self.direction == 'right':
			self.position_next = [self.position_now[0] + 1, self.position_now[1]]
		elif self.direction == 'up':
			self.position_next = [self.position_now[0], self.position_now[1] - 1]
		elif self.direction == 'down':
			self.position_next = [self.position_now[0], self.position_now[1] + 1]

		if Map_background[self.position_next[1]][self.position_next[0]] == 'X':
			self.position_next = self.position_now

		animator(self)

class enemy():
	def __init__(self):
		# position_now: 起步格位置, position_next: 目標格位置, 以此計算動畫更新後position_frame的位置(像素位置)
		self.position_now = [0, 0]
		self.position_next = self.position_now
		self.position_frame = [self.position_now[0]*BLOCK_LENGTH, self.position_now[1]*BLOCK_LENGTH]

		# frame_class: 動畫圖組, frame_now: 更新後角色圖像, direction: 角色行進方向, speed: 角色移動速率
		self.frame_class = ghost()
		self.frame_now = self.frame_class.frame_down[0]
		self.direction = 'down'
		self.speed = 15

	def move(self, direction = None):
		if direction != None:
			self.direction = direction

		if self.direction == 'left':
			self.position_next = [self.position_now[0] - 1, self.position_now[1]]
		elif self.direction == 'right':
			self.position_next = [self.position_now[0] + 1, self.position_now[1]]
		elif self.direction == 'up':
			self.position_next = [self.position_now[0], self.position_now[1] - 1]
		elif self.direction == 'down':
			self.position_next = [self.position_now[0], self.position_now[1] + 1]

		if Map_background[self.position_next[1]][self.position_next[0]] == 'X':
			self.position_next = self.position_now

		animator(self)

def outputTest(Player, Enemies, game_time, frame_number, game_point = None):
	if test:
		if frame_number == 0:
			print('[init]')
		else:
			print('[main] frame update:', frame_number, '/ game time:', game_time, 's / game point:', game_point)

		s = ' '
		if len(Map_background[0]) > len('Map_background'):
			s *= len(Map_background[0]) - len('Map_background') + 2
		else:
			s *= 2
		print('Map_background', s, sep = '', end = '')

		s = ' '
		if len(Map_prop[0]) > len('Map_prop'):
			s *= len(Map_prop[0]) - len('Map_prop') + 2
		else:
			s *= 2
		print('Map_prop', s, sep = '', end = '')

		s = ' '
		if len(Map_charactor[0]) > len('Map_charactor'):
			s *= len(Map_charactor[0]) - len('Map_charactor') + 2
		else:
			s *= 2
		print('Map_charactor', s, sep = '')

		s1 = ' '
		if len(Map_background[0]) > len('Map_background'):
			s1 *= 2
		else:
			s1 *= len('Map_background') - len(Map_background[0]) + 2
		s2 = ' '
		if len(Map_prop[0]) > len('Map_prop'):
			s2 *= 2
		else:
			s2 *= len('Map_prop') - len(Map_prop[0]) + 2
		s3 = ' '
		if len(Map_charactor[0]) > len('Map_charactor'):
			s3 *= 2
		else:
			s3 *= len('Map_charactor') - len(Map_charactor[0]) + 2
		for i in range(0, len(Map_background)):
			for j in Map_background[i]:
				print(j, sep = '', end = '')
			print(s1, sep = '', end = '')
			for j in Map_prop[i]:
				print(j, sep = '', end = '')
			print(s2, sep = '', end = '')
			for j in Map_charactor[i]:
				print(j, sep = '', end = '')
			print(s3, sep = '', end = '')

			if i == 0:
				print('Player :', Player.position_now, '->', Player.position_next, ',', Player.direction, ',', Player.frame_class.count)
			elif i <= len(Enemies):
				print('Enemy', i-1, ':', Enemies[i-1].position_now, '->', Enemies[i-1].position_next, ',', Enemies[i-1].direction, ',', Enemies[i-1].frame_class.count)
			else:
				print('')
		print('==================================================================')
# outputTest(主角物件(必要), 敵人物件list(必要), 遊戲總時間(必要), 遊戲總禎數(必要), 已獲得分數點量), 將遊戲每次更新的各項數據輸出
def inRect(position, rect):
	if position[0] in range(rect.left, rect.right) and position[1] in range(rect.top, rect.bottom):
		return True
	else:
		return False
# inRect (座標(必要), 長方形(必要)), return 座標是否在長方形內
def getMap(filename, have_dot = True):
	f = open(filename, 'r')
	L = f.readlines()
	point = 0
	for i in L:
		map_g = []
		map_p = []
		map_c = []
		for j in i:
			# 若此格為'X', 視為牆壁, 否則一律視為地面
			if j == 'X':
				map_g.append('X')
				map_p.append(' ')
				map_c.append('X')
			elif j != '\n':
				map_g.append('_')

				# 若have_dot是True, Map_prop上會出現'.', 否則全為' '(空白鍵)
				if have_dot:
					map_p.append('.')
					point += 1
				else:
					map_p.append(' ')

				map_c.append(' ')
		Map_background.append(map_g)
		Map_prop.append(map_p)
		Map_charactor.append(map_c)

	if have_dot:
		return point
	else:
		return None
# getMap (地圖文字檔名(必要), 要不要加分數點), 將Map_background、 Map_prop、 Map_characor更新, 若有加分數點, return 分數點總量
def drawMap(Map, Surface, char_to_frame = None):
	# 將畫面淨空
	Surface.fill((0, 0, 0, 0))

	# 偵錯
	if len(Map) == 0:
		print("[drawMap] Map size = 0, can't draw map.")

	# 'X'代表牆壁, '_'代表地面, '.'代表分數點, ' '(空白鍵)代表透明
	elif char_to_frame == None:
		for i in range(0, len(Map)):
			for j in range(0, len(Map[i])):
				if Map[i][j] == 'X':
					Surface.blit(wall, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
				elif Map[i][j] == '_':
					Surface.blit(ground, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
				elif Map[i][j] == '.':
					Surface.blit(dot, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
	# 若有字元與圖片的對應dictionary, 則對每格字元畫出相應圖片在相應位置上
	else:
		for i in range(0, len(Map)):
			for j in range(0, len(Map[i])):
				frame = char_to_frame.get(Map[i][j])
				if frame != None:
					Surface.blit(frame, (j*BLOCK_LENGTH, i*BLOCK_LENGTH))
# drawMap(地圖表格(必要), 要畫的圖層(必要)), 將圖層依據表格的情況更新
def allocate(objects, DistanceRange = None, TargetPosition = None, Map = None, symbol = None):
	# 偵錯
	if DistanceRange == None and TargetPosition != None:
		print("[allocate] You should add DistanceRange as an argument.")
		return
	if DistanceRange != None and TargetPosition == None:
		print("[allocate] You should add TargetPosition as an argument.")
		return
	if Map == None and symbol != None:
		print("[allocate] You should add Map as an argument.")
		return
	if Map != None and symbol == None:
		print("[allocate] You should add symbol as an argument.")
		return
	if DistanceRange != None and DistanceRange[0] > DistanceRange[1]:
		print("[allocate] DistanceRange[1] should bigger than or equal to DistanceRange[0].")

	# check_list: 紀錄哪些位置已經確定不能放物件, 避免重複選取
	check_list = []
	for i in Map_background:
		c = []
		for j in i:
			if j == 'X':
				c.append('X')
			else:
				c.append(' ')
		check_list.append(c)

	# Map_distance: 紀錄與目標物相距的最短步數的表格
	Map_distance = []
	if DistanceRange != None:
		distance(TargetPosition, Map_distance)

	# remain_amount: 紀錄目前剩下多少位置尚未確認不能放物件
	remain_amount = 0
	for i in check_list:
		for j in i:
			if j != 'X':
				remain_amount += 1

	# n: 紀錄要散佈的物件的數量
	n = objects
	if type(objects) != int:
		n = len(objects)

	for i in range(0, n):
		if remain_amount <= 0:
			break

		x, y = None, None
		while True:
			if remain_amount <= 0:
				print("Can't find place for object. [allocate]")
				break

			# 隨機選取位置
			x = random.randint(1, len(Map_background[0])-2)
			y = random.randint(1, len(Map_background)-2)

			# 確認這格是否可以放物件
			if check_list[y][x] != 'X':
				check_list[y][x] = 'X' # 記錄此格已被計算過
				remain_amount -= 1
				if Map_distance == [] or Map_distance[y][x] in range(DistanceRange[0], DistanceRange[1]+1):
					break

		# 將Map上標記散佈位置
		if symbol != None:
			Map[y][x] = symbol

		# 更新物件位置
		if type(objects) != int:
			objects[i].position_now[0] = x
			objects[i].position_now[1] = y
			objects[i].position_next = objects[i].position_now
			objects[i].position_frame = [objects[i].position_now[0]*BLOCK_LENGTH, objects[i].position_now[1]*BLOCK_LENGTH]
# allocate (要隨機散佈的物件list或是物件數量(必要), 與目標物距離限制[最短距離, 最長距離], 目標物位置, 地圖表格標記), 會將物件們的位置隨機散佈
def distance(target_pos, Map_distance, step = 0):
	if Map_distance == []:
		for i in range(0, len(Map_background)):
			x = []
			for j in range(0, len(Map_background[i])):
				if Map_background[i][j] == 'X':
					x.append('X')
				else:
					x.append(10000)
			Map_distance.append(x)

	if Map_distance[target_pos[1]][target_pos[0]] != 'X':
		if Map_distance[target_pos[1]][target_pos[0]] >= step:
			Map_distance[target_pos[1]][target_pos[0]] = step
			step += 1

			distance([target_pos[0]-1, target_pos[1]], Map_distance, step)
			distance([target_pos[0]+1, target_pos[1]], Map_distance, step)
			distance([target_pos[0], target_pos[1]-1], Map_distance, step)
			distance([target_pos[0], target_pos[1]+1], Map_distance, step)
# distance (目標位置(必要), 最短步數表格(必要)), 最短步數表格的每格紀錄此格到目標位置的最短步數
def img_transform(frames):
	for i in range(0, len(frames)):
		frames[i] = pygame.transform.scale(frames[i], (BLOCK_LENGTH, BLOCK_LENGTH)).convert_alpha()
# img_transform (圖片list(必要)), 直接將圖片轉換為BLOCK_LENGTH的大小
def animator(charactor):
	# 更新方向與動畫計數器
	charactor.frame_class.count += 1
	if charactor.frame_class.count >= charactor.frame_class.frame_amount:
		# 更新Map_charactor
		Map_charactor[charactor.position_next[1]][charactor.position_next[0]] = Map_charactor[charactor.position_now[1]][charactor.position_now[0]]
		Map_charactor[charactor.position_now[1]][charactor.position_now[0]] = ' '
		# 更新角色位置與計數器
		charactor.position_now = charactor.position_next
		charactor.frame_class.count -= charactor.frame_class.frame_amount

	# 依據方向與動畫計數器更新frame_now
	if charactor.direction == 'up':
		charactor.frame_now = charactor.frame_class.frame_up[charactor.frame_class.count]
	elif charactor.direction == 'down':
		charactor.frame_now = charactor.frame_class.frame_down[charactor.frame_class.count]
	elif charactor.direction == 'left':
		charactor.frame_now = charactor.frame_class.frame_left[charactor.frame_class.count]
	elif charactor.direction == 'right':
		charactor.frame_now = charactor.frame_class.frame_right[charactor.frame_class.count]

	# 依據position_now與positon_next更新position_frame
	var_now = (charactor.frame_class.frame_amount - charactor.frame_class.count) / charactor.frame_class.frame_amount
	var_next = charactor.frame_class.count / charactor.frame_class.frame_amount
	charactor.position_frame[0] = (var_now*charactor.position_now[0] + var_next*charactor.position_next[0]) * BLOCK_LENGTH
	charactor.position_frame[1] = (var_now*charactor.position_now[1] + var_next*charactor.position_next[1]) * BLOCK_LENGTH
# animator (角色物件(必要)), 更新charactor的frame_now, position_frame
def chasing_direct(Player, Enemies, index):
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
#def chasing_random(Enemies, index):
def start():
	# 載入開始畫面圖片
	startImg = pygame.image.load('start.jpg')
	startImgRect = startImg.get_rect( center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

	# 設置遊戲開始按鍵
	BtnSize = [200, 50] # 按鈕大小
	BtnPosition = [SCREEN_WIDTH/2 - BtnSize[0]/2, SCREEN_HEIGHT/2 - BtnSize[1]/2 + 75] # 按鈕位置
	BtnColor_F, BtnColor_T = (255, 255, 255), (100, 100, 100) # 按鈕觸發與未觸發的顏色
	BtnFont = pygame.font.SysFont("Bold", 24) # 按鈕字體設定

	# 按鈕文字觸發與未觸發的顏色
	BtnText_F = BtnFont.render('START', True, (0, 0, 0))
	BtnText_T = BtnFont.render('START', True, (255, 255, 255))

	startBtn = SimpleButton(BtnPosition, BtnSize, BtnColor_F, BtnColor_T, BtnText_F, BtnText_T)

	# 當未開始遊戲時持續更新開始畫面
	global running
	begin = False

	while running and not begin:
		# 根據滑鼠位置更新按鈕圖片
		screen.blit(startImg, startImgRect)
		Mouse_pos = pygame.mouse.get_pos()
		BtnImg = startBtn.getImage(Mouse_pos)
		screen.blit(BtnImg, BtnPosition)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			# 若按下開始按鈕, 就開始遊戲
			if event.type == pygame.MOUSEBUTTONDOWN:
				if inRect(event.pos, startBtn.Rect) and event.button == 1:
					begin = True
		pygame.display.update()
# 開始畫面
def init(Player, Enemies):
	# 隨機生成玩家位置
	allocate([Player], Map = Map_charactor, symbol = 'O')

	# 隨機生成敵人位置, 敵人至少離玩家8步遠
	DistanceRange = [8, 10000]
	allocate(Enemies, DistanceRange, Player.position_now, Map_charactor, 'G')

	# 更新背景與道具圖層
	drawMap(Map_background, background)
	Map_prop[Player.position_now[1]][Player.position_now[0]] = ' ' # 去掉主角原本站的那格
	drawMap(Map_prop, prop)

	#更新角色圖層
	charactor.fill((0, 0, 0, 0))
	charactor.blit(Player.frame_now, Player.position_frame)
	for Enemy in Enemies:
		charactor.blit(Enemy.frame_now, Enemy.position_frame)

	# 將三圖層更新在畫面上
	screen.blit(background, (0, 0))
	screen.blit(prop, (0, 0))
	screen.blit(charactor, (0, 0))
	pygame.display.update()

	outputTest(Player, Enemies, 0, 0, 0)
# 初始化地圖
def main():
	# 初始化
	Player = player()

	enemy_amount = 3 # 敵人數量 = 3
	Enemies = []
	for i in range(0, enemy_amount):
		x = enemy()
		Enemies.append(x)
	init(Player, Enemies)

	# 計算更新時間
	clock = pygame.time.Clock()
	update_rate = 30
	
	# 每個角色動畫更新的計時器
	timer_Player = 0
	timer_Enemies = [0] * enemy_amount

	# 遊戲計時器, 遊戲總禎數, 遊戲分數, 場上剩餘點數
	game_time = 0.0
	frame_number = 0
	game_point = 0
	global total_point
	
	global running
	while running:
		clock.tick(update_rate)
		game_time += 1 / update_rate
		frame_number += 1

		# 敵人動畫更新
		# 獲得各格至目標物的最短步數
		for i in range(0, len(Enemies)):
			timer_Enemies[i] += 1
			if timer_Enemies[i] >= update_rate / Enemies[i].speed:
				# 當敵人動畫做完一個循環(走過一格), 即可改變行進方向
				if Enemies[i].frame_class.count == 0:
					direction = chasing_direct(Player, Enemies, i) # 估算要往哪邊走能最快追到敵人
					Enemies[i].move(direction)
				else:
					Enemies[i].move()
				timer_Enemies[i] %= update_rate / Enemies[i].speed
		
		# 主角動畫更新
		timer_Player += 1
		if timer_Player >= update_rate / Player.speed:
			# 當主角動畫做完一個循環(走過一格), 即可改變行進方向
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

				# 若踩到的格子有分數點,  將分數點去掉, game_point += 1, 更新道具圖層畫面
				if Map_prop[Player.position_now[1]][Player.position_now[0]] != ' ':
					Map_prop[Player.position_now[1]][Player.position_now[0]] = ' '
					game_point += 1
					drawMap(Map_prop, prop)

			# 否則, 單純更新frame_now與position_frame
			else:
				Player.move()
			timer_Player %= update_rate / Player.speed
		
		# 將角色圖像更新
		charactor.fill((0, 0, 0, 0))
		charactor.blit(Player.frame_now, Player.position_frame)
		for Enemy in Enemies:
			charactor.blit(Enemy.frame_now, Enemy.position_frame)

		# 將三圖層更新在畫面上
		screen.blit(background, (0, 0))
		screen.blit(prop, (0, 0))
		screen.blit(charactor, (0, 0))
		pygame.display.update()

		outputTest(Player, Enemies, game_time, frame_number, game_point)

		# 當分數點被全部吃完, 遊戲結束
		if game_point >= total_point:
			running = False

		# 當主角與任何一個敵人相撞, 遊戲結束
		for Enemy in Enemies:
			if Enemy.position_now == Player.position_next and Enemy.position_next == Player.position_now:
				running = False
				break

		# 當按下右上角X, 遊戲結束
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
# 遊戲主程式, return 遊戲結果, 遊戲獲勝為'win', 遊戲失敗為'lose'
'''
def win():
# 獲勝畫面, return 玩家的選擇, 再次嘗試遊戲為'retry', 結束遊戲為'quit'
def lose():
# 失敗畫面, return 玩家的選擇, 再次嘗試遊戲為'retry', 結束遊戲為'quit'
'''
pygame.init()

# 當test為True時, 會於每禎更新時輸出各角色內部數據與地圖表格
test = True

# 讀入背景地圖表格與道具地圖表格
Map_background = []
Map_prop = []
Map_charactor = []
total_point = getMap('map.txt')
total_point -= 1 # 去掉主角原本站的那格

# 設定每格長寬與畫面大小
BLOCK_LENGTH = 50
SCREEN_WIDTH = len(Map_background[0])*BLOCK_LENGTH
SCREEN_HEIGHT = len(Map_background)*BLOCK_LENGTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 建立背景、道具、角色的圖層
background = pygame.Surface(screen.get_size()).convert_alpha()
prop = pygame.Surface(screen.get_size()).convert_alpha()
charactor = pygame.Surface(screen.get_size()).convert_alpha()

# 載入地面、牆壁、分數點的圖片並縮放
wall = pygame.image.load('wall2.png')
wall = pygame.transform.scale(wall, (BLOCK_LENGTH, BLOCK_LENGTH)).convert_alpha()
ground = pygame.image.load('ground2.png')
ground = pygame.transform.scale(ground, (BLOCK_LENGTH, BLOCK_LENGTH)).convert_alpha()
dot = pygame.image.load('dot.png')
dot = pygame.transform.scale(dot, (BLOCK_LENGTH, BLOCK_LENGTH)).convert_alpha()

# 遊戲開始畫面
running = True
start()

# 主程式開始
while running:
	#game_state = main()
	main()
	if running == False:
		break
	'''
	elif game_state == 'win':
		game_state = win()
	elif game_state == 'lose':
		game_state = lose()

	if game_state == 'retry':
		continue
	elif game_state == 'quit':
		break
	'''
# 結束遊戲
pygame.quit()
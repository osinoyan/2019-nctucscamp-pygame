import pygame
import random
pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

x = 400
y = 300
r = 45
vx = 0.0
vy = 0.0
ax = 0.0
ay = 0.88

state = 'START' 
score = 0

canvas = pygame.Surface(SCREEN_SIZE)
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial', 500)

picture = pygame.image.load('ball.png')                # 載入[ball.png]圖片檔 
picture = pygame.transform.scale(picture, (r*2, r*2))  # 把圖片大小調成相當於球的[直徑]*[直徑]

def reset():
	global x, y, vx, vy, state
	state = 'START'
	# 球的位置、速度重置 --------------------
	x = 400
	y = 300
	vx = 0.0
	vy = 0.0
	# -------------------------------------

def check_game_over():
	global x, y, state
	y_max = SCREEN_SIZE[1] + r
	if y > y_max:
		reset()

def ball_animation():
	global x, y, vx, vy
	x_max = SCREEN_SIZE[0] - r  # 球剛好碰到右壁時，此時的球心 x 座標
	x_min = r                   # 球剛好碰到左壁時，此時的球心 x 座標
	
	# 牛頓運動定律 --------------------------
	
	x = int(x + vx)
	y = int(y + vy)
	vx = vx + ax
	vy = vy + ay

	# 彈性碰撞 ------------------------------

	if x > x_max: # 碰到右邊的牆
		ex = x - x_max
		t = ex / vx
		vx = -vx
		x = int(x_max - vx*(1-t))
		if abs(vx) < 1:
			vx = 0
			x = x_max
	
	if x < x_min: # 碰到左邊的牆
		ex = x - x_min
		t = ex / vx
		vx = -vx
		x = int(x_min - vx*(1-t))
		if abs(vx) < 1:
			vx = 0
			x = x_min

def distance_square(pos1, pos2):
	x1 = pos1[0]
	y1 = pos1[1]
	x2 = pos2[0]
	y2 = pos2[1]
	return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

def ball_bounce():
	global vx, vy
	vx = random.uniform(-5.0, 5.0)      # 球的 x 速度是介在 -5.0 ~ 5.0 之間的隨機數字
	vy = random.uniform(-21.0, -20.0)   # 球的 y 速度是介在 -21.0 ~ -20.0 之間的隨機數字

def check_hit_ball(mouse_pos):
	global score
	ball_pos = [x, y]
	if r * r > distance_square(mouse_pos, ball_pos):
		print('HIT!')
		ball_bounce()
		score = score + 1
	else:
		print('NO!')

running = True
while running:
	# 遊戲事件偵測 ----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					check_hit_ball(event.pos)  
					if state == 'START':
						state = 'PLAYING'      
						score = 0
	
	# 動畫控制 --------------------------------------
	clock.tick(60)
	if state == 'START': 
		canvas.fill(pygame.Color('BLACK'))
	elif state == 'PLAYING':
		ball_animation()
		check_game_over()
		canvas.fill(pygame.Color('WHITE'))
	
	# 更新畫面 --------------------------------------
	score_text = myfont.render(str(score), True, pygame.Color('PINK'))
	canvas.blit(score_text, (10, 10))
	# pygame.draw.circle(canvas, pygame.Color('LIGHTBLUE'), (x, y), r)
	canvas.blit(picture, (x-r, y-r)) # 把球的圖片根據球的位置座標貼在畫布上面
	screen.blit(canvas, (0, 0))
	pygame.display.update()
	# ----------------------------------------------

pygame.quit()
import pygame
import random
import math # 引入數學模組
pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

x = 400
y = 300
r = 45
vx = 0.0
vy = 0.0
ax = 0.0
# ay = 0.88
ay = 0.3 # 為了測試把重力加速度先調小

canvus = pygame.Surface(SCREEN_SIZE)
clock = pygame.time.Clock()

def ball_animation():
	global x, y, vx, vy, ax, ay
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
		if math.fabs(vx) < 1:
			vx = 0
			x = x_max
	
	if x < x_min: # 碰到左邊的牆
		ex = x - x_min
		t = ex / vx
		vx = -vx
		x = int(x_min - vx*(1-t))
		if math.fabs(vx) < 1:
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
	# vy = random.uniform(-21.0, -20.0) # 球的 y 速度是介在 -21.0 ~ -20.0 之間的隨機數字
	vy = -10.0                           # 球的 y 速度是 -10.0 (測試用)

def check_hit_ball(mouse_pos):
	ball_pos = [x, y]
	if r * r > distance_square(mouse_pos, ball_pos):
		print('HIT!')
		ball_bounce()
	else:
		print('NO!')

running = True
while running:
	# 遊戲事件偵測 ----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# 當滑鼠事件發生
		if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1: # 按下左鍵時
					check_hit_ball(event.pos) # 確認滑鼠有沒有按到球
	
	# 動畫控制 --------------------------------------
	clock.tick(60)
	ball_animation()
	
	# 更新畫面 --------------------------------------
	canvus.fill(pygame.Color('WHITE'))
	pygame.draw.circle(canvus, pygame.Color('LIGHTBLUE'), (x, y), r)
	screen.blit(canvus, (0, 0))
	pygame.display.update()
	# ----------------------------------------------

pygame.quit()
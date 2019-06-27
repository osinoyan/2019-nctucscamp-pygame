import pygame
import pygame.gfxdraw
import sys
import math
import random

pygame.init()

# 設定視窗的長寬大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 重置所有狀態
def reset():
	global ball_pos
	global ball_radius
	global ball_acc
	global ball_velocity
	global score
	score = 0
	# ball
	ball_pos = [400, 300]
	ball_radius = 45
	# FACTORS
	ball_acc = [0, 0.88]
	ball_velocity = [0.0, 0.0]

# 取得兩個點的距離平方
def distance_square(pos1, pos2):
	x1 = pos1[0]
	y1 = pos1[1]
	x2 = pos2[0]
	y2 = pos2[1]
	return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

# 確認滑鼠有沒有按到球
def check_hit_ball(mouse_pos):
	if ball_radius * ball_radius > distance_square(mouse_pos, ball_pos):
		print(mouse_pos)
		print(ball_pos)
		print('Hit!')
		ball_bounce(mouse_pos)
	else:
		print('NO!')

# 球被滑鼠按到後要做的事
def ball_bounce(mouse_pos):
	global score
	score = score + 1
	vx = ball_velocity[0]
	vy = ball_velocity[1]
	vx = random.uniform(-5.5, 5.5)
	vy = random.uniform(-20.5, -21.5)
	ball_velocity[0] = vx
	ball_velocity[1] = vy

# -------------------------------------------------------
reset()
canvus = pygame.Surface(screen.get_size())
picture = pygame.image.load('ball.png')
picture = pygame.transform.scale(picture, (ball_radius*2+3, ball_radius*2+3))
myfont = pygame.font.SysFont('Arial', 500)

# 是否遊戲結束
running = True
clock = pygame.time.Clock()
while running:
	# ----------遊戲事件偵測----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				reset()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				check_hit_ball(event.pos)
	# ANIMATION ------------------------------------------------
	clock.tick(60)
	x = ball_pos[0]
	y = ball_pos[1]

	# gravity
	ball_velocity[0] = ball_velocity[0] + ball_acc[0]
	ball_velocity[1] = ball_velocity[1] + ball_acc[1]
	x = x + ball_velocity[0]
	y = y + ball_velocity[1]

	y_max = ( 500 - (ball_radius + 1) )
	x_max = ( SCREEN_WIDTH - (ball_radius + 1) )
	x_min = (ball_radius + 1)
	vx = ball_velocity[0]
	vy = ball_velocity[1]
	ax = ball_acc[0]
	ay = ball_acc[1]
	

	# if y_ex > 0:
	# 	v = vy
	# 	ex = y - y_max
	# 	t = ex / v
	# 	v = -0.8*v
	# 	y = y_max - v*(1-t)
	# 	if math.fabs(v) < 2:
	# 		ball_velocity[1] = 0
	# 		y = y_max
	# 	else:
	# 		ball_velocity[1] = v

	# 右邊的牆
	if x > x_max:
		v = vx
		ex = x - x_max
		t = ex / v
		v = -v
		print('t='+str(t))
		print('vx='+str(vx))
		x = x_max - v*(1-t)
		if math.fabs(v) < 1:
			ball_velocity[0] = 0
			x = x_max
		else:
			ball_velocity[0] = v
	
	# 左邊的牆
	if x < x_min:
		v = vx
		ex = x - x_min
		t = ex / v
		v = -v
		x = x_min - v*(1-t)
		if math.fabs(v) < 1:
			ball_velocity[0] = 0
			x = x_min
		else:
			ball_velocity[0] = v




	ball_pos = [int(x), int(y)]
	# ----------更新畫面--------------------------------------
	canvus.fill(pygame.Color('WHITE'))

	score_text = myfont.render(str(score), True, pygame.Color('LIGHTBLUE'))

	canvus.blit(score_text, (10, 10))

	# pygame.draw.line(canvus, pygame.Color('LIGHTBLUE'), [0, 500], [800, 500], 2)
	# pygame.gfxdraw.filled_circle(canvus, ball_pos[0], ball_pos[1], ball_radius, pygame.Color('LIGHTBLUE'))
	# pygame.gfxdraw.aacircle(canvus, ball_pos[0], ball_pos[1], ball_radius, pygame.Color('LIGHTBLUE'))
	canvus.blit(picture, (ball_pos[0]-ball_radius, ball_pos[1]-ball_radius))
	screen.blit(canvus, (0, 0))
	pygame.display.update()
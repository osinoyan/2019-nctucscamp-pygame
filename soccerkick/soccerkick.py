import pygame
#import pygame.gfxdraw
#import sys
import math
import random

pygame.init()

# 設定視窗的長寬大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 重置所有狀態
def reset():
	global ball_pos, ball_radius, ball_acc, ball_velocity
	global state, score
	state = 'START'
	# ball
	ball_pos = [400, 300]
	ball_radius = 45
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

def ball_animation():
	global ball_pos, ball_velocity, ball_acc
	x = ball_pos[0]
	y = ball_pos[1]
	vx = ball_velocity[0]
	vy = ball_velocity[1]
	ax = ball_acc[0]
	ay = ball_acc[1]

	r = ball_radius
	x_max = ( SCREEN_WIDTH - (r + 1) )
	x_min = (r + 1)

	# 牛頓運動定律
	x = x + vx
	y = y + vy
	vx = vx + ax
	vy = vy + ay

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
		ex = x - x_max
		t = ex / vx
		vx = -vx
		x = x_max - vx*(1-t)
		if math.fabs(vx) < 1:
			ball_velocity[0] = 0
			x = x_max
		else:
			ball_velocity[0] = vx
	
	# 左邊的牆
	if x < x_min:
		ex = x - x_min
		t = ex / vx
		vx = -vx
		x = x_min - vx*(1-t)
		if math.fabs(vx) < 1:
			vx = 0
			x = x_min

	ball_pos[0] = int(x)
	ball_pos[1] = int(y)
	ball_velocity[0] = vx
	ball_velocity[1] = vy
	ball_acc[0] = ax
	ball_acc[1] = ay

def check_game_over():
	global ball_pos, state
	y = ball_pos[1]
	r = ball_radius
	y_max = ( 600 + (r + 1) )
	if y > y_max:
		reset()

# 初始化 ---------------------------------------------------
reset()
canvas = pygame.Surface(screen.get_size())
picture = pygame.image.load('ball.png')
picture = pygame.transform.scale(picture, (ball_radius*2+3, ball_radius*2+3))
myfont_small = pygame.font.SysFont('Arial', 30)
myfont = pygame.font.SysFont('Arial', 500)
state = 'START'
score = 0


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

		if state == 'START':
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					check_hit_ball(event.pos)
					if state == 'START':
						state = 'PLAYING'
						score = 0
		elif state == 'PLAYING':
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					check_hit_ball(event.pos)
	# ANIMATION ------------------------------------------------
	clock.tick(60)
	if state == 'START':
		# ----------更新畫面--------------------------------------
		canvas.fill(pygame.Color('BLACK'))
		hint_text = myfont_small.render('Tap to start', True, pygame.Color('LIGHTBLUE'))
		canvas.blit(hint_text, (335, 200))

	elif state == 'PLAYING':
		ball_animation()
		check_game_over()
		# ----------更新畫面--------------------------------------
		canvas.fill(pygame.Color('WHITE'))


	score_text = myfont.render(str(score), True, pygame.Color('LIGHTBLUE'))
	canvas.blit(score_text, (10, 10))
	# pygame.draw.line(canvas, pygame.Color('LIGHTBLUE'), [0, 500], [800, 500], 2)
	# pygame.gfxdraw.filled_circle(canvas, ball_pos[0], ball_pos[1], ball_radius, pygame.Color('LIGHTBLUE'))
	# pygame.gfxdraw.aacircle(canvas, ball_pos[0], ball_pos[1], ball_radius, pygame.Color('LIGHTBLUE'))
	canvas.blit(picture, (ball_pos[0]-ball_radius, ball_pos[1]-ball_radius))
	screen.blit(canvas, (0, 0))
	pygame.display.update()
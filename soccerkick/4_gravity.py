import pygame
pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

x = 400
y = 300
r = 45
vx = 0.0  # x速度
vy = 0.0  # y速度
ax = 0.0  # x加速度
ay = 0.88 # y加速度

canvus = pygame.Surface(SCREEN_SIZE)
clock = pygame.time.Clock()

# 每一幀球的移動
def ball_animation():
	global x, y, vx, vy, ax, ay
	# 牛頓運動定律
	x = int(x + vx)
	y = int(y + vy)
	vx = vx + ax
	vy = vy + ay

running = True
while running:
	# 遊戲事件偵測 ----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
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
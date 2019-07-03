import pygame
pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

x = 400
y = 300
r = 45

canvus = pygame.Surface(SCREEN_SIZE)

# 建立時鐘
clock = pygame.time.Clock()

running = True
while running:
	# 遊戲事件偵測 ----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# 動畫控制 --------------------------------------
	clock.tick(60) # 每秒執行 60 次
	y = y + 1 # 球往下等速移動
	# 更新畫面 --------------------------------------
	canvus.fill(pygame.Color('WHITE'))
	pygame.draw.circle(canvus, pygame.Color('LIGHTBLUE'), (x, y), r)
	screen.blit(canvus, (0, 0))
	pygame.display.update()
	# ----------------------------------------------

pygame.quit()
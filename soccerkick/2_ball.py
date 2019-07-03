import pygame
pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# 球的位置和尺寸 -------------------------------
x = 400 # 橫軸位置
y = 300 # 縱軸位置
r = 45  # 半徑
# --------------------------------------------

canvus = pygame.Surface(SCREEN_SIZE)

running = True
while running:
	# 遊戲事件偵測 ----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# 更新畫面 --------------------------------------
	canvus.fill(pygame.Color('WHITE'))
	pygame.draw.circle(canvus, pygame.Color('LIGHTBLUE'), (x, y), r) # 根據座標和半徑，在畫布上畫出圓形(球)
	screen.blit(canvus, (0, 0))
	pygame.display.update()
	# ----------------------------------------------
pygame.quit()
import pygame
pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# 畫布 -------------------------------------------
canvus = pygame.Surface(SCREEN_SIZE)
# -----------------------------------------------

running = True
while running:
	# 遊戲事件偵測 ----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# 更新畫面 --------------------------------------
	canvus.fill(pygame.Color('WHITE'))
	screen.blit(canvus, (0, 0))
	pygame.display.update()
	# ----------------------------------------------
pygame.quit()
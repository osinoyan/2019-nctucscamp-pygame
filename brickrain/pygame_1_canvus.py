import pygame
pygame.init()

# 設定視窗的長寬大小
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# 畫布
canvus = pygame.Surface(SCREEN_SIZE)

# 是否遊戲結束
running = True
while running:
	# ----------遊戲事件偵測----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# -------------------------------------------------------
	canvus.fill(pygame.Color('WHITE'))
	screen.blit(canvus, (0, 0))
	pygame.display.update()

pygame.quit()
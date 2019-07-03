import pygame
pygame.init()

# 設定視窗的長寬大小
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# 球的位置和尺寸
ball_pos = (400, 300)
ball_radius = 45

# 畫布
canvus = pygame.Surface(SCREEN_SIZE)
# 圖片
picture = pygame.image.load('ball.png')
picture = pygame.transform.scale(picture, (ball_radius*2+3, ball_radius*2+3))

# 是否遊戲結束
running = True
while running:
	# ----------遊戲事件偵測----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# -------------------------------------------------------
	canvus.fill(pygame.Color('WHITE'))
	# pygame.draw.circle(canvus, pygame.Color('LIGHTBLUE'), ball_pos, ball_radius)
	canvus.blit(picture, (ball_pos[0]-ball_radius, ball_pos[1]-ball_radius))
	screen.blit(canvus, (0, 0))
	pygame.display.update()

pygame.quit()
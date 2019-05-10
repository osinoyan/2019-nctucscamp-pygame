import pygame
import pygame.gfxdraw
import sys

pygame.init()

# 設定視窗的長寬大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 是否遊戲結束
gameOver = False

# 文字元件初始化
pygame.font.init()
# 字型設定
myfont = pygame.font.SysFont('Arial', 30)
# 定義顏色: 青色CYAN BLUE
CYAN_BLUE = (75, 139, 190)
# 設定文字內容 (內容, 是否消除鋸齒, 顏色)
text = myfont.render('How are you today?', True, CYAN_BLUE)
text_rect = text.get_rect( center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) )
# screen.blit(text, text_rect)

# PLAYER
player_pos = [400, 300]
player_radius = 15

while not gameOver:
	# ----------遊戲事件偵測----------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		x = player_pos[0]
		y = player_pos[1]
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x -= 3
			elif event.key == pygame.K_RIGHT:
				x += 3

		player_pos = [x, y]


	# ----------更新畫面--------------------------------------
	screen.fill( (0, 0, 0) )
	pygame.gfxdraw.filled_circle(screen, player_pos[0], player_pos[1], player_radius, CYAN_BLUE)
	pygame.gfxdraw.aacircle(screen, player_pos[0], player_pos[1], player_radius, CYAN_BLUE)
	pygame.display.update()
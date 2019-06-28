2019 進修組 Pygame小組 
===
> 王立洋 林冠宇
> 文件連結: https://hackmd.io/s/S1FN2UrsE
> github: https://github.com/osinoyan/2019-nctucscamp-pygame
## Table of Contents

[TOC]

目標
---

- 帶大家寫出一個pygame小遊戲: 
    - ###  ==小精靈==
- 一邊教一些pygame套件常用的模組，再利用教的東西，一邊帶大家寫遊戲

摘要
---
- pygame 套件介紹+安裝
- pygame 基本遊戲架構 (sys.exit() 等等.. 讓遊戲至少可以安詳地開啟和關閉)
    - pygame.init
    - pygame.display.update
    - pygame.quit
- pygame 顯示
    - 設定視窗與圖層(convert)
    - fill
    - pygame.draw
    - pygame.image
    - pygame.font
    - blit
    - 顏色表示、座標軸表示
- pygame 事件
    - pygame.key
    - pygame.mouse
- pygame 動畫
    - pygame.time
- pygame.sprite(角色類別)
    - collision
        - pygame.sprite.collide_rect
### advanced
- read/write file
- sound


### 統一參數命名
> 視窗：screen / 寬：SCREEN_WIDTH / 高：SCREEN_HEIGHT
> 圖片：picture ==因為pygame中有image這個class，怕搞混==
:::success
正片開始
:::
## 套件介紹+安裝
### 介紹 
- Pygame是一群Python語言的模組，顧名思義便是讓Python方便製作遊戲
- 想要快速製作一些邏輯簡單的小遊戲，pygame 是非常不錯的選擇
### 安裝
```bash=
python -m pip install --upgrade pip
python -m pip install pygame
import pygame
```
## 基本遊戲架構
- 初始化
    - `pygame.init()`
- 更新畫面
    - `pygame.display.update()`
- 結束遊戲
    - `pygame.quit()`
    

```python=
#匯入pygame
import pygame
#pygame初始化
pygame.init()

...  #遊戲的初始化與背景設置放在這邊

#開始運行遊戲
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  #終止遊戲判斷
        else 
            ...  #其他遊戲判斷與更新都放在這邊
            
#離開遊戲
pygame.quit()
```

## 顯示圖形/圖片/文字
```python=
#設定視窗大小與名字
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500 #(視窗寬, 視窗高) = (800, 500)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('xxxxxxx')

#新增一個圖層
canvas_1 = pygame.Surface(screen.get_size()).convert()
canvas_1.fill((255, 255, 255)) #將圖層背景設定為白色
```
#### 畫出圖形
```python=
#畫出藍色長方形，左上角座標 = (70, 50)，寬與高 = (40, 30)
pygame.draw.rect(canvas_1, (0, 0, 255), [70, 50, 40, 30])

#畫出黑色圓形，圓心座標 = (20, 30)，半徑 = 10
pygame.draw.circle(canvas_1,(0, 0, 0) , (20, 30), 10)

#畫出紅色直線，線從座標(0, 0)，畫到座標(800, 500)，線粗 = 5
pygame.draw.line(canvas_1, (255, 0, 0), (0, 0), (800, 500), 5)
```
- 電腦顯示的座標軸：原點(0, 0)在左上角，x軸向右，y軸向下
- 顏色表示方法：(紅色 , 綠色 , 藍色)，每個數值0~255
#### 顯示圖片
```python=
#載入圖片
picture = pygame.image.load('picture.png').convert()

#調整圖片為寬與高 = (50, 50)
picture = pygame.transform.scale(picture, (50, 50)).convert()

#將圖片畫到圖層上，左上角座標(100, 80)
canvas_1.blit(picture, (100, 80))
```
- convert的作用
    - 將一個文件名稱輸入load函數，它會輸出一個加載了圖像的Surface
    - 加載完成之後，我們使用Surface中的convert。convert函數也會輸出一個該圖像的新Surface，但圖像被轉換為與我們的顯示(display)相同的像素點格式
    - 由於圖像與屏幕有著同樣的格式，blit時會非常快。如果我們沒有進行轉換，blit函數會更慢，因為它運行時必須把一種格式的像素點轉換為另一種格式
#### 顯示文字
```python=
#設定文字字型與大小
myfont = pygame.font.SysFont("Arial", 24)

# 定義顏色: 青色CYAN BLUE
CYAN_BLUE = (75, 139, 190)

# 設定文字內容 (內容, 是否消除鋸齒, 顏色)
text = myfont.render('How are you today?', True, CYAN_BLUE)

# 建立一個 'text' 尺寸大小的矩形，命名為 'text_rect'
# 並且設定該矩形的中心點為視窗的中心點
text_rect = text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# 將 'text' 文字元件，以text_rect的位置放置在視窗 'screen'
canvas_1.blit(text, text_rect)
```
- text_rect為何可以這樣用？
    - rect本身就代表著一組寬與高，而text.get_rect會回傳一個rect，就可以直接使用在blit上了
- 我的長方形被圓形壓著啦！！！
    - 那是因為先寫了draw.rect，下一行才寫draw.circle才會這樣
    - draw或blit的順序決定了覆蓋順序
- 將圖層更新至視窗
`screen.blit(canvas_1, (0, 0))`

## 事件
- pygame會接受使用者的各種操作 (例如按鍵盤，移動滑鼠等) ，以產生事件
- 事件隨時可能發生，而且量也可能會很大，pygame的做法是把一串的事件存放在一個陣列裡，再一個一個處理。
- 事件陣列
    - `pygame.event.get()`
    - 陣列中各個事件(event)有各種不同的形態(type)，例如鍵盤按下或滑鼠移動等等，而根據型態的不同，事件帶有的參數就不同
#### 鍵盤輸入
```python=
while running:
    #開始偵測事件
    for event in pygame.event.get():
        #當偵測到按鍵按下
        if event.type == KEYDOWN:
            if event.key == K_UP:
                ... #執行按向上鍵的功能
            if event.key == K_a:
                ... #執行按A鍵的功能
                
        #當偵測到按鍵放開
       if event.type == KEYUP:
            ...
```
- 上面的方法是當按下或放開才會偵測，所以如果要讓角色持續移動，而不是按一下走一格的話，要使用下面的寫法
```python=
#偵測按鍵持續輸入
while running:
    #獲得鍵盤輸入情況的一個陣列
    KEY = pygame.key.get_pressed()

    #如果偵測到向上鍵有按著
    if KEY[pygame.K_DOWN]:
        ...
```
#### 滑鼠輸入
```python=
while running:

    #開始偵測事件
    for event in pygame.event.get():
    
        #當偵測到滑鼠按鍵按下
        if event.type == MOUSEKEYDOWN:
            if event.button == 0:
                ... #執行按左鍵的功能(0: 左鍵 / 1: 中鍵 / 2: 右鍵)
            
            #獲得滑鼠按下時的座標(x, y)
            Position = event.pos

        #當偵測到滑鼠按鍵放開
        if event.type == MOUSEKEYUP:
            ...
            
        #當偵測到滑鼠移動
        if event.type == MOUSEMOTION:
        
            #滑鼠按鍵按下狀況(左鍵 , 中鍵 , 右鍵)
            Button = event.buttons
            
            #獲得滑鼠現在座標(x, y)
            Position = event.pos
            
            #獲得滑鼠移動距離
            Distance = event.rel
```
- 同樣的，上面的寫法是當滑鼠有按下或移動才會偵測，如果要持續偵測 (例如讓角色跟著滑鼠移動) ，要使用下面的寫法
```python=
    #偵測滑鼠按鍵持續按著
    KEY_MOUSE = pygame.mouse.get_pressed()
    
    #如果偵測到左鍵有按著
    if KEY_MOUSE[0]:
        ...
        
    #持續偵測滑鼠位置
    Pos_MOUSE = pygame.mouse.get_pos()
    
    #讓角色的位置持續等於滑鼠位置
    player.pos = Pos_MOUSE
```
- 還記得一開始基本遊戲架構的`event.type == pygame.QUIT`嗎？其實它也是一種event，相當於我們關掉視窗的動作，所以如果沒有這個判斷，視窗是關不掉的喔！
- pygame.mouse ==我把滑鼠的部分寫得比較清楚了，看這部分要不要留==
    - `clock.tick(n)`
        - 每秒執行n次
    - `pygame.mouse.get_pressed()`
        - 0: 左鍵
        - 1: 中鍵
        - 2: 右鍵
    - `pygame.mouse.get_pos()`
        - 回傳目前滑鼠位置的坐標串列，位置變數為x,y坐標
```python=
while running:
    clock.tick(30)        #每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:          #按滑鼠左鍵後球可移動
        playing = True
    elif buttons[2]:        #按滑鼠右鍵後球不能移動
        playing = False
```

## 動畫
- 使用一個迴圈，持續更新東西的位置或圖片，就會看起來像是在動了
- pygame.time
    - `pygame.time.Clock()`
        - 建立時間元件
    - `tick(n)`
        - 每秒執行n次
```python=
#建立時間元件
clock = pygame.time.Clock()

#長方形初始位置
Pos_X, Pos_Y = 30, 30

while running:
    clock.tick(30)  #每秒更新30次
    Pos_X += 1  #更新長方形位置
    
    #重新畫出長方形
    pygame.draw.rect(canvas_1, (0, 0, 255), [Pos_X, Pos_Y, 40, 30])
    screen.blit(canvas_1, (0, 0))
```
- 變成貪食蛇啦~
    - 因為draw跟blit只會把新的圖畫上去，但並不會把舊的東西清掉
    - 在draw之前加上`canvas_1.fill(原背景顏色)`就可以把舊的長方形清掉了

## 角色類別
- pygame.sprite
    - 能創造多個相同的物件，除了複製多個物件，還可以進行動畫繪製及碰撞偵測等
```python=
角色群組名稱 = pygame.sprite.Group()
#加入角色物件
角色群組名稱.add(角色物件)
#繪製到畫布上
角色群組名稱.draw(圖層)
```
- collision
    - pygame.sprite.collide_rect()
        - 偵測矩形的碰撞
```python=
spirte_1 = MySprite("sprite_1.png",200,200,1)
sprite_2 = MySprite("sprite_2.png",50,50,1)
result = pygame.sprite.collide_rect(sprite_1,sprite_2)
if result:
    print "Collision occurred"
```








###### tags: `資工營` `進修組` `2019` `pygame`

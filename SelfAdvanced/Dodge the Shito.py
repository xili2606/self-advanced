import subprocess
import sys

try:
    # 尝试导入pygame库
    import pygame
except ImportError:
    # 如果导入失败，使用pip命令安装pygame
    print("pygame is not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    # 安装完毕后再次尝试导入
    import pygame
import pygame
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
size = (700, 500)
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("Dodge the Shito")

# 加载背景图片
background = pygame.image.load('OIP.png').convert()
# 根据需要调整背景图片的大小以匹配窗口大小
background = pygame.transform.scale(background, size)

# Creating the Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the image for the player
        self.image = pygame.image.load('eva01.png').convert_alpha()
        # Resize the image if necessary
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 450

# Load Music
pygame.mixer.music.load("Decisive Battle.mp3")
# Play music
pygame.mixer.music.play(-1)

# create enemy sprites
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file):
        super().__init__()
        # 根据传入的文件名加载图片
        self.image = pygame.image.load(image_file).convert_alpha()
        # 假设所有敌人的大小都一样，可以调整大小
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(size[0] - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > size[1]:
            self.rect.x = random.randrange(size[0] - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

# 创建玩家实例
player = Player()
# 创建精灵组
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# 生成17个敌人，每个敌人使用不同的图片
for i in range(1, 18):
    image_file = f'{i}.png'
    enemy = Enemy(image_file)
    enemies.add(enemy)
    all_sprites.add(enemy)

# 创建时钟对象
clock = pygame.time.Clock()

# Game loop
done = False
start_ticks = pygame.time.get_ticks() # 开始计时
while not done:
    # Handle Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    # 更新所有精灵
    all_sprites.update()

    # Checks for collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        done = True  # If there is a collision effectively ending the game.

    # 在屏幕上绘制背景图片
    screen.blit(background, (0, 0))
    # Draw all the sprites on top of the background
    all_sprites.draw(screen)

    # 更新窗口
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)

# 计算得分
seconds = (pygame.time.get_ticks() - start_ticks) / 1000
print(f"游戏结束！你的得分是：{seconds}秒")

# 退出Pygame
pygame.quit()











# import pygame
# import random

# # initialize
# pygame.init()

# # set the dimensions of the window 
# size = (700, 500)
# screen = pygame.display.set_mode(size)

# # set the title of the window
# pygame.display.set_caption("Dodge the Blocks")




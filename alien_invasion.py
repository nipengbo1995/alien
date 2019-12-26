import sys

import pygame

<<<<<<< HEAD
=======
from settings import Settings

>>>>>>> 2019/12/26-2

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
<<<<<<< HEAD
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

=======
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    bg_color = (230, 230, 230)

>>>>>>> 2019/12/26-2
    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

<<<<<<< HEAD
=======
        # 每次循环都重绘屏幕
        screen.fill(bg_color)

>>>>>>> 2019/12/26-2
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()

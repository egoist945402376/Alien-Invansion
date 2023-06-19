import sys

import pygame

from settings import Settings
from Ship import Ship

def run_game():
    pygame.init()

    ai_settings = Settings()

    # Set_mode 方法返回整个游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_weight, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(screen)

    # background color
    bg_color = ai_settings.bg_color

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()
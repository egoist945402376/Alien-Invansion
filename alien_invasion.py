import sys

import pygame

from settings import Settings
from ship import Ship
from xiaomeiyan import Xiaomeiyan
import game_functions as gf

def run_game():
    pygame.init()

    ai_settings = Settings()

    # Set_mode 方法返回整个游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_weight, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)
    xiaomeiyan = Xiaomeiyan(screen)

    # background color
    bg_color = ai_settings.bg_color

    while True:
        gf.check_events(ship)
        ship.update()
        #Update screen
        gf.update_screen(ai_settings,screen,ship)
        #gf.for_fun_update_screen(ai_settings, screen, ship, xiaomeiyan)

run_game()
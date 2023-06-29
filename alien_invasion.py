import sys

import pygame

from settings import Settings
from ship import Ship
from xiaomeiyan import Xiaomeiyan
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from bullet import Bullet
from alien import Alien


def run_game():
    pygame.init()

    ai_settings = Settings()

    # Set_mode 方法返回整个游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 子弹
    bullets = Group()


    # 外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    xiaomeiyan = Xiaomeiyan(screen)

    # background color
    bg_color = ai_settings.bg_color

    #alien = Alien(ai_settings, screen)

    # 逻辑: 检测按键 做出对应行为 更新对象的属性 再更新屏幕
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            # 调用update时 编组bullets 自动对其内所有精灵对象调用update
            gf.update_bullets(ai_settings,screen, ship, aliens, bullets)
            #Update screen
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)
        #gf.for_fun_update_screen(ai_settings, screen, ship, xiaomeiyan)

run_game()
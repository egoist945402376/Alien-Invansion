import sys

import pygame

from bullet import Bullet
from alien import Alien
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def for_fun_update_screen(ai_settings, screen, ship, xiaomeiyan):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    xiaomeiyan.blitme()

    pygame.display.flip()

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_of_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_of_alines_row = get_number_aliens_row(ai_settings,ship.rect.height, alien.rect.height)
    for i in range(number_of_alines_row):
        for j in range(number_of_aliens_x):
            create_alien(ai_settings, screen, aliens, j, i)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_aliens_row(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_aliens_row = int(available_space_y / (2 * alien_height))
    return number_aliens_row

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    new_alien = Alien(ai_settings, screen)
    alien_width = new_alien.rect.width
    alien_height = new_alien.rect.height
    new_alien.x = alien_width + 2 * alien_number * alien_width
    new_alien.y = alien_height + 2 * row_number * alien_height
    new_alien.rect.x = new_alien.x
    new_alien.rect.y = new_alien.y
    aliens.add(new_alien)


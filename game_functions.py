import sys

import pygame

from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets,stats)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_forward = True
    if event.key == pygame.K_DOWN:
        ship.moving_back = True
    if event.key == pygame.K_SPACE:
        fire_bullet(bullets, screen, ai_settings, ship)
        #if len(bullets) < ai_settings.bullets_allowed:
            #new_bullet = Bullet(ai_settings, screen, ship)
           # bullets.add(new_bullet)
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_p:
        pause_and_resume(stats)
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_forward = False
    if event.key == pygame.K_DOWN:
        ship.moving_back = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

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

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def fire_bullet(bullets, screen, ai_settings, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collisions:
        #print(len(collisions.keys()))
        for aliens in collisions.values():
            #print(len(aliens))
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        sb.prep_level()

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        print("You die.")

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_level()
        sb.prep_high_score()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def pause_and_resume(stats):
    if not stats.game_active:
        stats.game_active = True
    else:
        stats.game_active = False

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
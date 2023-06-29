import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_direction = 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.moving_direction * self.ai_settings.alien_speed_factor
        self.rect.x = self.x
        if self.rect.right > self.screen_rect.right:
            self.moving_direction = -1
            self.y += self.ai_settings.alien_drop_factor
        elif self.rect.left < self.screen_rect.left:
            self.moving_direction = 1
            self.y += self.ai_settings.alien_drop_factor
        self.rect.y = self.y
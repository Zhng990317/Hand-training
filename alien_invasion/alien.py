# -*-coding:utf-8 -*-
# @Date: 2023/6/19 19:52
# @File: alien.py
from pygame.sprite import Sprite
import pygame
alien_image_path = './images/alien.bmp'

class Alien(Sprite):
    def __init__(self, init_settings, screen):
        super().__init__()
        self.screen = screen
        self.init_settings = init_settings

        self.alien_image = pygame.image.load(alien_image_path)
        self.rect = self.alien_image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.alien_image, self.rect)




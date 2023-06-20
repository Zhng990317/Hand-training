# -*-coding:utf-8 -*-
# @Date: 2023/6/19 16:07
# @File: ship.py
import pygame

ship_image_path = './images/ship.bmp'


class Ship:
    def __init__(self, screen, init_settings):
        self.screen = screen
        self.init_settings = init_settings

        self.ship_image = pygame.image.load(ship_image_path)
        self.rect = self.ship_image.get_rect()
        self.screen_rect = screen.get_rect()

        self.center = float(self.rect.centerx)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.ship_image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.init_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.init_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

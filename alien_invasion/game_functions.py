# -*-coding:utf-8 -*-
# @Date: 2023/6/19 16:25
# @File: game_functions.py
import sys
import pygame
from bullet import Bullet

class GameFunction:

    def __init__(self):
        pass

    def check_events(self, ship, init_settings, screen, bullets):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, init_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(ship, event)

    def check_keydown_events(self, event, init_settings, screen, ship, bullets):
        """按下按键"""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # 创建一颗子弹，并将其加入到编组bullets中
            self.fire_bullet(init_settings, screen, ship, bullets)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, ship, event):
        """松开按键"""
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

    def update_screen(self, init_settings, screen, ship, alien, bullets):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕
        screen.fill(init_settings.bg_color)

        # 在飞船和外星人后面重绘所有子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        alien.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def update_bullets(self, bullets):
        """更新子弹的位置，并删除已消失的子弹"""
        # 更新子弹的位置
        bullets.update()
        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

    def fire_bullet(self, init_settings, screen, ship, bullets):
        if len(bullets) < init_settings.bullets_allowed:
            new_bullet = Bullet(init_settings, screen, ship)
            bullets.add(new_bullet)

game_func = GameFunction()

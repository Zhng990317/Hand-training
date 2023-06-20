# -*-coding:utf-8 -*-
# @Date: 2023/6/19 15:25
# @File: alien_invasion.py

import pygame
from settings import Settings
from ship import Ship
from game_functions import game_func
from pygame.sprite import Group
from alien import Alien
# bg_color = (230, 230, 230)

def run_game():
    pygame.init()
    init_settings = Settings()
    screen = pygame.display.set_mode((init_settings.width, init_settings.height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(screen,init_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    alien = Alien(init_settings, screen)

    while True:
        game_func.check_events(ship, init_settings, screen, bullets)
        ship.update()
        game_func.update_bullets(bullets)
        game_func.update_screen(init_settings, screen, ship, alien, bullets)



run_game()

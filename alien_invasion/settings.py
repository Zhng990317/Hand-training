# -*-coding:utf-8 -*-
# @Date: 2023/6/19 15:49
# @File: settings.py
class Settings:
    def __init__(self):
        #screen
        self.height = 800
        self.width = 1200
        self.bg_color = (230, 230, 230)
        #ship
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

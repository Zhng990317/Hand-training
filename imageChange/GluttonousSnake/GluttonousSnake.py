# -*-coding:utf-8 -*-
# @Date: 2023/2/7 19:22
# @File: GluttonousSnake
import random
import time
import pygame
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE


class Food:
    def __init__(self, x, y, surface):
        self.x = 44 * x
        self.y = 44 * y
        self.surface = surface
        self.image = pygame.image.load(r'C:\Users\NineZhang\Pictures\新建文件夹\1.png').convert()

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

class Snake():
    def __init__(self, x, y, surface):
        self.x = [x*44]
        self.y = [y*44]      # 用两个列表来存储贪吃蛇每个节点的位置
        self.length = 1        # 贪吃蛇的长度
        self.direction = 0     # 0表示向右, 1表示向下, 2表示向左, 3表示向上
        self.image = pygame.image.load(r'C:\Users\NineZhang\Pictures\新建文件夹\2.png').convert()       # 加载蛇
        self.surface = surface
        self.step = 44         # 运动步长
        self.updateCount = 0     # 更新次数

        # 虽然有这么多节点,但是有length来控制界面上画出多少蛇的节点
        for i in range(1, 100):
            self.x.append(-100)
            self.y.append(-100)

    def draw(self):
        for i in range(self.length):
            self.surface.blit(self.image, (self.x[i],self.y[i]))

    def update(self):
        self.updateCount += 1
        if self.updateCount > 2:
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            if self.direction == 0:
                self.x[0] = self.x[0] + self.step  # 向右
            if self.direction == 1:
                self.y[0] = self.y[0] + self.step  # 向下
            if self.direction == 2:
                self.x[0] = self.x[0] - self.step  # 向左
            if self.direction == 3:
                self.y[0] = self.y[0] - self.step  # 向上

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 2

    def moveUp(self):
        self.direction = 3

    def moveDown(self):
        self.direction = 1

class SnakeGame:

    def __init__(self):
        self.width = 800
        self.height = 600
        self._running = False

    def init(self):
        pygame.init()
        # 初始化一个准备显示的窗口或屏幕
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        self._running = True
        self.food = Food(5, 5, self._display_surf)
        self.snake = Snake(1, 1, self._display_surf)

    def render(self):
        self._display_surf.fill((0, 0, 0))  # 游戏界面填充为黑色
        self.food.draw()  # 画出食物
        self.snake.draw()
        pygame.display.flip()

    def loop(self):
        self.snake.update()
        self.eat()
        self.faild_check()

    def eat(self):
        if self.isCollision(self.food.x, self.food.y, self.snake.x[0], self.snake.y[0], 40):
            self.food.x = random.randint(2, 9) * 44
            self.food.y = random.randint(2, 9) * 44
            self.snake.length += 1  # 蛇的长度加1

    def faild_check(self):
        # 检查是否吃到了自己
        for i in range(2, self.snake.length):
            if self.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i], 40):
                print('吃到自己了')
                exit(0)

        if self.snake.x[0] < 0 or self.snake.x[0] > self.width \
                or self.snake.y[0] < 0 or self.snake.y[0] > self.height:
            print('出边界了')
            exit(0)

    def listen_keybord(self):
        keys = pygame.key.get_pressed()
        if (keys[K_RIGHT]):
            self.snake.moveRight()
        if (keys[K_LEFT]):
            self.snake.moveLeft()
        if (keys[K_UP]):
            self.snake.moveUp()
        if (keys[K_DOWN]):
            self.snake.moveDown()
        if (keys[K_ESCAPE]):
            self._running = False

    @staticmethod
    def isCollision(x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True

        return False

    def run(self):
        self.init()
        while self._running:
            pygame.event.pump()  # 内部处理pygame事件处理程序
            self.listen_keybord()  # 监听键盘上下左右键
            self.loop()
            self.render()
            time.sleep(0.05)


if __name__ == '__main__':
    snake = SnakeGame()
    snake.run()
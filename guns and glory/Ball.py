from random import randrange as rnd, choice
import tkinter as tk
import math as m


class Ball():
    """Батя пули и цели"""
    def __init__(self, canv):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.canv = canv
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = 0
        self.live = 1
    def hittest(self, obj):
        """Проверка столкновения пули и цели"""
        if m.sqrt((self.x - obj.x) ** 2 +
                  (self.y - obj.y) ** 2) > self.r + obj.r:
            return False
        else:
            return True



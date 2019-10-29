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


class Bullet(Ball):
    def move(self):
        """Движение пули в грави-поле"""
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        self.canv.delete(self.id)
        self.id = self.canv.create_oval(self.x - self.r, self.y - self.r,
                                   self.x + self.r, self.y + self.r,
                                   fill=self.color)
        if self.y + self.r > 600:
            self.vy *= -1
            zy = abs(self.vy) / self.vy
            self.vy = (abs(self.vy) - 2) * zy
        if self.x + self.r > 800 or self.x - self.r < 0:
            self.vx *= -1
            zx = abs(self.vx) / self.vx
            self.vx = (abs(self.vx) - 1) * zx
        if self.y + self.r > 600:
            self.y = 600 - self.r
        if self.x + self.r > 800:
            self.x = 800 - self.r
        elif self.x - self.r < 0:
            self.x = self.r


class Target(Ball):
    def new_target(self, x):
        """ Инициализация новой цели. """
        self.x = x
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        vy = self.vy = rnd(2, 5)
        y = y - vy + vy
        self.live = 1
        color = self.color = 'red'
        self.canv.coords(self.id, x - r, y - r, x + r, y + r)
        self.canv.itemconfig(self.id, fill=color)
        self.canv.delete(self.id)
        self.id = self.canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
    def move(self):
        """Движение вне поля, просто по траектории, так красивее"""
        self.y -= self.vy
        self.canv.delete(self.id)
        self.id = self.canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        if self.y + self.r > 600 or self.y - self.r < 0:
            self.vy *= -1
        if self.y + self.r > 600:
            self.y = 600 - self.r
        elif self.y - self.r < 0:
            self.y = self.r

    def hit(self):
        """Уничтожение мишени, начисление очков"""
        global id_points, points
        self.canv.coords(self.id, -10, -10, -10, -10)
        self.canv.delete(self.id)

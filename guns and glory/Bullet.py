from random import randrange as rnd, choice
import tkinter as tk
import math as m
import Ball as B

class Bullet(B.Ball):
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

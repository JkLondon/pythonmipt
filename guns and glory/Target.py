from random import randrange as rnd, choice

import Ball as B

lives = 0


class Target(B.Ball):
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

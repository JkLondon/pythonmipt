import math as m
import Bullet as Bl


bullet = 0
balls = []


class Gun():
    """Создание пушки"""
    def __init__(self, canv):
        self.canv = canv
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        """Начало выстрела, пушка на взводе"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выпускание пули"""
        global balls, bullet
        bullet += 1
        new_ball = Bl.Bullet(self.canv)
        new_ball.r += 5
        new_ball.x = 20 + max(self.f2_power, 20) * m.cos(self.an)
        new_ball.y = 450 + max(self.f2_power, 20) * m.sin(self.an)
        if event.x != new_ball.x:
            self.an = m.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        else:
            self.an = m.pi / 2
        new_ball.vx = self.f2_power * m.cos(self.an)
        new_ball.vy = - self.f2_power * m.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.x != 20:
                self.an = m.atan((event.y - 450) / (event.x - 20))
            else:
                self.an = m.pi / 2
        if self.f2_on:
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')
        self.canv.coords(self.id, 20, 450,
                        20 + max(self.f2_power, 20) * m.cos(self.an),
                        450 + max(self.f2_power, 20) * m.sin(self.an)
                        )

    def power_up(self):
        """Увеличение мощности, регулируется долгим нажатием"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')

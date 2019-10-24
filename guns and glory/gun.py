from random import randrange as rnd, choice
import tkinter as tk
import math as m
import time
import datetime as dt


# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = 0
        self.live = 1

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        canv.delete(self.id)
        self.id = canv.create_oval(self.x - self.r, self.y - self.r,
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

    def hittest(self, obj):
        if m.sqrt((self.x - obj.x) ** 2 +
                  (self.y - obj.y) ** 2) > self.r + obj.r:
            return False
        else:
            return True


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = ball()
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
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * m.cos(self.an),
                    450 + max(self.f2_power, 20) * m.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


id_points = canv.create_text(30, 30, text=0, font='28')
points = 0


class target():
    def __init__(self):
        self.live = 1
        self.id = 0
        self.vx = 0
        self.vy = 0

    def new_target(self, x):
        """ Инициализация новой цели. """
        self.x = x
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        vy = self.vy = rnd (2,5)
        self.live = 1
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)
        canv.delete(self.id)
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def move(self):
        self.y -= self.vy
        canv.delete(self.id)
        self.id = canv.create_oval(
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
        global id_points, points
        canv.coords(self.id, -10, -10, -10, -10)
        points += 1
        canv.itemconfig(id_points, text=points)
        

t = [None] * 2
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
lives = 0


def new_game(event=''):
    global g1, t, screen1, balls, bullet, lives
    for i in range(len(t)):
        t[i] = target()
        t[i].new_target(400 + 110 * i)
        t[i].live = 1
        lives += 1
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    zzz = 0.03
    while lives:
        for i in range(len(t)):
            if t[i].live:
                t[i].move()
        for b in balls:
            if b.live:
                b.move()
                for i in range(len(t)):
                    '''
                    if t[i].live:
                        t[i].move()'''
                    if b.hittest(t[i]) and t[i].live:
                        t[i].live = 0
                        t[i].hit()
                        canv.delete(b.id)
                        canv.delete(t[i].id)
                        b.live = 0
                        lives -= 1
        canv.update()
        time.sleep(zzz)
        g1.targetting()
        g1.power_up()
    for i in balls:
        canv.delete(i.id)
    balls = []
    tx = dt.datetime.now()
    delta =  1
    canv.bind('<Button-1>', '')
    canv.bind('<ButtonRelease-1>', '')
    canv.itemconfig(screen1, text='Вы уничтожили 2 цели за ' +
                    str(bullet) + ' выстрелов')
    while (dt.datetime.now() - tx).seconds < delta:
        canv.update()
        time.sleep(zzz)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    root.after(1, new_game)


new_game()
tk.mainloop()

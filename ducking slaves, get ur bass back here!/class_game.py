import tkinter as tk
from random import randrange as rnd, choice
import time
import math as m


root = tk.Tk()
root.geometry('800x600')
tk.canv = tk.Canvas(root, bg = 'white')
tk.canv.pack(fill = tk.BOTH, expand = 1)


class Ball:
    
    ball_count = 0
    colorsb = ['red', 'orange' , 'yellow', 'green', 'blue']
    def __init__(self, x, y, r, v, angle, color, number):
        Ball.ball_count += 1
        self.x = x
        self.y = y
        self.r = r
        self.angle = angle
        self.v = v
        self.number = number

    def draw_ball(i):
        x = rnd(10,700)
        y = rnd(10,550)
        r = rnd(30,50)
        v = rnd(1,5)
        q = rnd(0,2)
        z=1
        if q:
            z=-2
        angle = (rnd(1,180) * z)%180
        curcol = choice(colorsb)
        coors[i] = [x, y, r]
        colors[i] = curcol
        tk.canv.create_oval(x - r,y - r, x + r, y + r, fill =
                                           curcol, width = 0)
        return Ball(x, y, r, v, angle, curcol, i)
n = int(input())
score = 0    
tk.canv.bind('<Button-1>', click)
L = tk.Label(root, bg='black', fg='white', width=20)
L.pack()
balls= [None] * n
for i in range(n):
    balls[i] = Ball()
    balls[i] = balls[i].draw_ball(i)
move()

tk.mainloop()

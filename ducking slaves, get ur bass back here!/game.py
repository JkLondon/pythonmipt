import csv
import datetime as dt
import math as m
import tkinter as tk
from random import randrange as rnd, choice

root = tk.Tk()
root.geometry('800x600')
tk.canv = tk.Canvas(root, bg='white')
tk.canv.pack(fill=tk.BOTH, expand=1)
colorsb = ['red', 'orange', 'yellow', 'green', 'blue']


def file_reader(file_obj, path):
    file_obj = open(path, 'r')
    data = []
    for i in file_obj:
        i = i.split(',')
        i[0] = int(i[0])
        data.append(i)
    return file_obj, data


def draw_ball(i):
    global balls, coors, colors, v, angle
    x = rnd(10, 700)
    y = rnd(10, 550)
    r = rnd(30, 50)
    v[i] = rnd(1, 5)
    q = rnd(0, 2)
    z = 1
    if q:
        z = -1
    angle[i] = (rnd(1, 180) * z) % 180
    curcol = choice(colorsb)
    coors[i] = [x, y, r]
    colors[i] = curcol
    balls[i] = tk.canv.create_oval(x - r, y - r, x + r, y + r, fill=
    curcol, width=0)


def move_ball(i):
    global balls, coors, colors, v, angle
    x = coors[i][0]
    y = coors[i][1]
    r = coors[i][2]
    curcol = colors[i]
    balls[i] = tk.canv.create_oval(x - r, y - r, x + r, y + r, fill=
    curcol, width=0)


def click(event):
    my_x, my_y = event.x, event.y
    for i in range(len(balls)):
        x, y, r = coors[i][0], coors[i][1], coors[i][2]
        if m.sqrt((x - my_x) ** 2 + (y - my_y) ** 2) <= r:
            eliminate(i)
            break


def eliminate(i):
    global balls, coors, score, L
    tk.canv.delete(balls[i])
    draw_ball(i)
    L['text'] = str(score + 1)
    score += 1
    return


def move():
    global balls, coors, v, angle, name, data
    tk.canv.delete(tk.ALL)
    if (dt.datetime.now() - tx).seconds > delta:
        data.append([score, name])
        data = sorted(data)
        path = 'results.csv'
        file_obj = open(path, 'w')
        for i in range(len(data)):
            fstr = str(data[i][0]) + ',' + str(data[i][1])
            file_obj.write(fstr + '"')
        file_obj.close()
        return
    for i in range(n):
        for j in range(n):
            if i != j and m.sqrt((coors[i][0] - coors[j][0]) ** 2 +
                                                 (coors[i][1] - coors[j][1]) ** 2) <= coors[i][2] + coors[j][2]:
                collision(i, j)
    for i in range(n):
        coors[i][0] += v[i] * m.cos(angle[i] * (m.pi / 180))
        coors[i][1] += v[i] * m.sin(angle[i] * (m.pi / 180))
        move_ball(i)
    for i in range(n):
        crosstheborder(i)
    for i in range(n):
        coors[i][0] += v[i] * m.cos(angle[i] * (m.pi / 180))
        coors[i][1] += v[i] * m.sin(angle[i] * (m.pi / 180))
        move_ball(i)
    root.after(4, move)


def collision(i, j):
    global angle, coors
    m1 = coors[i][2] ** 2
    m2 = coors[j][2] ** 2
    c1x = coors[i][0] + coors[i][2]
    c2x = coors[j][0] + coors[j][2]
    c1y = coors[i][1] + coors[i][2]
    c2y = coors[j][1] + coors[j][2]
    v1 = v[i]
    v2 = v[j]
    if c2x - c1x == 0:
        fi = 90
    else:
        fi = m.atan((c2y - c1y) /
                    (c2x - c1x)) / m.pi * 180
    aL1 = angle[i] - fi
    aL2 = angle[j] - fi
    aL1 *= m.pi / 180
    aL2 *= m.pi / 180
    if m.cos(aL2) == 0:
        b1 = m.pi / 2
    else:
        b1 = m.atan((m1 * v1 * m.sin(aL1)) / (m2 * v2 * m.cos(aL2)))
    if m.cos(aL1) == 0:
        b2 = m.pi / 2
    else:
        b2 = m.atan((m2 * v2 * m.sin(aL2)) / (m1 * v1 * m.cos(aL1)))
    if b1 == 0 and m.cos(aL2) < 0:
        b1 = -1 * m.pi
    if b2 == 0 and m.cos(aL1) < 0:
        b2 = -1 * m.pi
    if b1 < 0 and aL1 > 0:
        b1 += m.pi
    if b2 < 0 and aL2 > 0:
        b2 += m.pi
    fi *= m.pi / 180
    angle[i] = (fi + b1) / m.pi * 180
    angle[j] = (fi + b2) / m.pi * 180
    v[i] = m.sqrt((m2 * v2 * m.cos(aL2) / m1) ** 2 +
                  (v1 * m.sin(aL1)) ** 2)
    v[j] = m.sqrt((m1 * v1 * m.cos(aL1) / m2) ** 2 +
                  (v2 * m.sin(aL2)) ** 2)
    delt = coors[i][2] + coors[j][2] - m.sqrt((c1x - c2x) ** 2 + (c1y - c2y)
                                              ** 2)
    if c2y != c1y:
        coors[i][1] += delt * m.sin(fi) * (c1y - c2y) / abs(c1y - c2y) / 2
        coors[j][1] -= delt * m.sin(fi) * (c1y - c2y) / abs(c1y - c2y) / 2
    if c1x != c2x:
        coors[i][0] += delt * m.cos(fi) * (c1x - c2x) / abs(c1x - c2x) / 2
        coors[j][0] -= delt * m.cos(fi) * (c1x - c2x) / abs(c1x - c2x) / 2


def crosstheborder(i):
    global angle, coors
    if coors[i][0] + coors[i][2] > 800:
        if angle[i] < 0:
            angle[i] = (180 - abs(angle[i])) * (-1)
        else:
            angle[i] = 180 - angle[i]
        coors[i][0] = 800 - coors[i][2]
    elif coors[i][0] - coors[i][2] < 0:
        if angle[i] < 0:
            angle[i] = (180 - abs(angle[i])) * (-1)
        else:
            angle[i] = 180 - angle[i]
        coors[i][0] = coors[i][2] + 5
    elif coors[i][1] + coors[i][2] > 580:
        angle[i] *= -1
        coors[i][1] = 580 - coors[i][2]
    elif coors[i][1] - coors[i][2] < 0:
        angle[i] *= -1
        coors[i][1] = coors[i][2] + 5
    if angle[i] != 180 and angle[i] != -180:
        if angle[i] <= 0:
            angle[i] = (abs(angle[i]) % 180) * (-1)
        else:
            angle[i] = abs(angle[i]) % 180


print("Enter your name, dude!")
name = input()
n = int(input())
balls = [0] * n
colors = [0] * n
coors = [[0] * 3] * n
v = [0] * n
angle = [0] * n
score = 0
tk.canv.bind('<Button-1>', click)
L = tk.Label(root, bg='black', fg='white', width=20)

L.pack()
tx = dt.datetime.now()
delta = 30
for i in range(n):
    draw_ball(i)
move()
f = None
f, data = file_reader(f, 'results.csv')
tk.mainloop()

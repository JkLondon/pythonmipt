import datetime as dt
import time
import tkinter as tk
import Bullet as Bl
import Target as Tg
import gun as G

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
t = [None] * 2
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = G.Gun(canv)
bullet = 0
id_points = canv.create_text(30, 30, text=0, font='28')


def new_game(event=''):
    """Само тело игры"""
    global g1, t, screen1, balls, bullet, lives, id_points, points
    for i in range(len(t)):
        t[i] = Tg.Target(canv)
    t[i].new_target(400 + 110 * i)
    t[i].live = 1
    Tg.lives += 1


canv.bind('<Button-1>', g1.fire2_start)
canv.bind('<ButtonRelease-1>', g1.fire2_end)
canv.bind('<Motion>', g1.targetting)
zzz = 0.03
while Tg.lives:
    for i in range(len(t)):
        if t[i].live:
            t[i].move()
    for b in G.balls:
        if b.live:
            b.move()
            for i in range(len(t)):
                '''
                if t[i].live:
                    t[i].move()'''
                if b.hittest(t[i]) and t[i].live:
                    t[i].live = 0
                    t[i].hit()
                    Bl.points += 1
                    canv.itemconfig(id_points, text=Bl.points)
                    canv.delete(b.id)
                    b.live = 0
                    Tg.lives -= 1
    canv.update()
    time.sleep(zzz)
    g1.targetting()
    g1.power_up()
for i in G.balls:
    canv.delete(i.id)
G.balls = []
tx = dt.datetime.now()
delta = 1
canv.bind('<Button-1>', '')
canv.bind('<ButtonRelease-1>', '')
canv.itemconfig(screen1, text='Вы уничтожили 2 цели за ' +
                              str(G.bullet) + ' выстрелов')
while (dt.datetime.now() - tx).seconds < delta:
    canv.update()
    time.sleep(zzz)
    g1.targetting()
    g1.power_up()
G.bullet = 0
Bl.points = 0
canv.itemconfig(screen1, text='')
canv.itemconfig(id_points, text=0)
root.after(1, new_game)

new_game()
tk.mainloop()

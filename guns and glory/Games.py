import datetime as dt
import time
import tkinter as tk
import Bullet as Bl
import Gun as G
import Target as Tg


class Game:
    def __init__(self):
        """Параметры игры"""
        self.root = tk.Tk()
        self.fr = tk.Frame(self.root)
        self.root.geometry('800x600')
        self.canv = tk.Canvas(self.root, bg='white')
        self.canv.pack(fill=tk.BOTH, expand=1)
        self.t = [None] * 2
        self.screen1 = self.canv.create_text(400, 300, text='', font='28')
        self.g1 = G.Gun(self.canv)
        self.bullet = 0
        self.id_points = self.canv.create_text(30, 30, text=0, font='28')
        self.canv.bind('<Button-1>', self.g1.fire2_start)
        self.canv.bind('<ButtonRelease-1>', self.g1.fire2_end)
        self.canv.bind('<Motion>', self.g1.targetting)
        self.event = ''
        self.zzz = 0.03
    def new_game(self):
        """Само тело игры"""
        print("HERE")
        for i in range(len(self.t)):
            self.t[i] = Tg.Target(self.canv)
            self.t[i].new_target(400 + 110 * i)
            self.t[i].live = 1
            Tg.lives += 1
        while Tg.lives:
            for i in range(len(self.t)):
                if self.t[i].live:
                    self.t[i].move()
            for b in G.balls:
                if b.live:
                    b.move()
                    for i in range(len(self.t)):
                        '''
                        if t[i].live:
                            t[i].move()'''
                        if b.hittest(self.t[i]) and self.t[i].live:
                            self.t[i].live = 0
                            self.t[i].hit()
                            Bl.points += 1
                            self.canv.itemconfig(self.id_points, text=Bl.points)
                            self.canv.delete(b.id)
                            b.live = 0
                            Tg.lives -= 1
            self.canv.update()
            time.sleep(self.zzz)
            self.g1.targetting()
            self.g1.power_up()
        for i in G.balls:
            self.canv.delete(i.id)
        G.balls = []
        tx = dt.datetime.now()
        delta = 1
        self.canv.itemconfig(self.screen1, text='Вы уничтожили 2 цели за ' +
                                      str(G.bullet) + ' выстрелов')
        while (dt.datetime.now() - tx).seconds < delta:
            self.canv.update()
            time.sleep(self.zzz)
            self.g1.targetting()
            self.g1.power_up()
        G.bullet = 0
        Bl.points = 0
        self.canv.itemconfig(self.screen1, text='')
        self.canv.itemconfig(self.id_points, text=0)
        self.root.after(1, self.new_game)

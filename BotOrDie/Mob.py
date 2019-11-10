import tkinter as tk


class Mob(tk.Tk):
    def __init__(self):
        self.x = 0
        self.y = 200
        tk.Tk.__init__(self)
        self.spritesheet = tk.PhotoImage(file=".\images\Mario.gif")
        self.canvas = tk.Canvas(self, width=100, height=100)
        self.canvas.pack()

    def updateMob(self):

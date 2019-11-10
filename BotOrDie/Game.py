import tkinter as tk
import Mob as M
import Physics as Ph


class Game:
    def __init__(self):
        """Параметры игры"""
        self.root = tk.Tk()
        self.fr = tk.Frame(self.root)
        self.root.geometry('800x600')
        self.canv = tk.Canvas(self.root, bg='white')
        self.canv.pack(fill=tk.BOTH, expand=1)
        self.Mario = M.Mob()

    def new_game(self):
        self.root.bind('<Button-1>',Ph.move(self.Mario))
        self.root.after(1, self.new_game)
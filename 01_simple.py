# coding: utf-8
"""
Использование графического модуля graph.py.
GR_SIMPLE - простые программы
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *
penColor(140,129,46)
brushColor(140,129,46)
polygon([(0,15), (250,500), 
         (0,500)])
penColor(36,75,72)
brushColor(36,75,72)
polygon([(15,0), (273,500), 
         (500,500), (500,0)])
polygon([(10,5), (5,10), 
         (258,500), (265,500)])
penColor("black")
penSize(5)
brushColor("brown")
polygon([(0,15), (250,500), 
         (258,500), (5,10)])
polygon([(10,5), (265,500), 
         (273,500), (15,0)])

penSize(1)
brushColor("black")
polygon([(125,500), (125,300), 
         (200,300), (200,500)])
brushColor(255,168,85)
penColor(255,168,85)
circle(163,280,30)
penColor("black")
circle(163,290,5)
penColor(230,171,67)
brushColor(230,171,67)
circle(250,130,100)
circle(400,300,60)
penSize(10)
point(153,270,"black")
point(173,270,"black")
penSize(1)
penColor("black")
brushColor(255,168,85)
polygon([(150,310), (140,315), 
         (130,280), (140,275)])
polygon([(176,310), (186,315), 
         (196,280), (183,275)])

run()

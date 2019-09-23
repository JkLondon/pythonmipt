import turtle as t
import math
from time import sleep
gpi=180
def nug(n,x):
	vnug=gpi*(n-2)/n
	ugpov=gpi-vnug
	t.right(vnug/2)
	for i in range(n):
		t.forward(x)
		t.left(ugpov)
	t.left(vnug/2)
def a(R,n):
	return 2*R*math.sin(math.pi/n) 
R=10
t.left(gpi)
somepoint=30
for i in range(3,13): #треуг-тренадуг
	nug(i,a(R,i))
	t.penup()
	t.backward(somepoint)
	R+=somepoint
	t.pendown()


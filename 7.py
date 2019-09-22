import turtle as t
import math
p1=1
line=180
k=10
for i in range(1,10000):
	t.left(p1)
	t.forward((i*math.pi/line)/k)

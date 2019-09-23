import turtle as t
from time import sleep
t.speed(1000)
one_degree=1
twopi=360
turn=60
def circle(rl):
	for i in range(twopi):
		t.forward(one_degree)
		if rl==0:
			t.left(one_degree)
		else:
			t.right(one_degree)
for i in range(1,444):
	for rl in range(2):
		circle(rl)
	t.left(turn)

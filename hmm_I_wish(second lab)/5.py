import turtle as t

for i in range(10,101,10):
	for j in range(4):
		t.forward(i)
		t.left(90)
	t.penup()
	t.backward(5)
	t.right(90)
	t.forward(5)
	t.left(90)
	t.pendown()

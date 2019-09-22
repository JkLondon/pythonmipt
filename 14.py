import turtle as t
tpi=360
pi=180

def star(n):
    for i in range(n):
        t.forward(100)
        if n % 2 == 1:
            t.right(pi - pi / n)
        else:
            t.right(pi - tpi / n)


star(5)
t.right(180)
t.penup()
t.forward(100)
t.pendown()

star(11)

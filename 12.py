import turtle as t
gpi=180
def dugin(n):
    for i in range(gpi//n):
        t.forward(1)
        t.right(n)
lenght=20
halfpi=90
t.left(gpi)
t.penup()
t.forward(300)
t.left(gpi)
t.pendown()
t.left(halfpi)
for i in range(lenght):
    dugin(1)
    dugin(10)

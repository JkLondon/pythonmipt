import turtle as t


def half_of_circle(R, side='r', color='black'):
    t.color(color)
    t.width(10)
    for i in range(int(180 * R)):
        t.forward(0.5)
        if side == 'l':
            t.left(1 / R)
        else:
            t.right(1 / R)


def circle(R, side='r', color='white'):
    t.color(color)
    t.begin_fill()
    for i in range(int(360 * R)):
        t.forward(0.5)
        if side == 'l':
            t.left(1 / R)
        else:
            t.right(1 / R)
    t.end_fill()


circle(4, 'l', "yellow")
t.left(90)
t.forward(190)
t.left(90)
t.forward(57)
circle(1, 'l', 'blue')
t.penup()
t.right(180)
t.forward(114)
t.pendown()
circle(1, color='blue')
t.penup()
t.backward(57)
t.right(90)
t.forward(38)
t.width(10)
t.color('black')
t.pendown()
t.forward(76)
t.penup()
t.left(90)
t.forward(57)
t.right(90)
t.pendown()
half_of_circle(2, 'r', 'red')

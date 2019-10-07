import graph as g


def keyPressed(event):
    global dx, dy, ex, ey
    if event.keycode == g.VK_LEFT:
        dx = -5
        dy = 0
        ex = 0
        ey = 0
    elif event.keycode == g.VK_RIGHT:
        dx = 5
        dy = 0
        ex = 0
        ey = 0
    elif event.keycode == g.VK_UP:
        dx = 0
        dy = -5
        ex = 0
        ey = 0
    elif event.keycode == g.VK_DOWN:
        dx = 0
        dy = 5
        ex = 0
        ey = 0
    elif event.keycode == g.VK_TAB:
        dx = 0
        dy = 0
        ex = -5
        ey = 0
    elif event.keycode == g.VK_DELETE:
        dx = 0
        dy = 0
        ex = 5
        ey = 0
    elif event.keycode == g.VK_SPACE:
        updatemouth()  # вызов сатаны (если разкомментишь)
        print("DUUUUUUUUCK")
        dx = 0
        dy = 0
        ex = 0
        ey = 0
    elif event.keycode == g.VK_BACK:
        # movelefthand()  разработке
        dx = 0
        dy = 0
        ex = 0
        ey = 0
    elif event.keycode == g.VK_ESCAPE:
        g.close()
    else:
        pass
    updateeyes()
    updateman()


def crosstheborder(x, y, blx, bly, bux, buy):
    global dx, dy

    if (x - blx)*(buy - bly)-(y - bly)*(bux - blx) >= 0:
        return (-10, 10)
    elif x <= 75:
        return (10, 0)
    elif y >= 500:
        return (0, -10)
    else:
        return (dx, dy)


def moveobs(a, x, y):
    for i in a:
        g.moveObjectBy(i, x, y)


def updateman():
    global dx, dy
    x = g.xCoord(body) + 75
    y = g.yCoord(body) + 200
    a = crosstheborder(x, y, 0, 15, 250, 500)
    dx = a[0]
    dy = a[1]
    moveobs([body, head, rhand, lhand, mouth, leye, reye], dx, dy)


def updateeyes():
    global ex, ey
    xl = g.xCoord(leye)
    xr = xl + 20
    xh, yh = g.center(head)
    if xl < xh - 30:
        ex = 10
    elif xr > xh + 10:
        ex = -10
    g.moveObjectBy(leye, ex, ey)
    g.moveObjectBy(reye, ex, ey)


def updatemouth():
    global dm, mouth
    x, y = g.center(mouth)
    g.deleteObject(mouth)
    mouth = g.circle(x, y, dm + 1)
    dm += 1
    if dm > 10:
        dm = 4
    return


dx, dy, ex, ey = 0, 0, 0, 0


# floor
g.penColor(140, 129, 46)
g.brushColor(140, 129, 46)
g.polygon([(0, 15), (250, 500), (0, 500)])

# sea
g.penColor(36, 75, 72)
g.brushColor(36, 75, 72)
g.polygon([(15, 0), (273, 500), (500, 500), (500, 0)])

# background of fence
g.polygon([(10, 5), (5, 10), (258, 500), (265, 500)])

# fence
g.penColor("black")
g.penSize(5)
g.brushColor("brown")
g.polygon([(0, 15), (250, 500), (258, 500), (5, 10)])  # lower
g.polygon([(10, 5), (265, 500), (273, 500), (15, 0)])  # upper

# islands
g.penColor(230, 171, 67)
g.brushColor(230, 171, 67)
g.circle(250, 130, 100)  # upper
g.circle(400, 300, 60)  # lower

# body
g.penSize(1)
g.penColor("black")
g.brushColor("black")
body = g.polygon([(125, 500), (125, 300), (200, 300), (200, 500)])

# head
g.brushColor(255, 168, 85)
g.penColor(255, 168, 85)
head = g.circle(163, 280, 30)

# mouth
dm = 4
g.penColor("black")
mouth = g.circle(163, 290, dm)

# eyes
g.penSize(10)
leye = g.point(153, 270, "black")  # left
reye = g.point(173, 270, "black")  # right

# hands
g.penSize(1)
g.penColor("black")
g.brushColor(255, 168, 85)
lhand = g.polygon([(140, 315), (130, 280), (140, 275), (150, 310)])  # left
lh = [(140, 315), (130, 280), (140, 275), (150, 310)]
rhand = g.polygon([(176, 310), (186, 315), (196, 280), (183, 275)])  # right
rh = [(176, 310), (186, 315), (196, 280), (183, 275)]

g.onKey(keyPressed)

g.run()

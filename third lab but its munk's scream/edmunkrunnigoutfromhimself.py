import graph as g
from math import *
import random


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

def ellips1(xc, yc, a, b, fi=0):
    l=[]
    for x in range(-a, a):
        y = ((1 - x**2 / a**2) * b**2) ** (1/2)
        l.append((xc + cos(fi) * x + sin(fi) * y, \
                  (yc - sin(fi) * x + cos(fi) * y)))
    for x in range(a, -a, -1):
        y = ((1 - x**2 / a**2) * b**2) ** (1/2)
        l.append((xc + cos(fi) * x + sin(fi) * (-y), \
                  (yc - sin(fi) * x + cos(fi) * (-y))))
    g.polygon(l)


def ellips():
    #wanted to do this: ellips(xc1 = xc, yc1 = yc, a1 = a, b1 = b, fi1 = fi)
    g.brushColor(230, 171, 67)
    global xc, yc, a, b, fi, ell
    g.deleteObject(ell)
    l=[]
    for x in range(-a, a):
        y = ((1 - x**2 / a**2) * b**2) ** (1 / 2)
        l.append((xc + cos(fi) * x + sin(fi) * y, \
                  (yc - sin(fi) * x + cos(fi) * y)))
    for x in range(a, -a, -1):
        y = ((1 - x**2 / a**2) * b**2) ** (1 / 2)
        l.append((xc + cos(fi) * x + sin(fi) * (-y), \
                  (yc - sin(fi) * x + cos(fi) * (-y))))
    ell = g.polygon(l)
    fi += 0.02

def spiral():
    global xc, yc, a, b, k, fi, sp
    g.penColor('black')
    g.penSize(3)
    g.deleteObject(sp)
    r = 5
    n = 20000
    points = []
    for i in range(n):
        x = (r / 2 * cos(r / k)) * a / b
        y = r / 2 * sin(r / k)
        points.append((xc + cos(fi) * x + sin(fi) * y, \
                  (yc - sin(fi) * x + cos(fi) * y)))
        r += 0.01
        
    sp = g.polyline(points)


dx, dy, ex, ey = 0, 0, 0, 0


# sea
g.penColor(36, 75, 72)
g.brushColor(36, 75, 72)
g.polygon([(0, 0), (0, 500), (500, 500), (500, 0)])
for i in range(20):
    g.brushColor(36 + random.randint(0, 20), 75 + i, 72 + i)
    g.penColor(g.brushColor())
    l = random.randint(40, 120)
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    ellips1(x, y, l, l/4, -pi / 2 * (500 - x / 3)*(500 - y / 4))

# border
g.brushColor('black')
g.rectangle(0, 500, 500, 600)


# floor
g.penColor(140, 129, 46)
g.brushColor(140, 129, 46)
g.polygon([(0, 15), (250, 500), (0, 500)])

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
#g.circle(400, 300, 60)  # lower

# spirals
sp = g.point(350, 280)
ell = g.point(350, 280)
xc = 350
yc = 280
a = 100
b = 50
k = 10
fi = 0

spiral()


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
g.onTimer(spiral, 10)
g.onTimer(ellips, 10)


g.run()

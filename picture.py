import graph as g
import random
import math


def keyPressed(event):
    global Dx, Dy, light
    Dx = 0
    Dy = 0
    if event.keycode == g.VK_ESCAPE:
        g.close()
    elif event.keycode == g.VK_LEFT:
        Dx = -5
        Dy = 0
    elif event.keycode == g.VK_RIGHT:
        Dx = 5
        Dy = 0
    elif event.keycode == g.VK_UP:
        Dx = 0
        Dy = -5
    elif event.keycode == g.VK_DOWN:
        Dx = 0
        Dy = 5
    elif event.keycode == g.VK_SPACE:
        turnlights()
    else:
        pass
    move_ghost()


def ellips(xc, yc, a, b, fi=0):
    L = []
    for x in range(-a, a):
        y = ((1 - x**2 / a**2) * b**2) ** (1/2)
        L.append((xc + math.cos(fi) * x + math.sin(fi) * y,
                  (yc - math.sin(fi) * x + math.cos(fi) * y)))
    for x in range(a, -a, -1):
        y = ((1 - x**2 / a**2) * b**2) ** (1/2)
        L.append((xc + math.cos(fi) * x + math.sin(fi) * (-y),
                  (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
    g.polygon(L)


def ellipse(xc, yc, a1, b1, a2, b2, fi=0):
    L = []
    if b1 < 0:
        for x in range(-a1, a1, 1):
            y = ((1 - x**2 / a2**2) * b1**2) ** (1/2)
            L.append((xc + math.cos(fi) * x + math.sin(fi) * (-y),
                      (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
        for x in range(a2, -a2, -1):
            y = ((1 - x**2 / a2**2) * b2**2) ** (1/2)
            L.append((xc + math.cos(fi) * x + math.sin(fi) * (-y),
                      (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
    elif b2 < 0:
        for x in range(a1, -a1, -1):
            y = ((1 - x**2 / a1**2) * b1**2) ** (1/2)
            L.append((xc + math.cos(fi) * x + math.sin(fi) * y,
                      (yc - math.sin(fi) * x + math.cos(fi) * y)))
        for x in range(-a2, a2):
            y = ((1 - x**2 / a2**2) * b2**2) ** (1/2)
            L.append((xc + math.cos(fi) * x + math.sin(fi) * y,
                      (yc - math.sin(fi) * x + math.cos(fi) * y)))
    else:
        for x in range(a1, -a1, -1):
            y = ((1 - x**2 / a1**2) * b1**2) ** (1/2)
            L.append((xc + math.cos(fi) * x + math.sin(fi) * y,
                      (yc - math.sin(fi) * x + math.cos(fi) * y)))
        for x in range(-a2, a2):
            y = ((1 - x**2 / a2**2) * b2**2) ** (1/2)
            L.append((xc + math.cos(fi) * x + math.sin(fi) * (-y),
                      (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
    g.brushColor('light yellow')
    g.penColor('black')
    return g.polygon(L)


def move_ghost():
    global x, Dx, Dy, y
    global head, body, eye1, eye2
    g.brushColor('lightgray')
    g.moveObjectBy(head, Dx, Dy)
    g.moveObjectBy(body, Dx, Dy)
    g.brushColor('black')
    g.moveObjectBy(eye1, Dx, Dy)
    g.moveObjectBy(eye2, Dx, Dy)
    g.brushColor('white')
    g.moveObjectBy(blood, Dx, Dy)
    x += Dx
    y += Dy


def windows(r, gr, b):
    for i in range(3):
        delta = random.randint(0, 100)
        g.brush_color = g.brushColor(r - delta, gr - delta, b - delta)
        g.rectangle(100 + (300 - 210) / 4 + i * ((300 - 210) / 4 + 70), 330,
                    100 + (300 - 210) / 4 + i * ((300 - 210) / 4 + 70) +
                    70, 400)


def turnlights():
    global window, light
    if light:
        g.brushColor('black')
    else:
        g.brushColor('gold')
    for i in range(3):
        g.deleteObject(window[i])
        window[i] = g.rectangle(100 + (300 - 210) / 4 + i * ((300 - 210) / 4 +
                                70), 330, 100 + (300 - 210) / 4 + i * ((300 -
                                210)/4 + 70) + 70, 400)
    light = not light 
    ghostrearm()
    return


def ghostrearm():  # перезагрузка призрака
    global head, body, eye1, eye2, x, y, blood, light
    g.deleteObject(head)
    g.deleteObject(eye1)
    g.deleteObject(body)
    g.deleteObject(eye2)
    g.deleteObject(blood)
    g.brushColor('lightgray')
    head = g.circle(x, y, 30)
    body = g.polygon([(x - 60, y + 50), (x - 30, y), (x + 30, y),
                     (x + 60, y + 50)])
    if light:
        g.brushColor('black')
    else:
        g.brushColor('red')
    eye1 = g.circle(x - 15, y - 10, 3)
    eye2 = g.circle(x + 15, y - 10, 3)
    if light:
        g.brushColor('lightgray')
        g.penColor('lightgray')
    else:
        g.brushColor('red')
        g.penColor('red')
    blood = g.polygon([(x + 5, y + 1),(x + 8, y + 1),(x + 8, y + 11),
                       (x + 5, y + 11)])
    g.penColor('black')
    return


def tobase():
    g.brushColor('black')
    g.penColor('black')


def updmoon():
    global b1, b2, moon
    g.deleteObject(moon)
    if b2 == 50 and b1 > -50:
        b1 -= 1
    elif b1 == -50 and b2 == 50:
        b1, b2 = b2, b1
    elif b1 == 50 and b2 < 50:
        b2 += 1
    
    moon = ellipse(430, 50, 50, b1, 50, b2, math.pi/2)
    
light = True
width = 600
height = 600
Dx = 0
Dy = 0
r = 20
gr = 55
b = 70
b1 = 50
b2 = 50
g.brushColor(r, gr, b)
g.rectangle (0, 0, width, height)

# Gradient
for i in range(height):
    g.penColor(r, gr, b)
    g.line(0, i, 600, i)
    if i % 10 == 0:
        r += 3
        gr += 1
        b += 2
g.brushColor(35, 25, 15)
g.rectangle(0, 400, 600, 600)

# Moon
g.brushColor('light yellow')
g.penColor('light yellow')
moon = ellipse(430, 50, 50, 50, 50, 50, math.pi/2)
g.brushColor(35, 60, 80)
g.penColor(g.brushColor())
tobase()

# Stars
for i in range(300):
    g.point(random.randint(0, 600), random.randint(0, 400), 'white')

# Clouds
for i in range(10):
    g.brushColor(115 + i, 100 + 2 * i, 145 + 2 * i)
    g.penColor(g.brushColor())
    l = random.randint(40, 120)
    ellips(random.randint(0, 500), random.randint(0, 350), l, l / 4)

# House
g.penColor('black')
g.brushColor(37, 30, 20)
g.rectangle(100, 200, 400, 500)
g.brushColor(100, 70, 50)
g.rectangle(100, 270, 400, 285)
for i in range(20):
    g.rectangle(100 + i * 15, 200, i * 15 + 110, 270)
g.rectangle(100, 200, 400, 205)
g.brushColor(40, 20, 0)
g.polygon([(70, 200), (320, 130), (430, 200)])
window = [0] * 3
for i in range(3):
    g.brushColor('gold')
    window[i] = g.rectangle(100 + (300 - 210) / 4 + i * ((300 - 210) / 4 + 70), 330, \
                            100 + (300 - 210) / 4 + i * ((300 - 210)/4 + 70)
                            + 70, 400)


# Ghost
head, body, eye1, eye2, blood = 0, 0, 0, 0, 0
x = 100
y = 430
ghostrearm()
g.onTimer(updmoon, 100)
g.onKey(keyPressed)
g.run()

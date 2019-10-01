from graph import *
from math import sin, cos, sqrt, asin


def keyPressed(event):
    global dx, dy, ex, ey
    if event.keycode == VK_LEFT:
        dx = -5; dy = 0
        ex = 0; ey =0
    elif event.keycode == VK_RIGHT:
        dx = 5; dy = 0
        ex = 0; ey =0
    elif event.keycode == VK_UP:
        dx = 0; dy = -5
        ex = 0; ey =0
    elif event.keycode == VK_DOWN:
        dx = 0; dy = 5
        ex = 0; ey =0
    elif event.keycode == VK_TAB:
        dx = 0; dy = 0
        ex = -5; ey = 0
    elif event.keycode == VK_DELETE:
        dx = 0; dy = 0
        ex = 5; ey = 0
    elif event.keycode == VK_SPACE:
        updatemouth()  # вызов сатаны (если разкомментишь)
        print("DUUUUUUUUCK")
        dx = 0; dy = 0
        ex = 0; ey = 0
    elif event.keycode == VK_BACK:
        # movelefthand()  разработке
        dx = 0; dy = 0
        ex = 0; ey = 0
    elif event.keycode == VK_ESCAPE:
        close()
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
        moveObjectBy(i, x, y)

        
def updateman():
    global dx, dy
    x = xCoord(body) + 75
    y = yCoord(body) + 200
    a = crosstheborder(x, y, 0, 15, 250, 500)
    dx = a[0]
    dy = a[1]
    moveobs([body, head, rhand, lhand, mouth, leye, reye], dx, dy)


def updateeyes():
    global ex, ey

    xl = xCoord(leye)
    xr = xl + 20
    ye = yCoord(leye)
    xh, yh = center(head)
    if xl < xh - 30:
        ex = 10
    elif xr > xh + 10:
        ex = -10
    moveObjectBy(leye, ex, ey)
    moveObjectBy(reye, ex, ey)


def updatemouth():
    global dm, mouth
    x, y = center(mouth)
    deleteObject(mouth)
    mouth = circle(x, y, dm + 1, "mouth")
    dm += 1
    if dm > 10:
        dm=4
    return
'''
don't move something here!

def movelefthand():
    global lhand, lh, rh, rhand
    print(lh)
    x=[0] * 4; y = [0] * 4
    for i in range(4):
        x[i], y[i] = lh[i][0], lh[i][1]
    l = sqrt( (x[1] - x[0])*(x[1] - x[0]) + (y[1] - y[0]) * (y[1] - y[0]) )
    a = asin( (y[0] - y[1]) / l )
    print(cos(a))
    a -= 0.1
    print(cos(a))
    xn = x[0] - l * cos(a)
    yn = y[0] - l * sin(a)
    x[1], y[1] = xn, yn
    l = sqrt( (x[3] - x[0])*(x[3] - x[0]) + (y[3] - y[0]) * (y[3] - y[0]) )
    a = asin( (y[3] - y[0]) / l )
    a += 0.1
    xn = x[0] + l * cos(a)
    yn = y[0] + l * sin(a)
    x[3], y[3] = xn, yn
    l = sqrt( (x[2] - x[0])*(x[2] - x[0]) + (y[2] - y[0]) * (y[2] - y[0]) )
    a = asin( (y[0] - y[2]) / l )
    a -= 0.1
    xn = x[0] - l * cos(a)
    yn = y[0] - l * sin(a)
    x[2], y[2] = xn, yn
    deleteObject(lhand)
    for i in range(4):
        lh[i] = (x[i],y[i])
    print(lh)
    lhand=polygon(lh)
'''
dx, dy, ex, ey = 0, 0, 0, 0


# floor
penColor(140, 129, 46)
brushColor(140, 129, 46)
polygon([(0, 15), (250, 500),(0, 500)])

# sea
penColor(36, 75, 72)
brushColor(36, 75, 72)
polygon([(15, 0), (273, 500), (500, 500), (500, 0)])

# background of fence
polygon([(10, 5), (5, 10), (258, 500), (265, 500)])

# fence
penColor("black")
penSize(5)
brushColor("brown")
polygon([(0, 15), (250, 500), (258, 500), (5, 10)])  # lower
polygon([(10, 5), (265, 500), (273, 500), (15, 0)])  # upper

# islands
penColor(230, 171, 67)
brushColor(230, 171, 67)
circle(250, 130, 100, "upis")  # upper
circle(400, 300, 60, "loveis")  # lower

# body
penSize(1)
penColor("black")
brushColor("black")
body=polygon([(125, 500), (125, 300), (200, 300), (200, 500)])

# head
brushColor(255, 168, 85)
penColor(255, 168, 85)
head=circle(163, 280, 30, "head")

# mouth
dm=4
penColor("black")
mouth=circle(163, 290, dm, "mouth")

# eyes
penSize(10)
leye=point(153, 270, "black")  # left
reye=point(173, 270, "black")  # right

# hands
penSize(1)
penColor("black")
brushColor(255, 168, 85)
lhand = polygon([ (140, 315), (130, 280), (140, 275), (150, 310)])  # left
lh = [ (140, 315), (130, 280), (140, 275), (150, 310) ]
rhand = polygon([(176, 310), (186, 315), (196, 280), (183, 275)])  # right
rh=[(176, 310), (186, 315), (196, 280), (183, 275)]

onKey(keyPressed)

run()






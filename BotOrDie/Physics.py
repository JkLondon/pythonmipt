def move(obj):
    dx = 1
    obj.x += dx
    obj.canv.delete(obj.id)
    obj.draw()
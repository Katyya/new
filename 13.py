from graph import *


def keyPressed(event):
    global dx, dy
    if event.keycode == VK_LEFT:"new"
        dx = -5
        dy = 0


    elif event.keycode == VK_RIGHT:
        dx = 5
        dy = 0

def update():

    if 380 >= xCoord(obj) :
        moveObjectBy(obj, dx, dy)
        close()

    if 380 <= xCoord(obj):
        moveObjectBy(obj, -5, 0)



brushColor("blue")
rectangle(0, 0, 400, 400)

x = 100
y = 100
dx = 0
dy = 0
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x + 20, y + 20)
onKey(keyPressed)
onTimer(update, 50)
onTimer(update1, 50)
run()

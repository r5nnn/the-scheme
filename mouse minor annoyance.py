import time, random, sys, math, threading
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def MouseX():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x


def MouseY():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.y
def move():
    o=-1
    p=1
    counter=0
    while (xx==1):
        if(counter>0):
            counter=counter-1
        x, y = MouseX(), MouseY()
        windll.user32.mouse_event(1, o, p, 0, 0)
        if((x==0 or x==1919) and counter==0):
            counter=5
            print("wingle")
            o*=-1
        elif((y==0 or y==1079) and counter==0):
            counter=5
            print("dingle")
            p*=-1
        time.sleep(0.01)
def shutdown():
    windll.user32.mouse_event(1, -7000, -7000, 0, 0)
    time.sleep(0.1)
    windll.user32.mouse_event(1, 0, 7000, 0, 0)
    time.sleep(0.1)
    windll.user32.mouse_event(6, 0, 0, 0, 0)
    time.sleep(0.1)
    windll.user32.mouse_event(1, 0, -100, 0, 0)
    time.sleep(0.1)
    windll.user32.mouse_event(6, 0, 0, 0, 0)
    time.sleep(0.1)
    windll.user32.mouse_event(1, 10, -30, 0, 0)
    time.sleep(0.1)
    windll.user32.mouse_event(6, 0, 0, 0, 0)
def angle(t, t1, ns, ew):
    tick=0
    tick1=0
    windll.user32.SetCursorPos(948, 886)
    time.sleep(1)
    while(xx==1):
        if (tick==int(t)):
            windll.user32.mouse_event(1, int(ns), 0, 0, 0)
            tick=0
        if(tick1==int(t1)):
            windll.user32.mouse_event(1, 0, int(ew), 0, 0)
            tick1=0
        tick +=1
        tick1 +=1
        time.sleep(0.001)
xx = 1
pullx = 0
pully = 0
choice = input(
    "\nwrite 1 for shutdown on border touch, 2 for mirror, 3 for black hole, 4 for bounce")
if (choice == "0"):
    print(MouseX(),MouseY())

elif (choice == "1"):
    move = input("should mouse move slightly for a minor annoyance?\n1 for move, 2 for no move")
    while (xx == 1):
        if (move == "1"):
            windll.user32.mouse_event(1, -1, 0, 0, 0)
        time.sleep(0.01)
        x, y = MouseX(), MouseY()
        print(x, y)
        if (x == 0 or y == 0 or x == 1919 or y == 1079):
            print("YO DIE NOW")
            shutdown()
elif (choice == "2"):
    while (xx == 1):
        x, y = MouseX(), MouseY()
        print(x, y)
        if (x == 0):
            windll.user32.SetCursorPos(1919, y)
            time.sleep(0.05)
        elif (x == 1919):
            windll.user32.SetCursorPos(0, y)
            time.sleep(0.05)
        elif (y == 0):
            windll.user32.SetCursorPos(x, 1079)
            time.sleep(0.05)
        elif (y == 1079):
            windll.user32.SetCursorPos(x, 0)
            time.sleep(0.05)
elif (choice == "3"):
    blackhole = input("where should the mouse gravitate towards (put your mouse in that place)")
    bx, by = MouseX(), MouseY()
    while (xx == 1):
        x, y = MouseX(), MouseY()
        distancex = x - bx
        distancey = y - by
        calc = distancex ** 2 + distancey ** 2
        z = int(math.sqrt(calc))
        pull = int(math.ceil(((2200 - z - 1000) / 200)))
        if (distancex > 0):
            pullx = -abs(pull ** 2)
        if (distancex < 0):
            pullx = abs(pull ** 2)
        if (distancey > 0):
            pully = -abs(pull ** 2)
        if (distancey < 0):
            pully = abs(pull ** 2)
        windll.user32.mouse_event(1, pullx, pully, 0, 0)
        print(pull)
        time.sleep(0.01)
elif (choice == "4"):
    move()
elif (choice =="5"):
    tinput=input("t")
    t1input=input("t1")
    ns=input("-1 for up, 1 for down")
    ew=input("-1 for left, 1 for right")
    angle(tinput, t1input, ns, ew)

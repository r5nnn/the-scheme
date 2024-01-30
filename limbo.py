import tkinter as tk
import random
import threading as th

root = tk.Tk()
root.geometry('%dx%d+%d+%d' % (500, 500, 100, 100))
root.title('welcome to limbo v1.1')
root.configure(background='Black')
tk.Label(root, text='Limbo', bg='Black', fg='White', font=('Courier New', 100)).pack(padx=30, pady=10)
tk.Label(root, text='by r5ne', bg='Black', fg='White', font=('Courier New', 20)).pack(padx=30, pady=0)
countdown = tk.Label(root, text='Loading...', bg='Black', fg='White', font=('Courier New', 15))
countdown.pack(padx=30, pady=90)
XY1 = 1000, 100
XY2 = 1000, 350
XY3 = 1000, 600
XY4 = 1225, 100
XY5 = 1225, 350
XY6 = 1225, 600


class box:
    def __init__(self, w, h, x, y, root):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.root = root
        self.topwin = tk.Toplevel(root)

    def generate(self, name, bg):
        self.topwin.title(name)
        self.topwin.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.topwin.resizable(False, False)
        self.topwin.configure(background=bg)
        self.topwin.protocol("WM_DELETE_WINDOW", on_closing)

    def colorc(self, color):
        self.topwin.configure(background=color)
        self.topwin.update()

    def move(self, xy):
        self.topwin.attributes('-topmost', True)
        print(self.topwin.winfo_y(), xy[1])
        if self.topwin.winfo_y() < xy[1]:
            while self.topwin.winfo_y() < xy[1]:
                self.topwin.geometry(
                    '%dx%d+%d+%d' % (self.w, self.h, self.x, self.topwin.winfo_y() + 1))
                self.topwin.update()
        else:
            while self.topwin.winfo_y() > xy[1]:
                self.topwin.geometry(
                    '%dx%d+%d+%d' % (self.w, self.h, self.x, self.topwin.winfo_y() - 1))
                self.topwin.update()
        if self.topwin.winfo_x() < xy[0]:
            while self.topwin.winfo_x() < xy[0]:
                self.topwin.geometry(
                    '%dx%d+%d+%d' % (self.w, self.h, self.topwin.winfo_y() + 1, self.y))
                self.topwin.update()
        else:
            while self.topwin.winfo_x() > xy[0]:
                self.topwin.geometry(
                    '%dx%d+%d+%d' % (self.w, self.h, self.topwin.winfo_y() - 1, self.y))
                self.topwin.update()


def on_closing():
    root.destroy()


def loading(windows, rand_index):
    for i in range(3, -1, -1):
        countdown.config(text='Shuffling in ' + str(i))
        root.after(1000)
        countdown.update()
    root.after(0, mix, windows, rand_index)


def mix(windows, rand_index):
    windows[rand_index + 1].colorc('#181818')
    x = th.Thread(target=windows[1].move(XY2))
    x1 = th.Thread(target=windows[2].move(XY1))
    x2 = th.Thread(target=windows[5].move(XY3))
    x3 = th.Thread(target=windows[3].move(XY5))
    x.start()
    x1.start()
    x2.start()
    x3.start()


def main():
    x1 = box(200, 200, XY1[0], XY1[1], root)
    x2 = box(200, 200, XY2[0], XY2[1], root)
    x3 = box(200, 200, XY3[0], XY3[1], root)
    x4 = box(200, 200, XY4[0], XY4[1], root)
    x5 = box(200, 200, XY5[0], XY5[1], root)
    x6 = box(200, 200, XY6[0], XY6[1], root)
    boxes = ['#181818', '#181818', '#181818', '#181818', '#181818', '#181818']
    rand_index = random.randint(0, len(boxes) - 1)
    boxes[rand_index] = "#b7ff81"
    windows = {
        1: x1,
        2: x2,
        3: x3,
        4: x4,
        5: x5,
        6: x6
    }
    x1.generate('1', boxes[0])
    x2.generate('2', boxes[1])
    x3.generate('3', boxes[2])
    x4.generate('4', boxes[3])
    x5.generate('5', boxes[4])
    x6.generate('6', boxes[5])
    countdown.config(text='Try to follow the green window.')
    root.after(1000, loading, windows, rand_index)
    root.mainloop()


main()

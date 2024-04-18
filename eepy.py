import tkinter as tk
from ctypes import windll
import random


class Main:
    def __init__(self):
        self.root = tk.Tk()

        self.screenx = windll.user32.GetSystemMetrics(0)
        self.screeny = windll.user32.GetSystemMetrics(1)
        self.width, self.height = 200, 200
        self.image = tk.PhotoImage(file='.\\screensaver.gif')

        self.root.geometry("200x200+0+0")
        self.root.title("screensaver")
        self.root.overrideredirect(1)  # noqa
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()
        self.canvas.create_image((self.width / 2, self.height / 2), image=self.image)
        self.canvas.create_text((self.width / 2, self.height / 2), text="he is eepy", fill='white',
                                font='tkDefaeultFont 18')
        self.dx, self.dy = 1, 1
        self.windows = []
        self.windows = [[Toplevel(self.root, self.image, random.randint(0, self.screenx-self.width),
                                  random.randint(0, self.screeny-self.height), self.width, self.height)] for i in range(5)]
        for i, x in enumerate(self.windows):
            self.windows[i] += [x[0].toplevel]
        self.windows += [[self, self.root]]

    def update(self):
        for obj, window in self.windows:
            x, y = window.winfo_rootx(), window.winfo_rooty()
            bx, by = x + obj.width, y + obj.height
            if 0 > x or bx > self.screenx:
                obj.dx *= -1
            if 0 > y or by > self.screeny:
                obj.dy *= -1
            window.geometry(f"+{x + obj.dx*2}+{y + obj.dy*2}")
            window.update()
        self.root.after(0, self.update)

    def main(self):
        self.update()
        self.root.mainloop()


class Toplevel:
    def __init__(self, root, img, x, y, width, height):
        self.screenx, self.screeny = x, y
        self.width, self.height = width, height
        self.toplevel = tk.Toplevel(root)
        self.canvas = tk.Canvas(self.toplevel)
        self.toplevel.overrideredirect(1)  # noqa
        self.toplevel.geometry(f"{width}x{height}+{x}+{y}")
        self.canvas.pack()
        self.canvas.create_image((width / 2, height / 2), image=img)
        self.canvas.create_text((width / 2, height / 2), text="he is eepy", fill='white',
                                font='tkDefaeultFont 18')
        self.dx, self.dy = 1, 1


_ = Main()
_.main()

import tkinter as tk
from ctypes import windll, Structure, c_long, byref

SCREENX = windll.user32.GetSystemMetrics(0)
SCREENY = windll.user32.GetSystemMetrics(1)


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


class Window:
    def __init__(self, x, y, w, h):
        self.root = tk.Tk()
        self.pt = POINT()

        self.width, self.height = w, h
        self.x, self.y = x, y
        self.root.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        self.root.overrideredirect(1)  # noqa

        self.canvas = tk.Canvas(self.root)
        self.canvas.bind('<Button-1>', lambda _: self.click())
        self.canvas.pack()
        self.clicked = False
        self.released = False
        self.up = 0
        self.total_up = -8
        self.g = 2
        self.cooldown = [0, 0]
        self.dx, self.dy = 0, 0

    def main(self):
        self.update()
        self.root.mainloop()

    def update(self):
        windll.user32.GetCursorPos(byref(self.pt))
        self.mouse_x, self.mouse_y = self.pt.x, self.pt.y
        self.updates()
        self.root.update()
        self.root.after(1, self.update)

    @run_once
    def click(self):
        self.canvas.bind('<Button-1>')
        self.clicked = True
        self.canvas.create_rectangle((self.canvas.winfo_width(), self.canvas.winfo_height() / 2 - 10, self.canvas.winfo_width() - 20, self.canvas.winfo_height() / 2 + 10), fill='red', tags='bar')
        self.canvas.bind('<Button-1>', lambda _: self.release())

    @run_once
    def release(self):
        self.released = True
        magnitude = round(self.canvas.winfo_width() - self.canvas.coords('bar')[0])
        self.dx = round(magnitude / 10)

    def updates(self):
        self.cooldown = [x+1 for x in self.cooldown]
        if self.up < 0 and self.cooldown[0] > 50:
            self.cooldown[0] = 0
            self.up += 1
        if not self.clicked:
            self.root.geometry(f"+{self.y}+{round(self.mouse_y - self.height / 2)}")
        if self.clicked and not self.released:
            strength = (self.root.winfo_rootx() + self.width) - self.mouse_x
            coords = self.canvas.coords('bar')
            self.canvas.coords('bar', self.canvas.winfo_width() - strength, coords[1], coords[2], coords[3])
        if self.released:
            self.dy = self.g + self.up
            if self.root.winfo_rooty() + self.dy + self.height >= SCREENY:
                self.up = self.total_up
                self.total_up += 1 if self.total_up + 1 <= 0 else 0
                if self.total_up <= self.g:
                    self.dy = 0
            if self.root.winfo_rootx() + self.width + self.dx >= SCREENX or self.root.winfo_rootx() < 0:
                self.dx *= -1
            print(self.cooldown[1], self.dx)
            if self.cooldown[1] > 10 and self.root.winfo_rootx() <= 0:
                self.cooldown[1] = 0
                if self.dx > 0:
                    if self.dx - 1 >= 0:
                        self.dx -= 1
                    else:
                        self.dx = 0
                elif self.dx < 0:
                    if self.dx + 1 < 0:
                        self.dx += 1
                    else:
                        self.dx = 0
            self.root.geometry(f"+{self.root.winfo_rootx() + self.dx}+{self.root.winfo_rooty() + self.dy}")


window = Window(round(SCREENX / 2 - 200 / 2), round(SCREENY / 2 - 200 / 2), 200, 200)
window.main()

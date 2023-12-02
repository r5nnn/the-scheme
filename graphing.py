import tkinter as tk
from math import *
from colorsys import hsv_to_rgb


class PGrid():
    def __init__(self, width, height, delay=10):
        self.root = tk.Tk()
        self.width = width
        self.height = height
        self.delay = delay
        self.ox, self.oy = width // 2, height // 2
        self.photo = tk.PhotoImage(width=width, height=height)
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.pointers = []
        self.paused = True
        self.pause_btn = tk.Button(self.root, text='Run', command=self.pause_toggle)
        self.pause_btn.pack()

    def pause_toggle(self):
        self.paused = not self.paused
        text = 'Run' if self.paused else 'Pause'
        self.pause_btn.config(text=text)
        if not self.paused:
            self.update()

    def pointer(self, x, y, color, filled=False):
        x += self.ox
        y += self.oy
        bbox = (x - bodyrad, y - bodyrad, x + bodyrad, y + bodyrad)
        fillcolor = color if filled else ''
        return self.canvas.create_oval(bbox, fill=fillcolor, outline=color)

    def add_pointer(self, pointer):
        self.pointers.append(pointer)

    def update(self):
        if self.paused:
            return
        for pointer in self.pointers:
            x = int(0.5 + self.ox + body.x)
            y = int(0.5 + self.oy + body.y)
            if 0 <= x < self.width and 0 <= y < self.height:
                self.photo.put(body.color, (x, y))
            self.canvas.move(body.disc, body.dx, body.dy)
            body.update()
        self.root.after(self.delay, self.update)

    def start(self):
        self.root.mainloop()


class Graph():
    def __init__(self, pgrid, x, y)


width = height = 600
PGrid = pgrid(width, height)
PGrid.start()
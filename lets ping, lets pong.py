import random
import time
from tkinter import *


# class to make multiple instances of the paddle objects
class Paddle:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag):
        self.can, self.color, self.tag = can, color, tag
        self.start_x, self.start_y, self.size_x, self.size_y = start_x, start_y, size_x, size_y
        # paddle created
        self.paddle = self.can.create_rectangle((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                                tag=self.tag)
        self.yspeed = 0
        self.can.bind_all('<KeyPress-Up>', self.move_up)
        self.can.bind_all('<KeyPress-Down>', self.move_down)

    def move(self):
        self.can.move(self.paddle, 0, self.yspeed)
        pos = self.can.coords(self.paddle)
        if pos[1] <= 0:
            self.yspeed = 0
        if pos[3] >= 700:
            self.yspeed = 0

    def move_up(self, evt):
        self.yspeed = -2

    def move_down(self, evt):
        self.yspeed = 2

# class to make multiple instances of the ball objects
class Ball:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag, pad):
        self.can, self.color, self.tag, self.pad = can, color, tag, pad
        self.start_x, self.start_y, self.size_x, self.size_y = start_x, start_y, size_x, size_y
        # ball created
        self.ball = self.can.create_oval((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                         tag=self.tag)
        self.xspeed = 3
        self.yspeed = random.randrange(-3,3)

    def move(self):
        self.can.move(self.tag, self.xspeed, self.yspeed)
        pos = self.can.coords(self.tag)
        print(pos)
        if pos[1] <= 0:
            self.yspeed *=-1
        if pos[3] >= 700:
            self.yspeed *=-1
        if pos[0] <= 0:
            self.xspeed *=-1
        if pos[2] >= 1200:
            self.xspeed *=-1
        if self.hit_paddle(pos) == True:
            self.yspeed = random.randrange(-3,3)
            self.xspeed *=-1

    def hit_paddle(self, pos):
        paddle_pos = self.can.coords(self.pad.tag)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


# paddle movement
'''def callback(event, pad):
    constant_width = getattr(pad, 'start_x')
    w1 = getattr(pad, 'size_x') + getattr(pad, 'start_x')
    move_height = getattr(pad, 'size_y')
    x_event, y_event = event.x, event.y
    canvas.coords('pad', constant_width, y_event - move_height / 2, w1, y_event + move_height / 2)'''

root = Tk()  # main window
ws = root.winfo_screenwidth()  # width of root
hs = root.winfo_screenheight()  # height of root

# calculate x and y coordinates for the Tk root window
w = 1200  # width for the Tk root
h = 700  # height for the Tk root
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("ping pong")

# create canvas
canvas = Canvas(root, width=w, height=h)
canvas.pack()

# making paddles
paddle1 = Paddle(canvas, 10, 10, 10, 100, 'blue', 'pad')

# making ball
ball1 = Ball(canvas, 20, 20, 20, 20, 'yellow', 'ball', paddle1)

while True:
    ball1.move()
    paddle1.move()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

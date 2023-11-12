import random
import time
from tkinter import *


# class to make multiple instances of the paddle objects
class Paddle:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag, keyup, keydown):
        self.can, self.color, self.tag = can, color, tag
        self.start_x, self.start_y, self.size_x, self.size_y = start_x, start_y, size_x, size_y
        self.keyup, self.keydown = keyup, keydown
        self.paddle = self.can.create_rectangle((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                                tag=self.tag)  # paddle created
        self.yspeed = 0  # paddle only moves in y direction
        self.can.bind_all(self.keyup, self.move_up)  # bind specified keys to movement
        self.can.bind_all(self.keydown, self.move_down)

    def move(self):  # paddle boundary check
        self.can.move(self.paddle, 0, self.yspeed)
        pos = self.can.coords(self.paddle)
        if pos[1] <= 0:  # y
            self.yspeed = 0
        if pos[3] >= 700:  # y
            self.yspeed = 0

    def move_up(self, event):  # movements and paddle speed
        self.yspeed = -2

    def move_down(self, event):
        self.yspeed = 2


# class to make multiple instances of the ball objects
class Ball:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag, pad):
        self.can, self.color, self.tag, self.pad = can, color, tag, pad
        self.start_x, self.start_y, self.size_x, self.size_y = start_x, start_y, size_x, size_y
        self.ball = self.can.create_oval((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                         tag=self.tag)  # ball created
        self.xspeed, self.yspeed = 3, random.randrange(-3, 3)  # initial ball speed in x is randomised

    def move(self):  # ball paddle/wall bouncing method
        self.can.move(self.tag, self.xspeed, self.yspeed)
        pos = self.can.coords(self.tag)  # position of paddle
        print(pos)
        if pos[1] <= 0:  # top wall
            self.yspeed *= -1
        if pos[3] >= 700:  # bottom wall
            self.yspeed *= -1
        if pos[0] <= 0:  # left wall
            self.xspeed *= 1
        if pos[2] >= 1200:  # right wall
            self.xspeed *= -1
        if self.hit_paddle(pos):
            self.yspeed = random.randrange(-3, 3)  # randomise bounce of paddle
            self.xspeed *= -1

    def hit_paddle(self, pos):  # method to detect ball contact with paddle
        paddle_pos = self.can.coords(self.pad.tag)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False


# old mouse paddle movement
'''def callback(event, pad):
    constant_width = getattr(pad, 'start_x')
    w1 = getattr(pad, 'size_x') + getattr(pad, 'start_x')
    move_height = getattr(pad, 'size_y')
    x_event, y_event = event.x, event.y
    canvas.coords('pad', constant_width, y_event - move_height / 2, w1, y_event + move_height / 2)'''

root = Tk()  # main window
ws = root.winfo_screenwidth()  # screen width
hs = root.winfo_screenheight()  # screen height

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
paddle1 = Paddle(canvas, 10, 10, 10, 100, 'blue', 'pad', '<KeyPress-Up>', '<KeyPress-Down>')

# making ball
ball1 = Ball(canvas, 20, 20, 20, 20, 'yellow', 'ball', paddle1)

# mainloop
while True:
    ball1.move()
    paddle1.move()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

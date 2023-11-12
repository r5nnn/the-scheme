import random
import time, sys
import datetime
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
        if pos[1] == 0:
            self.yspeed = 0
        elif pos[1] <= 0:  # y top
            self.yspeed = 1
        if pos[3] == 700:
            self.yspeed = 0
        elif pos[3] >= 700:  # y bottom
            self.yspeed = -1

    def move_up(self, event):  # movements and paddle speed
        self.yspeed = -2

    def move_down(self, event):
        self.yspeed = 2


# class to make multiple instances of the ball objects
class Ball:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag, pad, pad1):
        self.can, self.color, self.tag, self.pad, self.pad1 = can, color, tag, pad, pad1
        self.start_x, self.start_y, self.size_x, self.size_y = start_x, start_y, size_x, size_y
        self.ball = self.can.create_oval((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                         tag=self.tag)  # ball created
        self.xspeed, self.yspeed = 3, random.randrange(-3, 3)  # initial ball speed in x is randomised
        self.live = True

    def move(self):  # ball paddle/wall bouncing method
        global blue, red
        self.can.move(self.tag, self.xspeed, self.yspeed)
        pos = self.can.coords(self.tag)  # position of paddle
        if pos[1] <= 0:  # top wall
            self.yspeed *= -1
        if pos[3] >= 700:  # bottom wall
            self.yspeed *= -1
        if pos[0] <= 0:  # left wall
            score[1]+=1
            self.live = False
        if pos[2] >= 1200:  # right wall
            score[0]+=1
            self.live = False
        if self.hit_paddle(pos) == 'inside':
            print('clip')  # i want to fix ball clipping into paddle
        if self.hit_paddle(pos):
            self.yspeed = random.randrange(-3, 3)  # randomise bounce of paddle
            self.xspeed *= -1
        if self.hit_paddle1(pos) == 'inside':
            print('clip')  # i want to fix ball clipping into paddle
        if self.hit_paddle1(pos):
            self.yspeed = random.randrange(-3, 3)  # randomise bounce of paddle1
            self.xspeed *= -1

    def hit_paddle(self, pos):  # method to detect ball contact with paddle
        # 0 = leftmost x, 2 = rightmost x
        # 1 = topmost y, 3 = bottommost y
        paddle_pos = self.can.coords(self.pad.tag)
        if paddle_pos[2] >= pos[0] >= paddle_pos[0]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return 'inside'
        elif pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_paddle1(self, pos):  # method to detect ball contact with paddle1
        paddle_pos1 = self.can.coords(self.pad1.tag)
        if paddle_pos1[0] >= pos[2] >= paddle_pos1[2]:
            if paddle_pos1[1] <= pos[3] <= paddle_pos1[3]:
                return True
        if pos[2] >= paddle_pos1[0] and pos[0] <= paddle_pos1[2]:
            if paddle_pos1[1] <= pos[3] <= paddle_pos1[3]:
                return True
        return False

class StatsBox:
    def __init__(self, can, width, height, x, y):
        self.width, height, x, y = width, height, x, y
        self.can = can
        self.can.create_window(width, height)
    def Text(self, can, size_x, size_y, string, font, tag):
        self.size_x, size_y = size_x, size_y
        self.can, string, font, tag = can, string, font, tag
        self.can.create_text(size_x, size_y, font=font, tag=tag, text=string)
# old mouse paddle movement
'''def callback(event, pad):
    constant_width = getattr(pad, 'start_x')
    w1 = getattr(pad, 'size_x') + getattr(pad, 'start_x')
    move_height = getattr(pad, 'size_y')
    x_event, y_event = event.x, event.y
    canvas.coords('pad', constant_width, y_event - move_height / 2, w1, y_event + move_height / 2)'''


def main(score):
    global time, root
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

    paddle1 = Paddle(canvas, 10, 10, 10, 100, 'blue', 'pad', '<KeyPress-Up>', '<KeyPress-Down>')  # making paddles
    paddle2 = Paddle(canvas, 1180, 10, 10, 100, 'red', 'pad1', '<KeyPress-w>', '<KeyPress-s>')
    ball1 = Ball(canvas, 20, 20, 20, 20, 'yellow', 'ball', paddle1, paddle2)  # making ball

    # all the text
    statsbox = StatsBox(canvas, 50, 50, x-100, y-100)
    scores = statsbox.Text(canvas, 600, 10, f'Blue - %(blue)s Red - %(red)s' % {'blue': score[0], 'red': score[1]}, 'Helvetica', 'score')
    # mainloop
    while ball1.live:
        ball1.move()
        paddle1.move()
        paddle2.move()
        root.update_idletasks()
        root.update()
        time.sleep(0.01)
    root.destroy()
    score1 = score
    print(score1)
    main(score1)

score = [0,0]
if __name__ == "__main__":
    main(score)

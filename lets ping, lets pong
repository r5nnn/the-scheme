from tkinter import *


# class to make multiple instances of the paddle objects
class Paddle:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag):
        self.can = can
        self.color = color
        self.tag = tag
        self.start_x = start_x
        self.start_y = start_y
        self.size_x = size_x
        self.size_y = size_y
        # paddle created
        self.paddle = self.can.create_rectangle((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                                tag=self.tag)


# class to make multiple instances of the ball objects
class Ball:
    def __init__(self, can, start_x, start_y, size_x, size_y, color, tag):
        self.can = can
        self.color = color
        self.tag = tag
        self.start_x = start_x
        self.start_y = start_y
        self.size_x = size_x
        self.size_y = size_y
        # ball created
        self.ball = self.can.create_oval((start_x, start_y, start_x + size_x, start_y + size_y), fill=color,
                                         tag=self.tag)


# class to make multiple instances of the text objects
class Text:
    def __init__(self, can, tx, ty, text, fill, font, tag):
        self.can = can
        self.text = text
        self.can.create_text(tx, ty, text=text, fill=fill, font=font, tag=tag)


# class to make key down and key up detection easier
class KeyRepeater(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current = {}
        self.functions = {}
        self.bind("<KeyPress>", self.keydown, add="+")
        self.bind("<KeyRelease>", self.keyup, add="+")
        self.key_loop()

    def key_loop(self):
        for function in self.current.values():
            if function:
                function()
        self.after(40, self.key_loop)  # set repeat time here.

    def key_bind(self, key, function):
        self.functions[key] = function

    def keydown(self, event=None):
        if event.keysym in self.functions:
            self.current[event.keysym] = self.functions.get(event.keysym)

    def keyup(self, event=None):
        self.current.pop(event.keysym, None)


def ballmove():
    global ball_x_speed, ball_y_speed
    canvas.move('ball', ball_x_speed, ball_y_speed)
    ball_coordinates = canvas.coords('ball')
    pad_coordinates = canvas.coords('pad')
    epad_coordinates = canvas.coords('epad')
    # paddle1 hitbox detection
    if pad_coordinates[1] <= ball_coordinates[1] <= pad_coordinates[3] and ball_coordinates[0] <= pad_coordinates[2]:
        ball_x_speed = -ball_x_speed
    # paddle2 hitbox detection
    if epad_coordinates[1] <= ball_coordinates[3] <= epad_coordinates[3] and ball_coordinates[2] >= epad_coordinates[0]:
        ball_x_speed = -ball_x_speed
    # general wall collosion detection
    if ball_coordinates[3] >= 700 or ball_coordinates[1] <= 0:
        ball_y_speed = -ball_y_speed
    root.after(10, ballmove)


# paddle movement
def callback(event, pad):
    constant_width = getattr(pad, 'start_x')
    w1 = getattr(pad, 'size_x') + getattr(pad, 'start_x')
    move_height = getattr(pad, 'size_y')
    x_event, y_event = event.x, event.y
    canvas.coords('pad', constant_width, y_event - move_height / 2, w1, y_event + move_height / 2)


def controls(event, pad):
    if event.char == 'w':
        canvas.move(pad, 0, -10)
    elif event.char == 's':
        canvas.move(pad, 0, 10)
    if event.keysym == 'Delete':
        root.destroy()


ball_x_speed, ball_y_speed = 2, 3  # defining speed and bounce function
epad_y_speed = 10  # speed of enemy paddle
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
root.overrideredirect(True)

# create canvas
canvas = Canvas(root, width=w, height=h)
canvas.pack()

# making paddles
paddle1 = Paddle(canvas, 10, 10, 10, 100, 'blue', 'pad')
canvas.bind('<Motion>', lambda event: callback(event, paddle1))  # binding paddle to motion in y
paddle2 = Paddle(canvas, 1190, 10, 10, 100, 'red', 'epad')
bind = KeyRepeater()
bind.key_bind('<KeyPress>', lambda event1: controls(event1, 'epad'))  # binding paddle to motion in y

# adding stats
time1 = Text(canvas, 10, 10, 'dongo', 'black', 'Helvetica', 'time')

# making ball
ball1 = Ball(canvas, 20, 20, 20, 20, 'yellow', 'ball')
ballmove()

# initialise
root.mainloop()

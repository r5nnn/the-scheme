from tkinter import *
import operator


class myButton(Button):
    def __init__(self, text, row, col, command, color=None, **kwargs):
        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self.color = color
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self.grid(row=self.row, column=self.column)


class myLabel(Label):
    def __init__(self, root, Root, text, row, col, Rootheight):
        self.text = text
        self.row = row
        self.column = col
        self.root = root
        self.Root = Root
        self.Rootheight = Rootheight
        super().__init__(root)
        self['text'] = self.text
        self.grid(row=self.row, column=self.column)
        self.bind("<Configure>", self.move)

    def move(self, event=None):
        x = self.Root.winfo_x()
        y = self.Root.winfo_y() - self.Rootheight - 30
        self.root.geometry("+%d+%d" % (x, y))
        self.root.after(1, self.move)

def listint(numList):
    s = ''.join(map(str, numList))
    return int(s)

def intlist(integer):
    s = [int(i) for i in str(integer)]
    return s

def btnprint(lab, num):
    global output
    if output[0] == '0':
        output[0] = num
    else:
        output.append(num)
    lab.config(text=output)


def btncmd(lab, method):
    global output
    if method == 'exe':
        if '+' in output:
            op = '+'
            real = '+'
        elif '×' in output:
            op = '×'
            real = '*'
        elif '-' in output:
            op = '-'
            real = '-'
        ind = output.index(op)
        num1=listint(output[:ind])
        num2=listint(output[ind+1:])
        output=intlist(eval(str(num1) + real + str(num2)))
        
    elif method == 'ac':
        output = ['0']
    lab.config(text=output)


def main():
    global display
    # CALCULATOR KEYBOARD
    root = Tk()
    # calculate x and y coordinates for the Tk root
    ws = root.winfo_screenwidth()  # screen width
    hs = root.winfo_screenheight()  # screen height
    w = 500  # width for the Tk root
    h = 500  # height for the Tk root
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.title("Test Button Class")
    root.geometry('%dx%d+%d+%d' % (w, h, x, y + 100))
    root.resizable(False, False)

    # CALCULATOR DISPLAY
    display = Toplevel()
    w = 500  # width for the Tk display
    h = 200  # height for the Tk display
    display.geometry('%dx%d+%d+%d' % (w, h, x, y - 130))
    ans = myLabel(display, root, output, 0, 0, h)
    display.resizable(False, False)

    # CALCULATOR BUTTONS
    d = {}
    n = 0
    for i in range(0, 10):
        d["num{0}".format(i)] = myButton(i, i, n, lambda i=i: btnprint(ans, i), 'light grey')

    add = myButton("Add", 0, 0, lambda: btnprint(ans, '+'), 'light grey')
    sub = myButton("Subtract", 0, 1, lambda: btnprint(ans, '-'), 'light grey')
    mult = myButton("Multiply", 0, 2, lambda: btnprint(ans, '×'), 'light grey')
    exe = myButton("Execute", 0, 3, lambda: btncmd(ans, 'exe'), 'light green')
    ac = myButton("AC", 0, 4, lambda: btncmd(ans, 'ac'), 'pink')

    root.mainloop()


output = ['0']

if __name__ == "__main__":
    main()

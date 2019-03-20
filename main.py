from tkinter import *
from random import randint
root = Tk()
c_width = 800
c_height = 600
c = Canvas(root, width=c_width, height=c_height, bg='gray')
snake = c.create_rectangle(0, 0, 20, 20, fill='white')
scale = 20
x_dir = scale
y_dir = 0
g_speed = 100

class Food:
    def __init__(self):
        self.x = randint(0, c_width/scale)*scale
        self.y = randint(0, c_height/scale)*scale
        self.pos = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='red')
    def destroy(self):
        c.delete(self.pos)
        pass
f = Food()

def launch_snake():
    c.move(snake, x_dir, y_dir)
    root.after(g_speed, launch_snake)

def move_r(event):
    global x_dir, y_dir
    x_dir = scale
    y_dir = 0

def move_l(event):
    global x_dir, y_dir
    x_dir = -scale
    y_dir = 0

def move_u(event):
    global x_dir, y_dir
    x_dir = 0
    y_dir = -scale

def move_d(event):
    global x_dir, y_dir
    x_dir = 0
    y_dir = scale


def is_food_eaten():
    global f
    if c.coords(snake) == c.coords(f.pos):
        f.destroy()
        f = Food()
    root.after(g_speed, is_food_eaten)


launch_snake()
is_food_eaten()


root.bind('<Right>', move_r)
root.bind('<Left>', move_l)
root.bind('<Up>', move_u)
root.bind('<Down>', move_d)


c.pack()
root.mainloop()
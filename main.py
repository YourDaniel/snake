from tkinter import *
from random import randint
root = Tk()
c_width = 800
c_height = 600
c = Canvas(root, width=c_width, height=c_height, bg='gray')
scale = 20
x_dir = scale
y_dir = 0
g_speed = 100
score = 0
dir = ''
input_stack = []


class Wormhole:
    def __init__(self):
        self.x1 = randint(0, c_width/scale-1)*scale
        self.y1 = randint(0, c_height/scale-1)*scale
        self.hole_1 = c.create_rectangle(self.x1, self.y1, self.x1+scale, self.y1+scale, fill='black', width=0)
        self.x2 = randint(0, c_width/scale-1)*scale
        self.y2 = randint(0, c_height/scale-1)*scale
        self.hole_2 = c.create_rectangle(self.x2, self.y2, self.x2+scale, self.y2+scale, fill='black', width=0)


class Food:
    def __init__(self):
        self.x = randint(0, c_width/scale-1)*scale
        self.y = randint(0, c_height/scale-1)*scale
        self.pos = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='red', width=0)

    def destroy(self):
        c.delete(self.pos)
        pass

    def create_new(self):
        self.x = randint(0, c_width/scale-1)*scale
        self.y = randint(0, c_height/scale-1)*scale
        self.pos = c.create_rectangle(self.x, self.y, self.x + scale, self.y + scale, fill='red', width=0)


class Snake:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.head = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='white', width=0)
        self.length = 0
        self.body = []

    def kill(self):
        c.delete(self.head)
        self.length = 0
        for i in range(len(self.body)):
            c.delete(self.body[i])
        self.body = []
        self.head = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='white', width=0)

    def draw_body(self):
        pass


snake = Snake()
f = Food()
wormhole = Wormhole()

def kill_snake():
    global score
    score = 0
    snake.kill()
    f.destroy()
    f.create_new()


def launch_snake():
    global x_dir, y_dir
    if snake.length > 0:
        snake.body.insert(0, c.create_rectangle(c.coords(snake.head)[0], c.coords(snake.head)[1], c.coords(snake.head)[0] + scale, c.coords(snake.head)[1] + scale, fill='white', width=0))
        if len(snake.body) > snake.length:
            c.delete(snake.body[-1])
            del snake.body[-1]
    valid_input = False

    if c.coords(snake.head) == c.coords(wormhole.hole_1):
        c.coords(snake.head, c.coords(wormhole.hole_2)[0], c.coords(wormhole.hole_2)[1], c.coords(wormhole.hole_2)[2], c.coords(wormhole.hole_2)[3])
    else:
        for i in range(len(input_stack)):
            if x_dir != -input_stack[i][0] and y_dir != -input_stack[i][1]:
                x_dir = input_stack[i][0]
                y_dir = input_stack[i][1]
                c.move(snake.head, input_stack[i][0], input_stack[i][1])
                input_stack.clear()
                valid_input = True
                break
        if not valid_input:
            c.move(snake.head, x_dir, y_dir)



    if c.coords(snake.head)[2] > c_width or c.coords(snake.head)[0] < 0 or c.coords(snake.head)[1] < 0 or c.coords(snake.head)[3] > c_height:
        kill_snake()
    for i in range(len(snake.body)):
        if c.coords(snake.body[i]) == c.coords(snake.head):
            kill_snake()
    root.after(g_speed, launch_snake)


def move_r(event):
    input_stack.insert(0, (scale, 0))
def move_l(event):
    input_stack.insert(0, (-scale, 0))
def move_u(event):
    input_stack.insert(0, (0, -scale))
def move_d(event):
    input_stack.insert(0, (0, scale))


def is_food_eaten():
    global f, score
    if c.coords(snake.head) == c.coords(f.pos):
        snake.length += 1
        f.destroy()
        f.create_new()
        score += 10
    root.after(g_speed, is_food_eaten)


def update_title():
    root.title('Snake. Score: {} {}'.format(score, len(snake.body)))
    root.after(g_speed, update_title)


launch_snake()
is_food_eaten()
update_title()

root.bind('<Right>', move_r)
root.bind('<Left>', move_l)
root.bind('<Up>', move_u)
root.bind('<Down>', move_d)


c.pack()
root.mainloop()
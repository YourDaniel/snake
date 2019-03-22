from tkinter import *
from random import randint
import menu
root = Tk()
c_width = 800
c_height = 600
c = Canvas(root, width=c_width, height=c_height, bg='gray')
scale = 20
g_speed = 100
score = 0
input_stack = []


class Wormhole:
    def __init__(self):
        self.x1 = randint(0, c_width/scale-1)*scale
        self.y1 = randint(0, c_height/scale-1)*scale
        self.hole_1 = c.create_rectangle(self.x1, self.y1, self.x1+scale, self.y1+scale, fill='black', width=0)
        self.x2 = randint(0, c_width/scale-1)*scale
        self.y2 = randint(0, c_height/scale-1)*scale
        self.hole_2 = c.create_rectangle(self.x2, self.y2, self.x2+scale, self.y2+scale, fill='black', width=0)
        self.wormhole_needed = False

    def destroy(self):
        c.delete(self.hole_1)
        c.delete(self.hole_2)

    def create_new(self):
        self.destroy()
        self.__init__()



class Food:
    def __init__(self):
        self.x = randint(0, c_width/scale-1)*scale
        self.y = randint(0, c_height/scale-1)*scale
        self.pos = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='red', width=0)

    def destroy(self):
        c.delete(self.pos)

    def create_new(self):
        self.x = randint(0, c_width/scale-1)*scale
        self.y = randint(0, c_height/scale-1)*scale
        self.pos = c.create_rectangle(self.x, self.y, self.x + scale, self.y + scale, fill='red', width=0)


class Snake:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.x_dir = scale
        self.y_dir = 0
        self.head = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='white', width=0)
        self.length = 3
        self.body = []

    def kill(self):
        c.delete(self.head)
        self.length = 3
        for i in range(len(self.body)):
            c.delete(self.body[i])
        self.body = []
        self.head = c.create_rectangle(self.x, self.y, self.x+scale, self.y+scale, fill='white', width=0)

    def launch_snake(self):
        if self.length > 0:
            self.body.insert(0, c.create_rectangle(c.coords(self.head)[0], c.coords(self.head)[1],
                                                    c.coords(self.head)[0] + scale, c.coords(self.head)[1] + scale,
                                                    fill='white', width=0))
            if len(self.body) > self.length:
                c.delete(self.body[-1])
                del self.body[-1]
        valid_input = False

        if c.coords(self.head) == c.coords(wh.hole_1):
            c.coords(self.head, c.coords(wh.hole_2)[0], c.coords(wh.hole_2)[1],
                     c.coords(wh.hole_2)[2], c.coords(wh.hole_2)[3])
        else:
            for i in range(len(input_stack)):
                if self.x_dir != -input_stack[i][0] and self.y_dir != -input_stack[i][1]:
                    self.x_dir = input_stack[i][0]
                    self.y_dir = input_stack[i][1]
                    c.move(self.head, input_stack[i][0], input_stack[i][1])
                    input_stack.clear()
                    valid_input = True
                    break
            if not valid_input:
                c.move(self.head, self.x_dir, self.y_dir)

        if c.coords(self.head)[2] > c_width or c.coords(self.head)[0] < 0 or c.coords(self.head)[1] < 0 or \
                c.coords(self.head)[3] > c_height:
            self.kill()
        for i in range(len(self.body)):
            if c.coords(self.body[i]) == c.coords(self.head):
                self.kill()
                break
        root.after(g_speed, self.launch_snake)


snake = Snake()
f = Food()
wh = Wormhole()


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
        wh.wormhole_needed = True
    if score % 100 == 0 and score > 0 and wh.wormhole_needed:
        wh.create_new()
        wh.wormhole_needed = False
    root.after(g_speed, is_food_eaten)


def update_title():
    root.title('Snake. Score: {}'.format(score))
    root.after(g_speed, update_title)


snake.launch_snake()
is_food_eaten()
update_title()

root.bind('<Right>', move_r)
root.bind('<Left>', move_l)
root.bind('<Up>', move_u)
root.bind('<Down>', move_d)


c.pack()
root.mainloop()

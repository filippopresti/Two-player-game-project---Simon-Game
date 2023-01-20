import turtle
from random import randint

t = turtle.Turtle()

up = 0
down = 1
left = 0
right = 1
steps = int(input('Enter number of steps: '))
t.speed(10)


for i in range(0, steps):
    up_down_random = randint(0, 1)
    left_right_random = randint(0, 1)
    if up_down_random == up:
        t.forward(15)
    else:
        t.backward(15)
    if left_right_random == left:
        t.left(90)
    else:
        t.right(90)
turtle.done()

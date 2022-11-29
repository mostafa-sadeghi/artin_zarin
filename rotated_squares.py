import turtle
import random

screen = turtle.Screen()
COLORS = ('red', 'green', 'blue', 'gray')
t = turtle.Pen()
t.pensize(4)
for j in range(12):
    t.pencolor(COLORS[j])
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.left(30)


screen.exitonclick()

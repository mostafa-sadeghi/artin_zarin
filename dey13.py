import turtle


s = turtle.Screen()
s.setup(620, 620)
s.bgcolor('black')
# s.bgpic('mario.png')
# s.register_shape("my_shape", ((10, 0), (10, 10), (-10, 10), (-10, 0)))
# s.register_shape("strawberry.gif")

p = turtle.Pen()
# p.shape('classic')  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# p.shape('my_shape')
# p.shape("strawberry.gif")
# p.shapesize(3, 3, 3)

p.penup()
p.pensize(4)
p.hideturtle()

# p.setpos(100, 100)
p.pendown()
p.speed('normal')
# for i in range(3):
#     p.forward(100)
#     p.left(120)
# for i in range(4):
#     p.forward(100)
#     p.left(90)
# for i in range(5):
#     p.forward(100)
#     p.left(72)
# for i in range(6):
#     p.forward(100)
#     p.left(60)

# draw star
# COLORS = ['green', 'blue', 'silver', 'red', 'cyan']
# p.pensize(4)
# p.penup()
# p.setpos(-90, 30)

# p.pendown()
# for i in range(5):
#     p.pencolor(COLORS[i])
#     p.forward(200)
#     p.rt(144)

# p.penup()
# p.speed('fastest')
# p.setposition(80, -140)
# p.pencolor("silver")
# p.pendown()
# p.write("Hello every body!", font=("", 25, "bold"))
# p.hideturtle()
# animation clock
p.pencolor('red')
for i in range(12):
    p.penup()
    p.setheading(-30 * i + 60)
    p.forward(150)
    p.pendown()
    p.forward(25)
    p.penup()
    p.forward(25)
    p.write(i+1, align="center", font=15)
    p.home()
p.setpos(0, -250)
p.pendown()
p.circle(250)
s.exitonclick()

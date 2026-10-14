from turtle import *
t = Turtle()
t.screen.setup(800, 800)
t.hideturtle()
t.speed(0)

A = 14
B = 6
X = 1.5
sx = 250 / X
sy = 300 / (A * X ** B)

t.pensize(2)
t.up()
t.goto(-350, 0)
t.down()
t.goto(350, 0)
t.up()
t.goto(0, -50)
t.down()
t.goto(0, 350)

for i in range(-3, 4):
    if i != 0:
        x = i * 0.5
        t.up()
        t.goto(x * sx, -5)
        t.down()
        t.goto(x * sx, 5)
        t.up()
        t.goto(x * sx, -25)
        t.write(str(x), align="center", font=("Arial", 10, "normal"))

for i in range(1, 5):
    y = A * X ** B * i / 4
    t.up()
    t.goto(-5, y * sy)
    t.down()
    t.goto(5, y * sy)
    t.up()
    t.goto(-10, y * sy - 5)
    t.write(str(round(y, 1)), align="right", font=("Arial", 10, "normal"))

t.up()
t.goto(340, -25)
t.write("x", font=("Arial", 12, "bold"))
t.goto(10, 340)
t.write("y", font=("Arial", 12, "bold"))
t.goto(-300, 340)
t.write("y = 14 * x^6", font=("Arial", 14, "bold"))

t.pensize(3)
t.color("red")
t.up()
t.goto(-X * sx, A * (-X) ** B * sy)
t.down()
for i in range(-60, 61):
    x = i * X / 60
    t.goto(x * sx, A * x ** B * sy)
t.screen.exitonclick()
t.screen.mainloop()

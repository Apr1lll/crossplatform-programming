from turtle import *
t = Turtle()
t.screen.setup(800, 600)
t.screen.bgcolor("lightyellow")
t.color("darkblue")
t.pensize(2)
t.speed(0)
t.hideturtle()
k = 1.4

def go(x, y):
    t.goto((x - 280) * k, (196 - y) * k)

def line(points):
    t.up()
    go(points[0][0], points[0][1])
    t.down()
    for p in points[1:]:
        go(p[0], p[1])

def label(text, x, y):
    t.up()
    go(x, y)
    t.write(text, font=("Arial", 18, "bold"))

def diamond(x, y, half):
    side = half * 2 ** 0.5 * k
    t.up()
    go(x, y)
    t.setheading(45)
    t.down()
    for i in range(4):
        t.fd(side)
        t.right(90)

line([(33, 5), (133, 5), (133, 105), (33, 105), (33, 5)])
line([(33, 105), (133, 5)])
label("1)", 5, 32)

line([(148, 65), (248, 65), (248, 165), (148, 165), (148, 65)])
line([(148, 65), (208, 5), (308, 5), (248, 65)])
line([(308, 5), (308, 105), (248, 165)])
label("2)", 150, 28)

line([(342, 7), (442, 57), (542, 7), (492, 107), (542, 207), (442, 157), (342, 207), (392, 107), (342, 7)])
line([(342, 7), (542, 207)])
line([(542, 7), (342, 207)])
line([(442, 57), (442, 157)])
line([(392, 107), (492, 107)])
label("3)", 330, 112)

x = 24
y = 149
t.up()
go(x, y)
t.down()
for i in range(8):
    x += 15
    go(x, y - 9.5)
    go(x, y + 10)
    y += 10
x = 144
y = 229
for i in range(8):
    x += 20
    go(x, y - 18.75)
    go(x, y)
for i in range(8):
    x = 143.5 - 15 * i
    y = 229.5 + 15 * i
    line([(x - 19.5, y), (x, y), (x, y + 19.5), (x - 19.5, y)])
label("4)", 20, 245)

left = 138
for i in range(1, 8):
    diamond(left, 309.5, 10 * i)
    left = left + 20 * i - 10 * (i - 1)
label("5)", 150, 358)

t.screen.exitonclick()
t.screen.mainloop()

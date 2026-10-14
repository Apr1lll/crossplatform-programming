import turtle
import math

n = 5
r = 80

wndow = turtle.Screen()
wndow.title("Button and star")
wndow.setup(500, 500)

btn = turtle.Turtle()
btn.hideturtle()
btn.up()
btn.goto(0, -r)
btn.down()
btn.fillcolor("orange")
btn.begin_fill()
btn.circle(r)
btn.end_fill()
btn.up()
btn.goto(0, -10)
btn.write("Push me", align="center", font=("Arial", 16, "bold"))

star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.pensize(3)
star.color("purple")

def draw_star(R):
    points = []
    for i in range(n):
        a = math.pi / 2 + 2 * math.pi * i / n
        points.append((R * math.cos(a), R * math.sin(a)))
    for i in range(n):
        star.up()
        star.goto(points[i])
        star.down()
        star.goto(points[(i + 2) % n])

def btnclick(x, y):
    if x * x + y * y <= r * r:
        btn.clear()
        draw_star(180)

turtle.listen()
turtle.onscreenclick(btnclick, 1)
turtle.done()

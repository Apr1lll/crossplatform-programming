import tkinter as tk
import turtle

def draw_spiral(event):
    window = tk.Toplevel(root)
    window.title("Черепашка")

    canvas = tk.Canvas(window, width=600, height=600, bg="white")
    canvas.pack()

    t = turtle.RawTurtle(canvas)
    t.speed(-1)
    t.pensize(2)

    colors = ["red", "orange", "gold", "green", "blue", "purple"]
    size = 10
    for i in range(36):
        t.pencolor(colors[i % 6])
        for j in range(4):
            t.forward(size)
            t.left(90)
        t.left(10)
        size += 5

root = tk.Tk()
root.title("Главное окно")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

canvas.create_oval(50, 60, 250, 140, fill="lightblue", outline="blue", width=2, tags="button")
canvas.create_text(150, 100, text="Нарисовать", font=("Arial", 14), tags="button")

canvas.tag_bind("button", "<Button-1>", draw_spiral)

root.mainloop()
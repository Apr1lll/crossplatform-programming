from tkinter import *
window = Tk()
window.title("Hello world")
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()

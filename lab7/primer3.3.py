from tkinter import *

def clicked():
    lbl.configure(text="кнопку нажали")

window = Tk()
window.title("Hello world")
window.geometry('400x250')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

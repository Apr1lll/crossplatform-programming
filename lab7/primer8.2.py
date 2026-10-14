from tkinter import *
from tkinter import scrolledtext

def clear():
    txt.delete(1.0, END)

window = Tk()
window.title("hello world")
window.geometry('400x250')
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
txt.insert(INSERT, 'Текстовое поле')
btn = Button(window, text="Очистить", command=clear)
btn.grid(column=0, row=1)
window.mainloop()

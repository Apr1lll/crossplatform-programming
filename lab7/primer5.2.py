from tkinter import *
from tkinter.ttk import Combobox

def clicked():
    lbl.configure(text=combo.get())

window = Tk()
window.title("hello world")
window.geometry('400x250')
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)
combo.grid(column=0, row=0)
btn = Button(window, text="Клик", command=clicked)
btn.grid(column=1, row=0)
lbl = Label(window)
lbl.grid(column=0, row=1)
window.mainloop()

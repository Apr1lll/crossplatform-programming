from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("hello world")
window.geometry('400x250')
chk = Checkbutton(window, text='Выбрать')
chk.grid(column=0, row=0)
window.mainloop()

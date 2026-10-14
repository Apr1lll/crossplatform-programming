from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("hello world")
window.geometry('400x250')
chk_state = IntVar()
chk_state.set(1)
chk = Checkbutton(window, text='Выбрать', variable=chk_state)
chk.grid(column=0, row=0)
window.mainloop()

from tkinter import *
window = Tk()
window.title("hello world")
window.geometry('400x250')
spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=0)
window.mainloop()

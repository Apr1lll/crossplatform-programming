from tkinter import *
from tkinter import filedialog
from os import path

def clicked1():
    file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    print(file)

def clicked2():
    folder = filedialog.askdirectory()
    print(folder)

def clicked3():
    file = filedialog.askopenfilename(initialdir=path.dirname(__file__))
    print(file)

window = Tk()
window.title("hello world")
window.geometry('400x250')
btn1 = Button(window, text='Выбрать файл', command=clicked1)
btn1.grid(column=0, row=0)
btn2 = Button(window, text='Выбрать папку', command=clicked2)
btn2.grid(column=1, row=0)
btn3 = Button(window, text='Файл из папки программы', command=clicked3)
btn3.grid(column=2, row=0)
window.mainloop()

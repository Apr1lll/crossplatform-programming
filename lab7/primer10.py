from tkinter import *
from tkinter import messagebox

def clicked():
    res = messagebox.askquestion('Заголовок', 'Текст')
    print(res)
    res = messagebox.askyesno('Заголовок', 'Текст')
    print(res)
    res = messagebox.askyesnocancel('Заголовок', 'Текст')
    print(res)
    res = messagebox.askokcancel('Заголовок', 'Текст')
    print(res)
    res = messagebox.askretrycancel('Заголовок', 'Текст')
    print(res)

window = Tk()
window.title("hello world")
window.geometry('400x250')
btn = Button(window, text='Клик', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()

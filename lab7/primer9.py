from tkinter import *
from tkinter import messagebox

def clicked1():
    messagebox.showinfo('Заголовок', 'Текст')

def clicked2():
    messagebox.showwarning('Заголовок', 'Текст')

def clicked3():
    messagebox.showerror('Заголовок', 'Текст')

window = Tk()
window.title("hello world")
window.geometry('400x250')
btn1 = Button(window, text='Информация', command=clicked1)
btn1.grid(column=0, row=0)
btn2 = Button(window, text='Предупреждение', command=clicked2)
btn2.grid(column=1, row=0)
btn3 = Button(window, text='Ошибка', command=clicked3)
btn3.grid(column=2, row=0)
window.mainloop()

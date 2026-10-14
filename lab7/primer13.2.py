from tkinter import *
from tkinter import Menu
from tkinter import messagebox

def clicked():
    messagebox.showinfo('Меню', 'Выбран пункт Новый')

window = Tk()
window.title("hello world")
window.geometry('400x250')
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый', command=clicked)
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
window.mainloop()

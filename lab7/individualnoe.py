from tkinter import *
from tkinter import ttk

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_mersenne_prime(n):
    if n == 2:
        return True
    if not is_prime(n):
        return False
    m = 2 ** n - 1
    s = 4
    for i in range(n - 2):
        s = (s * s - 2) % m
    return s == 0

clicks = 0
power = 1

def next_number():
    global clicks, power
    clicks += 1
    power += 1
    while not is_mersenne_prime(power):
        power += 1
    btn1.configure(text="Щелчок " + str(clicks) + ": " + str(2 ** power - 1))

def go_on():
    text2.delete(1.0, END)
    if pwd.get() == "6"  or pwd.get() == "шесть":
        text2.insert(INSERT, ending)
    else:
        text2.insert(INSERT, "Неверный пароль! Концовка осталась секретом.")

def show_word():
    word = ""
    for i in range(5):
        if states[i].get() == 1:
            word = word + letters[i]
    text3.delete(1.0, END)
    text3.insert(INSERT, word)

def show_example():
    text4.delete(1.0, END)
    text4.insert(INSERT, examples[selected.get() - 1])

window = Tk()
window.title("Лабораторная работа 7")
window.geometry('560x320')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Кнопка')
tab_control.add(tab2, text='Сообщение')
tab_control.add(tab3, text='Буквы')
tab_control.add(tab4, text='Типы')
tab_control.pack(expand=1, fill='both')

btn1 = Button(tab1, text="Нажми меня", font=("Arial", 14), command=next_number)
btn1.grid(column=0, row=0, padx=20, pady=20)

story = "«Что выведет программа print(2 + 2 * 2);»"
ending = "«Ошибку! Кому нужны эти точки с запятной?"
lbl2 = Label(tab2, text="Начало истории:")
lbl2.grid(column=0, row=0)
text1 = Text(tab2, width=60, height=4, wrap=WORD)
text1.grid(column=0, row=1, columnspan=2)
text1.insert(INSERT, story)
lbl3 = Label(tab2, text="Пароль:")
lbl3.grid(column=0, row=2)
pwd = Entry(tab2, width=20, show="*")
pwd.grid(column=1, row=2)
btn2 = Button(tab2, text="Продолжить", command=go_on)
btn2.grid(column=0, row=3, columnspan=2)
lbl4 = Label(tab2, text="Продолжение:")
lbl4.grid(column=0, row=4)
text2 = Text(tab2, width=60, height=5, wrap=WORD)
text2.grid(column=0, row=5, columnspan=2)

letters = ["К", "О", "Т", "Р", "А"]
states = []
for i in range(5):
    v = IntVar()
    states.append(v)
    chk = ttk.Checkbutton(tab3, text=letters[i], variable=v, command=show_word)
    chk.grid(column=i, row=0, padx=10, pady=10)
lbl5 = Label(tab3, text="Слово:")
lbl5.grid(column=0, row=1)
text3 = Text(tab3, width=30, height=2)
text3.grid(column=1, row=1, columnspan=4)

names = ["int", "float", "bool", "str", "tuple", "frozenset"]
examples = ["42", "3.14", "True", "'Привет'", "(1, 2, 3)", "frozenset({1, 2, 3})"]
selected = IntVar()
for i in range(6):
    rad = ttk.Radiobutton(tab4, text=names[i], value=i + 1, variable=selected, command=show_example)
    rad.grid(column=i, row=0, padx=5, pady=10)
lbl6 = Label(tab4, text="Пример:")
lbl6.grid(column=0, row=1)
text4 = Text(tab4, width=30, height=2)
text4.grid(column=1, row=1, columnspan=5)

window.mainloop()

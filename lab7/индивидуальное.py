import os
import tkinter as tk
from tkinter import ttk, messagebox

folder = os.path.dirname(os.path.abspath(__file__))
users_file = os.path.join(folder, "users.txt")



def load_users():
    users = {}
    if os.path.exists(users_file):
        f = open(users_file, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split(";")
                users[parts[0]] = parts[1]
        f.close()
    return users


def save_user(login, password):
    f = open(users_file, "a", encoding="utf-8")
    f.write(login + ";" + password + "\n")
    f.close()


users = load_users()



def calc_mortgage(amount, rate, years, down, pay_type, insurance_on):
    loan = amount * (1 - down / 100)   # сумма кредита за вычетом взноса
    n = years * 12                     # количество месяцев
    r = rate / 100 / 12                # ставка за месяц

    insurance = 0
    if insurance_on:
        insurance = loan * 0.01 / 12   # страховка 1% в год

    if pay_type == "Аннуитетный":
        if r == 0:
            payment = loan / n
        else:
            k = (1 + r) ** n
            payment = loan * r * k / (k - 1)
        payment = payment + insurance
        total = payment * n
        text = f"Ежемесячный платёж: {payment:.2f} ₽"
    else:
        principal = loan / n           # часть основного долга
        total = 0
        first = 0
        last = 0
        for month in range(n):
            debt = loan - principal * month
            payment = principal + debt * r + insurance
            total = total + payment
            if month == 0:
                first = payment
            last = payment
        text = f"Ежемесячный платёж: от {first:.2f} до {last:.2f} ₽"

    overpay = total - loan
    text = f"Сумма кредита: {loan:.2f} ₽\n" + text + f"\nПереплата: {overpay:.2f} ₽"
    return text



def register():
    login = login_entry.get().strip()
    password = password_entry.get()
    if login == "" or password == "":
        messagebox.showerror("Ошибка", "Введите логин и пароль")
        return
    if login in users:
        messagebox.showerror("Ошибка", "Такой пользователь уже есть")
        return
    if len(password) < 4:
        messagebox.showerror("Ошибка", "Пароль должен быть не короче 4 символов")
        return
    users[login] = password
    save_user(login, password)
    messagebox.showinfo("Готово", "Регистрация прошла успешно, теперь войдите")


def log_in():
    login = login_entry.get().strip()
    password = password_entry.get()
    if login in users and users[login] == password:
        login_frame.pack_forget()
        calc_frame.pack(padx=20, pady=20)
        root.title("Ипотечный калькулятор")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")



def calculate():
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        years = int(years_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа во все поля")
        return
    if amount <= 0 or rate < 0 or years <= 0:
        messagebox.showerror("Ошибка", "Значения должны быть больше нуля")
        return

    text = calc_mortgage(amount, rate, years, down_var.get(),
                         type_box.get(), insurance_var.get())
    result_label.config(text=text)



root = tk.Tk()
root.title("Авторизация")

login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)

tk.Label(login_frame, text="Логин:").grid(row=0, column=0, sticky="w")
login_entry = tk.Entry(login_frame)
login_entry.grid(row=0, column=1, pady=5)

tk.Label(login_frame, text="Пароль:").grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, pady=5)

tk.Button(login_frame, text="Войти", command=log_in).grid(row=2, column=0, pady=10)
tk.Button(login_frame, text="Регистрация", command=register).grid(row=2, column=1, pady=10)

calc_frame = tk.Frame(root)

tk.Label(calc_frame, text="Сумма, ₽:").grid(row=0, column=0, sticky="w")
amount_entry = tk.Entry(calc_frame)
amount_entry.grid(row=0, column=1, pady=3)

tk.Label(calc_frame, text="Ставка, % годовых:").grid(row=1, column=0, sticky="w")
rate_entry = tk.Entry(calc_frame)
rate_entry.grid(row=1, column=1, pady=3)

tk.Label(calc_frame, text="Срок, лет:").grid(row=2, column=0, sticky="w")
years_entry = tk.Entry(calc_frame)
years_entry.grid(row=2, column=1, pady=3)

tk.Label(calc_frame, text="Тип платежа:").grid(row=3, column=0, sticky="w")
type_box = ttk.Combobox(calc_frame, values=["Аннуитетный", "Дифференцированный"], state="readonly")
type_box.current(0)
type_box.grid(row=3, column=1, pady=3)

insurance_var = tk.BooleanVar()
tk.Checkbutton(calc_frame, text="Учитывать страховку", variable=insurance_var).grid(
    row=4, column=0, columnspan=2, sticky="w")

tk.Label(calc_frame, text="Первоначальный взнос:").grid(row=5, column=0, sticky="w")
down_var = tk.IntVar(value=10)
down_frame = tk.Frame(calc_frame)
down_frame.grid(row=5, column=1, sticky="w")
tk.Radiobutton(down_frame, text="10%", variable=down_var, value=10).pack(side="left")
tk.Radiobutton(down_frame, text="20%", variable=down_var, value=20).pack(side="left")
tk.Radiobutton(down_frame, text="30%", variable=down_var, value=30).pack(side="left")

tk.Button(calc_frame, text="Рассчитать", command=calculate).grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(calc_frame, text="", justify="left")
result_label.grid(row=7, column=0, columnspan=2, sticky="w")

root.mainloop()

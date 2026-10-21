import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QComboBox, QCheckBox, QRadioButton, QGridLayout,
                             QHBoxLayout, QMessageBox)

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



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")

        self.login_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Войти")
        login_button.clicked.connect(self.log_in)
        reg_button = QPushButton("Регистрация")
        reg_button.clicked.connect(self.register)

        layout = QGridLayout()
        layout.addWidget(QLabel("Логин:"), 0, 0)
        layout.addWidget(self.login_edit, 0, 1)
        layout.addWidget(QLabel("Пароль:"), 1, 0)
        layout.addWidget(self.password_edit, 1, 1)
        layout.addWidget(login_button, 2, 0)
        layout.addWidget(reg_button, 2, 1)
        self.setLayout(layout)

    def register(self):
        login = self.login_edit.text().strip()
        password = self.password_edit.text()
        if login == "" or password == "":
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль")
            return
        if login in users:
            QMessageBox.warning(self, "Ошибка", "Такой пользователь уже есть")
            return
        if len(password) < 4:
            QMessageBox.warning(self, "Ошибка", "Пароль должен быть не короче 4 символов")
            return
        users[login] = password
        save_user(login, password)
        QMessageBox.information(self, "Готово", "Регистрация прошла успешно, теперь войдите")

    def log_in(self):
        login = self.login_edit.text().strip()
        password = self.password_edit.text()
        if login in users and users[login] == password:
            self.calc = CalcWindow()
            self.calc.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")



class CalcWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ипотечный калькулятор")

        self.amount_edit = QLineEdit()
        self.rate_edit = QLineEdit()
        self.years_edit = QLineEdit()

        self.type_box = QComboBox()
        self.type_box.addItems(["Аннуитетный", "Дифференцированный"])

        self.insurance_check = QCheckBox("Учитывать страховку")

        self.radio10 = QRadioButton("10%")
        self.radio20 = QRadioButton("20%")
        self.radio30 = QRadioButton("30%")
        self.radio10.setChecked(True)
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio10)
        radio_layout.addWidget(self.radio20)
        radio_layout.addWidget(self.radio30)

        calc_button = QPushButton("Рассчитать")
        calc_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        layout = QGridLayout()
        layout.addWidget(QLabel("Сумма, ₽:"), 0, 0)
        layout.addWidget(self.amount_edit, 0, 1)
        layout.addWidget(QLabel("Ставка, % годовых:"), 1, 0)
        layout.addWidget(self.rate_edit, 1, 1)
        layout.addWidget(QLabel("Срок, лет:"), 2, 0)
        layout.addWidget(self.years_edit, 2, 1)
        layout.addWidget(QLabel("Тип платежа:"), 3, 0)
        layout.addWidget(self.type_box, 3, 1)
        layout.addWidget(self.insurance_check, 4, 0, 1, 2)
        layout.addWidget(QLabel("Первоначальный взнос:"), 5, 0)
        layout.addLayout(radio_layout, 5, 1)
        layout.addWidget(calc_button, 6, 0, 1, 2)
        layout.addWidget(self.result_label, 7, 0, 1, 2)
        self.setLayout(layout)

    def calculate(self):
        try:
            amount = float(self.amount_edit.text())
            rate = float(self.rate_edit.text())
            years = int(self.years_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите числа во все поля")
            return
        if amount <= 0 or rate < 0 or years <= 0:
            QMessageBox.warning(self, "Ошибка", "Значения должны быть больше нуля")
            return

        if self.radio10.isChecked():
            down = 10
        elif self.radio20.isChecked():
            down = 20
        else:
            down = 30

        text = calc_mortgage(amount, rate, years, down,
                             self.type_box.currentText(),
                             self.insurance_check.isChecked())
        self.result_label.setText(text)


app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec())

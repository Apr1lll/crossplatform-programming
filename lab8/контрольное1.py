import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
    QMessageBox, QApplication)


class SuccessWindow(QWidget):
    def __init__(self, login, auth_window):
        super().__init__()
        self.auth_window = auth_window
        self.initUI(login)

    def initUI(self, login):
        self.lbl = QLabel('Успешная авторизация!', self)
        self.lbl.move(60, 30)
        self.lbl.adjustSize()
        self.lbl_user = QLabel('Добро пожаловать, ' + login, self)
        self.lbl_user.move(60, 70)
        self.lbl_user.adjustSize()
        self.btn = QPushButton('Выйти', self)
        self.btn.move(60, 110)
        self.btn.clicked.connect(self.logout)
        self.setGeometry(300, 300, 300, 180)
        self.setWindowTitle('Успешная авторизация')

    def logout(self):
        self.auth_window.le_login.clear()
        self.auth_window.le_password.clear()
        self.auth_window.show()
        self.close()


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.users = {}
        self.initUI()

    def initUI(self):
        self.lbl_login = QLabel('Логин:', self)
        self.lbl_login.move(30, 30)
        self.le_login = QLineEdit(self)
        self.le_login.move(100, 28)
        self.lbl_password = QLabel('Пароль:', self)
        self.lbl_password.move(30, 70)
        self.le_password = QLineEdit(self)
        self.le_password.setEchoMode(QLineEdit.Password)
        self.le_password.move(100, 68)
        self.btn_login = QPushButton('Войти', self)
        self.btn_login.move(30, 120)
        self.btn_login.clicked.connect(self.login)
        self.btn_register = QPushButton('Регистрация', self)
        self.btn_register.move(140, 120)
        self.btn_register.clicked.connect(self.register)
        self.setGeometry(300, 300, 300, 180)
        self.setWindowTitle('Авторизация')
        self.show()

    def register(self):
        login = self.le_login.text()
        password = self.le_password.text()
        if login == '' or password == '':
            QMessageBox.warning(self, 'Ошибка', 'Введите логин и пароль')
        elif login in self.users:
            QMessageBox.warning(self, 'Ошибка', 'Такой логин уже занят')
        else:
            self.users[login] = password
            QMessageBox.information(self, 'Регистрация', 'Вы зарегистрированы')

    def login(self):
        login = self.le_login.text()
        password = self.le_password.text()
        if login in self.users and self.users[login] == password:
            self.success = SuccessWindow(login, self)
            self.success.show()
            self.hide()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthWindow()
    sys.exit(app.exec_())

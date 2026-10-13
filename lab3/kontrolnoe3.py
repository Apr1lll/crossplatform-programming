while True:
    email = input('Введите электронную почту: ')
    at = email.find('@')
    dot = email.rfind('.')
    if email.count('@') == 1 and ' ' not in email and at > 0 and dot > at + 1 and dot < len(email) - 1:
        print('Почта введена верно')
        break
    print('Почта введена неверно, попробуйте еще раз')

ticket = input("Введите номер билета (6 цифр): ")

if len(ticket) != 6 or not ticket.isdigit():
    print("Ошибка: нужно ввести ровно 6 цифр")
else:
    first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if first == second:
        print("Счастливый билет!")
    else:
        print("Обычный билет")
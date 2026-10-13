money = int(input("Введите сумму в рублях: "))

if money % 2 != 0:
    print("Размен невозможен: есть нечётная часть суммы")
else:
    count500 = money // 500
    money %= 500

    count100 = money // 100
    money %= 100

    count10 = money // 10
    money %= 10

    count2 = money // 2

    print("Купюр по 500:", count500)
    print("Купюр по 100:", count100)
    print("Купюр по 10:", count10)
    print("Монет по 2 руб.:", count2)
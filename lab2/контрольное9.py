def get_category(age):
    if 0 <= age < 7:
        return "Вам в детский сад"
    elif 7 <= age < 18:
        return "Вам в школу"
    elif 18 <= age < 25:
        return "Вам в профессиональное учебное заведение"
    elif 25 <= age < 65:
        return "Вам на работу"
    elif 65 <= age <= 120:
        return "Вам предоставляется выбор"
    else:
        return "Ошибка ввода"


def main():
    print("=== Программа определения возрастной категории ===")

    while True:
        age = int(input("Введите ваш возраст (для выхода введите -1): "))

        if age == -1:
            print("Программа завершена.")
            break

        print(get_category(age))


main()
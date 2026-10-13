fio = input("Введите ваше полное имя: ")

words = fio.split()

words.sort(key=len)

print("Слова по возрастанию длины:", words)
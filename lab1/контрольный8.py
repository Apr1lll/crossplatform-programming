text = input("Введите фразу: ")

text = text.lower().replace(" ", "")

reversed_text = text[::-1]

if text == reversed_text:
    print("Это палиндром!")
else:
    print("Это НЕ палиндром")
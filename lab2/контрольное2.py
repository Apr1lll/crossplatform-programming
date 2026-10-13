fio = input("Введите ваше полное имя: ")

words = fio.split()

longest = max(words, key=len)
shortest = min(words, key=len)

print("Самое длинное слово:", longest, f"(длина {len(longest)})")
print("Самое короткое слово:", shortest, f"(длина {len(shortest)})")
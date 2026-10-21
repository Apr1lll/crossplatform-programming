vowels = "аеёиоуыэюяaeiou"
signs = ".,!?;:«»()\"'—-…"

f = open("Война_и_мир.txt", "r", encoding="utf-8")
text = f.read()
f.close()

result = []
for word in text.split():
    word = word.strip(signs)
    if word != "" and word[0].lower() in vowels:
        new_word = word[0].upper() + word[1:]
        result.append(new_word)

f = open("слова_на_гласную.txt", "w", encoding="utf-8")
for word in result:
    f.write(word + "\n")
f.close()

print("Слов на гласную:", len(result))
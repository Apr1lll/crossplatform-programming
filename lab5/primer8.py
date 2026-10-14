file = open('строки.txt', 'w')
file.write('строка 1\n')
file.write('строка 2')
file.close()
list_1 = []
file = open('строки.txt', 'r')
for line in file:
    list_1.append(line.strip())
print(list_1)
file.close()

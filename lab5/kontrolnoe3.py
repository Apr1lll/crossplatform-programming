import os
file = open('дети.txt', 'w')
file.write('Иванов Иван 5 лет\n')
file.write('Петров Пётр 7 лет\n')
file.write('Сидорова Анна 3 года\n')
file.write('Смирнова Мария 6 лет\n')
file.write('Кузнецов Олег 4 года\n')
file.close()
file = open('дети.txt', 'r')
oldest = ''
youngest = ''
max_age = 0
min_age = 100
for line in file:
    line = line.strip()
    age = int(line.split()[2])
    if age > max_age:
        max_age = age
        oldest = line
    if age < min_age:
        min_age = age
        youngest = line
file.close()
file = open('старший и младший.txt', 'w')
file.write('Самый старший: ' + oldest + '\n')
file.write('Самый младший: ' + youngest)
file.close()
os.rename('дети.txt', 'Детский сад.txt')

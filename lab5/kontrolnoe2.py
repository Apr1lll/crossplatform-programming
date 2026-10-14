file = open('числа.txt', 'w')
file.write('5 -3 12 8 0 -7 25 4 -15 9')
file.close()
file = open('числа.txt', 'r')
numbers = []
for n in file.read().split():
    numbers.append(int(n))
file.close()
file = open('результат.txt', 'w')
file.write('Максимум: ' + str(max(numbers)) + '\n')
file.write('Минимум: ' + str(min(numbers)))
file.close()

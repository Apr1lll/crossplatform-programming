file = open('числа.txt', 'w')
file.write('3\n')
file.write('5\n')
file.write('-2\n')
file.write('7\n')
file.write('4\n')
file.close()
file = open('числа.txt', 'r')
numbers = []
for s in file:
    numbers.append(int(s.strip()))
file.close()
print('Максимум:', max(numbers))
print('Минимум:', min(numbers))

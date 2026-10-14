file = open('числа.txt', 'w')
file.write('3\n')
file.write('5\n')
file.write('2\n')
file.write('7\n')
file.write('4\n')
file.close()
file = open('числа.txt', 'r')
p = 1
for s in file:
    n = int(s.strip())
    print(n)
    p = p * n
file.close()
print('Произведение:', p)

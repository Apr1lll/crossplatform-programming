import math
x = []
y1 = []
y2 = []
y = []
for i in range(-6, 7):
    x.append(i)
    a = math.sqrt(1 + 2 * i ** 2 - math.sin(i) ** 2)
    b = (2 + i) / (2 + math.exp(-i)) ** (1 / 3)
    y1.append(a)
    y2.append(b)
    y.append(a + b)
y.sort()
file = open('data.txt', 'w')
file.write('x y1 y2\n')
for i in range(len(x)):
    file.write(str(x[i]) + ' ' + str(round(y1[i], 4)) + ' ' + str(round(y2[i], 4)) + '\n')
file.write('\ny = y1 + y2 по возрастанию:\n')
for v in y:
    file.write(str(round(v, 4)) + '\n')
file.write('\nmin(y1) = ' + str(round(min(y1), 4)) + '\n')
file.write('min(y2) = ' + str(round(min(y2), 4)) + '\n')
if min(y1) > min(y2):
    file.write('min(y1) > min(y2)')
elif min(y1) < min(y2):
    file.write('min(y1) < min(y2)')
else:
    file.write('min(y1) = min(y2)')
file.close()

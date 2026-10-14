import random
file = open('случайные.txt', 'w')
for i in range(10):
    file.write(str(random.randint(1, 100)) + '\n')
file.close()

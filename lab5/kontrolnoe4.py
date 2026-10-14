file = open('данные.txt', 'r')
for s in file:
    print(s.strip())
file.close()

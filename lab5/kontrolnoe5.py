list_1 = []
file = open('данные.txt', 'r')
for s in file:
    list_1.append(s.strip())
print(list_1)
file.close()

file = open('input.txt', 'r')
numbers = file.read().split()
file.close()
p = 1
for n in numbers:
    p = p * int(n)
file = open('output.txt', 'w')
file.write(str(p))
file.close()

print("Введите a, b, c, d через пробел: ", end = '')
a,b,c,d = map(int, input().split())

d1 = (a/b)+(c/d)
d2 = a*c-b*d
d3 = a**2 - b**2
d4 = c+d

res = d1/d2+d3/d4

print("Ответ:", res)
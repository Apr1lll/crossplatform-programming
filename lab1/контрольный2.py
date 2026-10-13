a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

verh1 = (1/a) - (1/(b+c))
niz1 = (1/a) + (1/(b+c))
drob1 = verh1 / niz1

skobki = 1 + (b**2 + c**2 - a**2) / (2*b*c)

drob2 = (a - b - c) / (a * b * c)

z1 = drob1 * skobki / drob2

z2 = ((a - b - c) / 2) * a

print("z1 =", z1)
print("z2 =", z2)
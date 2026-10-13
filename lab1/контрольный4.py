a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
c=float(input("Введите третье число: "))

maximum=a

if b>maximum:
    maximum=b
if c>maximum:
    maximum=c

print("Максимальное число =", maximum)
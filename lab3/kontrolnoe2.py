for count in range(3, 5):
    start = 10 ** (count - 1)
    end = 10 ** count
    print(count, '-значные числа Армстронга:')
    for n in range(start, end):
        x = n
        s = 0
        while x > 0:
            s += (x % 10) ** count
            x = x // 10
        if s == n:
            print(n)

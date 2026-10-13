s = input()
digits = set()
for c in s:
    if c in '0123456789':
        digits.add(c)
if len(digits) == 0:
    print('НЕТ')
else:
    print(' '.join(sorted(digits)))

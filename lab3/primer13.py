cities = tuple(input().split())
if 'Москва' not in cities:
    cities = cities + ('Москва',)
print(cities)

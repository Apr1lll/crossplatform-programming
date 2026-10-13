dishes = [
    ("Борщ", 35),
    ("Котлета", 40),
    ("Каша", 20),
    ("Чай", 3)
]

dishes.sort(key=lambda x: x[1])

print("Блюда по возрастанию цены:")
for name, price in dishes:
    print(f"  {name} — {price} руб.")
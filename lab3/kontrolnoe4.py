colors = {
    'red': 'красный',
    'orange': 'оранжевый',
    'yellow': 'желтый',
    'green': 'зеленый',
    'blue': 'синий',
    'black': 'черный',
    'white': 'белый'
}

print(colors)

for key in colors:
    last = key
print(colors[last])

del colors['red']
print(colors)

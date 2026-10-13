lst = [3, 5, 2, 8, 5, 1, 9, 5, 4, 7]

print("Исходный список:", lst)

i_max = lst.index(max(lst))
i_min = lst.index(min(lst))

lst[i_max], lst[i_min] = lst[i_min], lst[i_max]

print("После обмена max и min:", lst)

print("\nПовторяющиеся элементы:")
for elem in set(lst):
    count = lst.count(elem)
    if count > 1:
        print(f"  {elem} — встречается {count} раз")
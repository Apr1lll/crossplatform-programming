bytes_ = float(input("Введите объём информации в байтах: "))

kilobytes = bytes_ / 1024
megabytes = bytes_ / (1024 ** 2)

print(f"Объём в байтах:     {bytes_}")
print(f"Объём в Кбайтах:    {kilobytes}")
print(f"Объём в Мбайтах:    {megabytes}")
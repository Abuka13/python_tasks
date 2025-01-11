height = 10

for i in range(1, height + 1):
    # Печатаем пробелы
    for j in range(height - i):
        print(" ", end="")
    # Печатаем звездочки
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # Переход на новую строку


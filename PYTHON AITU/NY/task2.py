height = 10

for i in range(1, height + 1):
    # Печатаем пробелы
    for j in range(height - i):
        print(" ", end="")
    #we write the number 2025, but i dont know when
    if i == j:
        print(" ", 2025)
    # Печатаем звездочки
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # Переход на новую строку


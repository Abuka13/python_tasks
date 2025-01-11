start = 1
stop = 2
current_num = 2ы

for row in range(1, 5):
    for col in range(row):
        current_num -= 1
        print(current_num, end=" ")
    print()
    start = current_num
    stop += row + 1
    current_num = stop

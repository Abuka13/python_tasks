x = 5
for i in range(x):
    for j in range(x):
        if i == j or i + j == x - 1:
            print("1", end="")
        else:
            print("0", end="")
    print()
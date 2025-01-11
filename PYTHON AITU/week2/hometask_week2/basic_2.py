number1 = float(input("Input the first number: "))
number2 = float(input("Input the second number: "))
number3 = float(input("Input the third number: "))
if number1 > 0:
    number1 = number1 * number1 * number1
else:
    number1 = 0


if number2 > 0:
    number2 = number2 * number2 * number2
else:
    number2 = 0


if number3 > 0:
    number3 = number3 * number3 * number3
else:
    number3 = 0
print(f"First number: {number1},\nsecond number: {number2},\nthird number: {number3}")
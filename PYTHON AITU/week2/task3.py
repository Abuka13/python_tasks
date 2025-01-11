number1 = float(input("Input the first number: "))
number2 = float(input("Input the second number: "))
number3 = float(input("Input the third number: "))
number4 = float(input("Input the fourth number: "))
sum1 = number1 + number2
sum2 = number3 + number4
if sum2 == 0:
    print("Error, sum2 cannot be zero")
else:
    result = sum1 / sum2
    print(f"The result is: {result:.2f}")


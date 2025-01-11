num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
if num1*num1 + num2 * num2 > (num1+num2) * (num1+num2):
    print("The sum of their squares is greater")
elif (num1*num1) + (num2 * num2) < (num1+num2) * (num1+num2):
    print("The sum of their squares is less")
elif num1*num1 + num2 * num2 == (num1+num2) * (num1+num2):
    print("The sum of their squares is equal")
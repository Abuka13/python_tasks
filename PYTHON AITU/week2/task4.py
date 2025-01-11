number1 = input("Input the first value: ")
number2 = input("Input the second value: ")
try:
    number1 = int(number1)
    number2 = int(number2)
    print(number1+number2)
except ValueError:
    print(str(number1)+str(number2))
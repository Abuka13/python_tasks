a = input("Enter a number: ")
digit1 = int(a[0])
digit2 = int(a[1])
digit3 = int(a[2])
multiply = digit1 * digit2 * digit3
digit_sum = digit1 + digit2 + digit3
if multiply < int(a):
    print("The product is less")
else:
    print("The product is bigger")
if digit_sum % 5 == 0:
    print("The sum of the digits can be divided by 5")
else:
    print("The sum of the digits can not be divided by 5")


day = int(input("Enter a day: "))
if 1 <= day <= 31:
    last = 27
    lunar = 28
    next = last + lunar
    while next > 31:
        next -= 31
    print(f"The next full moon is on day: {next}.")


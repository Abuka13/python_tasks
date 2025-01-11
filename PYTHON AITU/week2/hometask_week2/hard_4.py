import datetime
current_day = int(input("Enter the current day: "))
current_month = int(input("Enter the current month: "))
current_year = int(input("Enter the current year: "))

birthday_day = int(input("Enter the day of your birthday: "))
birthday_month = int(input("Enter the month of your birthday: "))

if birthday_month > current_month or birthday_month == current_month and birthday_day > current_day:
    next_birthday_year = current_year
else:
    next_birthday_year = current_year + 1

next_birthday = datetime.date(next_birthday_year, birthday_month, birthday_day)
day_of_week = next_birthday.strftime("%A")

print(f"Your next birthday will fall on a {day_of_week}.")

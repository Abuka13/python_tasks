def sales_tax(amount):
    state_tax = amount * 0.04
    county_tax = amount * 0.02
    total_tax = state_tax + county_tax
    total_sale = amount + total_tax
    print("State Sales Tax:", state_tax)
    print("County Sales Tax:", county_tax)
    print("Total Sales Tax:", total_tax)
    print("Total Sale Amount:", total_sale)

def miles_per_gallon(miles, gallons):
    mpg = miles / gallons
    print("Miles per Gallon (MPG):", mpg)

def tip_tax_total(meal_charge):
    tip = meal_charge * 0.15
    sales_tax = meal_charge * 0.07
    total = meal_charge + tip + sales_tax
    print("Tip:", tip)
    print("Sales Tax:", sales_tax)
    print("Total Amount:", total)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    print("Temperature in Fahrenheit:", fahrenheit)



amount = float(input("Input purchase amount in $: "))
sales_tax(amount)
miles = float(input("Input number of miles driven: "))
gallons = float(input("Input gallons of gas used: "))
miles_per_gallon(miles, gallons)
meal_charge = float(input("Input price for the meal in $: "))
tip_tax_total(meal_charge)
celsius = float(input("Input temperature in Celsius: "))
celsius_to_fahrenheit(celsius)

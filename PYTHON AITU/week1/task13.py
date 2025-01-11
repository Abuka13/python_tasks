

def projected_sales(total,percent):
    print("Projected sales: ",total * (1 + percent))
def travel(speed, hours):
    print("The distance travelled: ", speed * hours)
def total_square_feet(total_feet):
    print("Total square feet: ",float(total_feet / 43560))
def product_sales(sales_tax_rate,subtotal):
    sales_tax = subtotal * sales_tax_rate
    print("Total product sales", subtotal + sales_tax)



percent = 0.23
total = float(input("Input total sale in $:"))
total_feet = float(input("Input total square feet: "))
prices = []
speed = 60

for i in range(1, 6):
    price = float(input(f"Enter the price of product {i} in $: "))
    prices.append(price)
total_square_feet(total_feet)
travel(speed,5)
travel(speed,8)
travel(speed,12)
projected_sales(total,percent)
product_sales(0.06, sum(prices))



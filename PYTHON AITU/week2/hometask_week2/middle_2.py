x = float(input("Enter the x of point B: "))
y = float(input("Enter the y of point B: "))
radius = float(input("Enter the radius of the circle R: "))

if x**2 + y**2 <= radius**2:
    print("The point is inside the circle.")
else:
    print("The point is outside the circle.")

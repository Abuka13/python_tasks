longitude = float(input("Enter the longitude of the point (in degrees): "))

if -180 <= longitude < 0:
    print("The point is in the western hemisphere.")
elif 0 <= longitude <= 180:
    print("The point is in the eastern hemisphere.")


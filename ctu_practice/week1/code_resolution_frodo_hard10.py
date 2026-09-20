# 10. Write a program that reads `distance_km` (float, input) and uses `speed_kmh = 27000` 
# to compute how many days a trip would take; print the result once formatted to 4 decimal places,
# and again formatted to 2 decimal places, each with its own label.

distance = float(input("What is the distance?"))
speed = float("27000")
days_traveled = distance / speed / 24
print("{:.2f}".format (days_traveled))
print("{:.4f}".format(days_traveled))


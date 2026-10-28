# Write a program using the `if __name__ == "__main__":` guard: 
# define a function `km_to_miles(km)` that returns the equivalent 
# distance in miles (1 km = 0.621371 miles), formatted to 2 decimal 
# places inside an f-string when printed. Put the input-reading and 
# printing logic inside the `if __name__ == "__main__":` block, not 
# at the top level of the file.

def km_to_miles(km):
    return km * 0.621371
if __name__ == "__main__":
        
    print(f"{km_to_miles(float(input())):.2f}")


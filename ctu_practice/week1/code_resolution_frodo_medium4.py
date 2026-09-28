# 4. Ask the user for a temperature in Celsius, 
# convert it to a `float`, and print the equivalent Fahrenheit 
# temperature (`F = C * 9/5 + 32`) formatted to exactly 2 decimal places.

temperature_C = float(input("What is the temperature in Celsius?"))
fahrenheit = temperature_C * 9/5 + 32
print("The temperature in Celsius is:", temperature_C)
print("And the temperature in Fahrenheit is: {:.2f}".format(fahrenheit))



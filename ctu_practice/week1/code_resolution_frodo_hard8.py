# 8. Write a program that reads `weight_kg` and `height_m` 
# (both floats, from input), computes BMI (`weight_kg / height_m ** 2`), 
# and prints the result formatted to 2 decimal places with a labeled message.
weight = float(input("What is your weight in KG"))
height = float(input("What is your height in Meters" ))
bmi_calculator = weight /height**2
print("Your BMI is:{:.2f}".format(bmi_calculator))

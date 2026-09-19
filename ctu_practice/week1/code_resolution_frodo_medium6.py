# 6. Ask for three separate purchase amounts (as input, converted to `float`) and print 
# their average formatted to 2 decimal places, labeled `"Average purchase: $X.XX"`.
amount1 = float(input())
amount2 = float(input())
amount3 = float(input())
average = amount1 + amount2 + amount3 / 3
print("The average purchase amount is: ${:.2f}".format(average))
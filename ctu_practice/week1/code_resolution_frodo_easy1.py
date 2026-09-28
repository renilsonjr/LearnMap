# 1. Write a script with fixed variables `daily_rate = 35`, `days = 6`, `weeks = 2` 
# that computes and prints the total pay for a pet-sitter, using one `print()` 
# call combining a label and the result.

daily_rate = 35
days = 6
weeks = 2

print("The daily rate for a pet-sitter is ${}, ".format(daily_rate), "working {} days per".format(days),"{} weeks".format(weeks))
print('The total pay is: ${}'.format(daily_rate * days * weeks))
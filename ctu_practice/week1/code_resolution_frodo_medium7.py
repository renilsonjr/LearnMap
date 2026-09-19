# 7. Write a script with a logic bug: 
# it's meant to apply a 10% discount but multiplies the price by `10` instead of `0.10`. 
# Leave the buggy version commented above the fixed, working version.



# value1 = int(input("What is price?"))
# percentage = value1 / 10 * 100 #the bug in percentage is this variable is because value1 comes first the /10
# print("With the 10 percent discount, the new price is:${:.2f}".format (value1 - percentage))


value1 = int(input("What is price?"))
percentage = 10 / value1 * 100 
print("With the 10 percent discount, the new price is:${:.2f}".format (value1 - percentage))
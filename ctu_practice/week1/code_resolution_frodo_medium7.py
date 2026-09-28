# 7. Write a script with a logic bug: 
# it's meant to apply a 10% discount but multiplies the price by `10` instead of `0.10`. 
# Leave the buggy version commented above the fixed, working version.



# value1 = int(input("What is price?"))
# percentage = (value * 10) #the bug here is because is multiplying by 10 instead of 0.10
# print("With the 10 percent discount, the new price is:${:.2f}".format (discount - value1))


value1 = int(input("What is price?"))
discount = (value1 * 0.10)
print("With the 10 percent discount, the new price is:${:.2f}".format (value1 - discount))
# 9. Write a script with a function-name bug: define a function with one 
# capitalization (for example `calc_Bonus`) but call it elsewhere with 
# different capitalization, and leave that broken version as a comment 
# showing the error it produces. Below it, write the corrected, working 
# version where the definition and every call match exactly.

# def calc_Bonus():
#     return "algo"
# print(calc_bonus()) #this script try to call a function that was not defined, "NameError"

def calc_Bonus():
    return "algo"
print(calc_Bonus())



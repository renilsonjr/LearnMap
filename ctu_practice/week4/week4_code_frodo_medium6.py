# 6. Write a function `minutes_to_hours(minutes)` with an intentional bug where it forgets the `return` statement 
# (leave the buggy version commented, showing what printing its result actually gives), then the corrected, working version below it.

def minutes_to_hours(minutes):
    resultado = minutes / 60
    #this function calculates and stores the result, but does not return it. Therefore, printing the function return value shows none.
print(minutes_to_hours(32)) 

def minutes_to_hours(minutes):
    return minutes / 60
print(minutes_to_hours(40))
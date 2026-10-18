# 5. Read a savings `goal` (float, input). Starting from `balance = 500.0`, 
# use a `while` loop that adds 8% interest each year until the balance reaches the goal; 
# print the year number and balance (2 decimals) on every iteration, then the total years it took.

goal = float(input())
balance = float(500.0)
year = 0
while balance <= goal:
    balance = balance * 1.08
    year = year + 1 
    
    print('In the {} year, you acumulated:{:.2f}, of interest'.format(year, balance))

print("It took {} years to reach your goal, and your balance is {:.2f}".format(year, balance))
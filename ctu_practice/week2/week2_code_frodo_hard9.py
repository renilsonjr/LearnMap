# 9. Write a program that reads three separate input integers and,
# using only `if`/`elif`/`else` (no `min()`, `max()`, or `sorted()`), 
# determines and prints the **median** (middle value) of the three.




num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2 and num1 > num3:
    print(num2)
elif num2 < num1 and num2 > num3:
    print(num3)
else:
    print(num2)

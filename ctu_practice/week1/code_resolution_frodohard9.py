# 9. Write a program that reads three separate inputs for hours worked on three different days, 
# sums them using an expression wrapped across multiple lines inside parentheses 
# (implicit continuation, like the `basic_syntax` line-continuation exercise), 
# multiplies by an hourly wage of `18`, and prints the weekly pay.
hours_worked_day1 = int(input("How many hours did you work in day 1?"))
hours_worked_day2 = int(input("How many hours did you work in day 2? "))
hours_worked_day3 = int(input("How many hours did you work in day 3? "))
hourly_wage = 18

print("The weekly pay is:", (hours_worked_day1 
      + hours_worked_day2 +  
        hours_worked_day3) * 
        hourly_wage)



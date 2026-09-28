# 3. Write a script with a multi-branch `if/elif/else` 
# that reads `grade_percent` (int, input) and prints 
# `"A"` for 90+, `"B"` for 80-89, `"C"` for 70-79, and `"F"` otherwise.
grade_percent = int(input())
if grade_percent >= 90:
    print('A')
elif grade_percent >=80:
    print('B')
elif grade_percent >= 70:
    print('C')
else:
    print('F')
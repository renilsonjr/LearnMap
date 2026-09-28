# 4. Write a script using `or` that prints `"Lucky number!"` 
# if a user-entered number is `7`, `13`, or `21`, otherwise 
# `"Just a number."`.
number = int(input())
if (number == 7) or (number == 13) or (number == 21):
    print("Lucky number!")
else:
    print('Just a number.')

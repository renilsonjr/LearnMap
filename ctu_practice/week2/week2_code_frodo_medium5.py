# 5. Write a script using `and` that prints `"Approved"` 
# only if `age` (input, int) is 18 or older AND the user answered 
# `'yes'` to having an ID, otherwise `"Denied"`.

age = int(input('What is your age?'))
id = input('Do you have an ID?')

if age >= 18 and id == 'yes':
    print('Approved')
else:
    print('Denied')


# 2. Write a script that reads `club_member_years` (int, input) 
# and sets `discount = 15` if 5 or more years, otherwise
# `discount = 0`; print the result.`
club_member_years = int(input('Do you have memebership?'))

if club_member_years >= 5:
    discount = 15
else:
    discount = 0
print('You have: ${}'.format(discount))


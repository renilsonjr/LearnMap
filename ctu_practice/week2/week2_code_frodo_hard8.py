# 8. Write a program checking a small hard-coded 
# inventory dictionary (item name → stock count) 
# against a user-entered item name, with a nested `if/else` 
# inside an outer membership check — first write a version with 
# **intentionally broken/inconsistent indentation** as a comment, 
# then the corrected, working version below it.

# inventory = {'pencil': 3,'pen': 5, 'computer': 0}

# item_name = input(('what item do u want?'))



#this comment carryes the program with an identation error
# if item_name in inventory:

# if inventory[item_name] > 0:
#         print('We have this amount {}'.format(inventory[item_name]))
# else:
#         print('Item sold out')
# else:
#     print('We dont have this item yet')

inventory = {'pencil': 3,'pen': 5, 'computer': 0}

item_name = input(('what item do u want?'))

if item_name in inventory:

    if inventory[item_name] > 0:
        print('We have this amount {}'.format(inventory[item_name]))
    else:
        print('Item sold out')
else:
    print('We dont have this item yet')
        
     

    





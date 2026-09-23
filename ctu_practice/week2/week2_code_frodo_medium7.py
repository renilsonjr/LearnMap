# 7. Write a script with a nested `if` inside an `if/else`: 
# read whether it's raining and whether the user has an umbrella 
# (both compared against `'yes'`); if raining, print a different 
# message depending on the umbrella; if not raining, print one message 
# regardless.

umbrella = input(('Do you have an umbrella?'))
raining = input(('Is it raining?'))

if raining == 'yes':
    if umbrella == 'yes':
        print("You can go outside")
    else:
        print("Grab an umbrella")
else:
    print('You still can go outside')
    

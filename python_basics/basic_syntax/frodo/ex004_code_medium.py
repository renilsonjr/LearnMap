# ## Medium
# 4. Write a script that would raise an `IndentationError` if run as-is (leave the broken version in a comment) and then include the corrected, working version below it.
# 5. Write a function `greet(name)` with a multi-line docstring and a one-line body, keeping every line under 79 characters (PEP 8).
# 6. Write a script that sums 10 hard-coded numbers using an expression wrapped across three lines via implicit continuation inside parentheses.
# 7. Write one line with two statements separated by `;`, then rewrite it as two separate lines; add a comment explaining which style is preferred and why.

# house_utensils = ("fork", "mug", "glass", "book", "higienic paper")
# user_input = input("Which item are you looking for? ")

# if user_input in house_utensils:
# print ("found") 
# else:
# print ("not found")

house_utensils = ("fork", "mug", "glass", "book", "higienic paper")
user_input = input("Which item are you looking for? ")

if user_input in house_utensils:
    print ("found")
else:
    print ("not found")


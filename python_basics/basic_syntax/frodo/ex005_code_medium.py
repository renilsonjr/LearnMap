# 5. Write a function `greet(name)` with a multi-line docstring and a one-line body, 
# keeping every line under 79 characters (PEP 8).


def greet(name):
    """
Greets person by,  
while
they are totally distracted thinking about their usells lifes
their name
"""
    print("hello", name)
greet("frodo")
print(greet.__doc__)
    
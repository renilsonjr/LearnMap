# 2. Write a function `greet(name)` that takes one parameter and returns a 
# greeting string built from it. Call it with two different names and print 
# both results.
user_input = input()
def greet(user_input):
    return user_input, "you are welcome"
print(greet(user_input))
# 2. Write a function `greet(name)` that takes one parameter and returns a 
# greeting string built from it. Call it with two different names and print 
# both results.
name1 = input("qual seu nome?")
name2 = input("qual seu nome?")
def greet(name):
    return f"you are welcome {name}"
print(greet(name1))
print(greet(name2))
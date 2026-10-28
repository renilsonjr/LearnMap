# 8. Write a script demonstrating variable scope: a global variable
# `visitor_count = 0`, and a function `log_visit()` that uses the `global`
# keyword to increment it by 1 each call. Call the function three times, then print the final count.
visitor_count = 0
def log_visit():
    global visitor_count
    visitor_count = visitor_count + 1
log_visit()
log_visit()
log_visit()
print(visitor_count)
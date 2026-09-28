# 4. Given `ratings = [4.5, 3.0, 5.0, 2.5, 4.0]`, use a `for` loop with an accumulator 
# variable to compute the sum, then print the average formatted to 2 decimal places, 
# plus the lowest and highest rating using `min()` and `max()`.

ratings = [4.5, 3.0, 5.0, 2.5, 4.0]
sum = 0
for i in ratings:
    sum = sum + i
print(sum)
print('{:.2f}'.format(sum / 5))
print(min(ratings))
print(max(ratings))
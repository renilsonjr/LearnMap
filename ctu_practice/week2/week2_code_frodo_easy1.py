# 1. Write a script that reads `movie_rating` (int, input) 
# and prints `"Kid-friendly"` if it's 3 or higher, 
# otherwise `"Not for kids"`.

movie_rating = int(input())
if movie_rating >= 3:
    print("Kid-friendly")
else:
    print("Not for kids")
    
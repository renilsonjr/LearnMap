# 5. Write two functions: `circle_area(radius)` that returns the area of a circle, and `cylinder_volume(radius, height)` 
# that calls `circle_area()` internally and returns the volume. Print the volume for one radius/height pair.

def circle_area(radius):
    return 3.14 * radius * radius
def cylinder_volume(radius, height):
    return circle_area(radius) * height
print(cylinder_volume(23,10))
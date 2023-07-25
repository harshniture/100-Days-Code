#Take three sides of a triangle. And then calculate the area of the triangle.

import math

a = float(input())
b = float(input())
c = float(input())

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of your triangle is ', area)
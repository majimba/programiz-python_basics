#!/usr/bin/python3

# Calculate the area of a triangle

# Create variables a, b, c to store input from user
a = float(input('Length of a: '))
b = float(input('Length of b: '))
c = float(input('Length of c: '))

# Compute semiperimeter s and then the area of the triangle using the above formula.
s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

# Print the area
print(area)

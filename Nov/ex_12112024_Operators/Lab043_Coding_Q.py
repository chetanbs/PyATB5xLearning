# Write a Program to Calculate the
# area of a circle given its radius using the formula
# ''' area=r^2 ''' (Take pie as 3.14)

#Logic Building formula

#Step 1 figure out the inputs and output
#input -> r -> data type -> float
#pi = 3.14
#power -> pow or ** -> any ca be used
#O/P -> float - area, print area

#Step 2
#rough logic = area * 3.14 * pow(r,2)

#import math

#Step 3
radius = float(input("Enter the radius of the circle\n"))
print(radius)
area = 3.140987654321 * (radius ** 2)

#print(math.pi)
print("Area of the Circle is = ", area)
print(f"Area of the Circle is (Area) = {area:.2f}")
# f -> Formatting the output statement

# * -> multiplication
# ** -> power

import math
print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("Area of the Circle is => ", area)




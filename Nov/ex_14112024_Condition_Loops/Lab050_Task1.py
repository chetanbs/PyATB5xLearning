# Write a program that classifies a triangle based on its side lengths. Given three input values
# representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

len1 = int(input("Enter the Length value1: "))  # 10 20
len2 = int(input("Enter the Length value2: "))  # 10 30
len3 = int(input("Enter the Length value3: "))  # 10 20

if len1 >= len2 and len1 >= len3:
    print("Triangle is equilateral")
elif len2 >= len1 and len2 >= len3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")

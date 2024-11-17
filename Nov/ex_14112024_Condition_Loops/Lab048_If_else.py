# Problem find the MAX between 3 numbers

#Logic Building

# User inputs - num1, num2, num3 -> int
# O/P -> int or string with max number

# Logic ? If_else - 1 Condition

# Syntax
# if condition 1:
#    print("Print 1")
# elif condition 2:
#    print("Print 2")
# elif condition 3:
#    print("Print 3")
# else:
#    print("Print else")


num1 = int(input("Enter the num1: "))  # 5, 10
num2 = int(input("Enter the num2: "))  # 3, 12
num3 = int(input("Enter the num3: "))  # 2, 11

# 5 > 3 and 5 > 2 => 5
# num1 > num2 and num 1 > num 3 => num1

# 12 > 10 and 12 > 11 => 12
# num2 > num1 and num2 > num3 => num2

# num3

if num1 > num2 and num1 > num3:
    print("Max number is: ", num1)
elif num2 > num1 and num2 > num3:
    print("Max number is: ", num2)
else:
    print("Max number is: ", num3)


# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 -> num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("Enter the value1 (dividend): "))
num2 = int(input("Enter the value2 (divisor): "))

#divmod() function also can be used 

quotient = num1 // num2  # using float division to get quotient
remainder = num1 % num2  # using module to get the remainder

print("Quotient Value (Q) = ", quotient)
print("Remainder Value (R) =", remainder)


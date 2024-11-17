#Write a Program to take user age and let him know if he can go to club. 21

user_age = int(input("Enter your age\n"))
age = int(user_age)

if user_age >= 21:
    print("You can go to Club")
else:
    print("You can not go to Club")


# Check for Edge cases
# We should consider edge cases such as:
# Negative age value or extremely high values -> program will break
# Non-Numeric input - ABC
# Age which is valid

# Optimize the Code
# Handle all the edges

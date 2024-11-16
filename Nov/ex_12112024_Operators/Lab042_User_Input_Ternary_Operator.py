# Program - if age > 18 -> Allowed to Vote
# else -> not allowed to Vote

user_age = int(input("Enter your age\n"))

if user_age > 18:
    print("Yes, you are eligible to Vote")
else:
    print("No, you are not eligible to Vote")

#Using Ternary Operator:
#print("Yes, you are eligible to Vote" if user_age > 18 else "Yes, you are not eligible to Vote")

print("Yes, you are eligible to Vote" if int(input("Enter your age\n")) else "Yes, you are not eligible to Vote")
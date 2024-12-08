print("---- Start of the Program ----")
try:
    a = int(input("Enter the num1: "))
    b = int(input("Enter the num2: "))
    c = a/b  # 10/0 -> ZeroDivisionError: division by zero
    print("Result Div is ", c) # ABC -> ValueError: invalid literal for int() with base 10: 'abc'
except Exception as e:
    print(e)

print("---- End of the Program ----")


# try:
        # Try this code, if error
# except:
        # Execute mme if try has some error
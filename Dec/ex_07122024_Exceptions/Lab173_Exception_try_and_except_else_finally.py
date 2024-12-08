try:
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    result = num1/num2  # 10/0 -> ZeroDivisionError: division by zero
    #print("Result Div is ", c) # ABC -> ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Output is ", result)
finally:
    print("This finally part will be always executed")




#try:
#    num1 = int(input("Enter the num1: "))
#    num2 = int(input("Enter the num2: "))
#    result = num1/num2  # 10/0 -> ZeroDivisionError: division by zero
    #print("Result Div is ", c) # ABC -> ValueError: invalid literal for int() with base 10: 'abc'
#except Exception as e:
#    print(e)
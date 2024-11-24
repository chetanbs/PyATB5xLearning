# User Defined -> a. With Arguments and b. Without Arguments
# a. They cant return anything -> non return
# b. They can return something
# c. They have a parameter
# d. They dont have parameters/arguments

# a. They cant return anything -> non return
# No return type and no parameters/Arguments

def greet():
    print("Hello")

greet()

# b. They can return something
# No Return type and with argument/Parameters

def greet_by_name(name):
    print("Hello,", name)

greet_by_name("Python")

# c. They have a parameter
# No Return Type and with Default Argument

def say_hello_default_arg(name="Python"):
    print("Hello", name.upper())

say_hello_default_arg("Program")
say_hello_default_arg()

def multiple_args(name1="A", name2="B"):
    print("Multiple", name1, name2)

multiple_args()
multiple_args("Learn", "Coding")
multiple_args(name1="Python")
multiple_args(name1="Learn", name2="Program")
multiple_args(name2="Code")

# 4. Arguments with Return Type

def sum_of_two(a, b):
    return a + b

result = sum_of_two(4, 56)
print(result)

def sum_of_two_number_with_default(num1 = 100, num2 = 200):
    return num1 + num2

result = sum_of_two_number_with_default(num1 = 34, num2 = 34)
print(result)
result = sum_of_two_number_with_default()
print(result)
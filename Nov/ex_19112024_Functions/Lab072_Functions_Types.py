def say_hello():
     print("Hello")

say_hello()


# Functions with arguments, parameters

def greet_by_name(name):
    print("Hello,", name)
    print(f"Hello, {name}")

greet_by_name("Python")
greet_by_name(123)
greet_by_name(3.14)
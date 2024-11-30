class Dog:
    # Attributes
    name = "chow"
    breed = None
    height = None
    weight = None

# Constructor
# Special function in Class ->  __init__()
# It will be automatically called when you create an Object
# __init__ -> Object is created, it will be called automatically
# 2 types of constructors - 1. Default  2. Parameterized
    def __init__(self):
        print("I will be called")

    # Behavior
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass

# Object Ref

chow_ref = Dog()
# Dog() - Object
# chow -> Object Reference

mow_ref = Dog()
bow_ref = Dog()
rancho_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)
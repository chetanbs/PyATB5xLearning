# Polymorphism
# Objects -> Many forms
# Behaviour - different based on who is calling
# Polymorphism allows objects of different classes to be treated as object of a common superclass
# Two Types
# 1. Method Overriding - Can override the methods of parent
# 2. Method Overloading - By default doesnot support direct method overloading concept

# Method Overloading

class Dog:

    def bark(self):
        print("Dog is barking")

    def bark(self, breed):
        print(f"Dog with {breed} is barking")


d = Dog()
d.bark("chow")
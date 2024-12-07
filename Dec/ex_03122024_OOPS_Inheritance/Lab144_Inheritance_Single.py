# Inheritance
# Inheritance is a fundamental concept in OOPs
# It allows a new class to be based on an existing class, inheriting its attributes and methods
# Child <- Parent (Attributes, Behavior)

# Types of Inheritance
# Single Inheritance: A Child class inherits from a single parent class
# Multiple Inheritance: A Child class inherits from two or more parent classes
# Multi-level Inheritance: A Class inherits from  child class, forming aparent -> child -> grandchild relationship
# Hierarchical Inheritance: Multiple child classed inherit from a single parent class
# Hybrid Inheritance:  combination of two or more types of inheritance

# Single Inheritance

class Father:
    key = "2BHK"
    def car(self):
        print("Father has a Car -> MarutiSuzuki")
        print(self.key)


class Son(Father):   # Single Inheritance
    key2 = "3BHK"
    def suv(self):
        print("Son has a Car -> MG")
        print(self.key2)

father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.suv()

# Son

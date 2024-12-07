# Abstraction - TO hide the details and show what is required
# Car - with key - __private, tyres - public
# Car - multiple - Engine, Gearbox
# Car - driver - Engine, gearbox?

# ABC - Abstract Base Class
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Bark")


obj = Dog("Bhow")
obj.make_sound()




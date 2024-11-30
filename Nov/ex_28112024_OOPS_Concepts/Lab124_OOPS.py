# OOPS Concept -> Object Oriented Program
# Object_oriented Programing is a methodology or pradigm to design a program using classed
#and objects

# It simplifies the software development and aintenance by providing some concepts
# Something related to Object -> Classes
# OOPS divide the program class and objects
# Emphasis the data
# Productivity is high

# Objects are the main building blocks of OOPS i.e your applications will be
# divided into multiple objects

# Class - Blueprint
# Class is a user-defined data type which defines its properties and its methods
# A class can have some properties and functions (called methods)
# Attributes | properties | data variables
# Behavior | Methods(functions) | Data members | Member functions

# Object
# Object is a run-time entity. It is an instance of the class
# An object can represent a person, place or any other item
# Real world entity from the clss

# Attributes
# Attributes - name, id, phoneNo, gender, color_eyes, city, location, address
# Behavior - walk, talk, write, sing, dance, watch, listen, sleep, cry, smile

class Person:
    # Attributes - What you have?
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    # Behavior - What you can do?

    def talk(self):    # NRNARG
        print("I can talk")

    def sleep(self, name):   # Arg with No Return
        print("I am a Method")
        print("Sleep", name)

    def sleep2(self, name):   # Arg with Return
        print("I am a Method")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):   # No Arg with Return
        return "I am walking"


# Create an Objet of the Class
# ObjectRef = ClassName() -> Object

abc = Person()
abc.name = "Learn Python"
abc.gender = "Male"



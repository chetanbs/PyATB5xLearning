# Encapsulation
# Bind the data variable with the methods
# Data Member / Class Variables
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation
# __private_var -> It is available only in the class and its methods
# public_var -> It is available to all

class Car:
    model = None
    name = None
    password = 123


    def __init__(self):
        self.password = "Test"   # Public instance variable
        self._password_secure = "pass123"  # # Private instance variable

    def change_password(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
#object_ref.password = "Hello"
print(object_ref.__password_secure)  # 'Car' object has no attribute '__password_secure'.
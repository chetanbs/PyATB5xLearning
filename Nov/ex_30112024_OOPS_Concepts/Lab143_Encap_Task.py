# Create a class with public and private variable and method to access them ouside

class Flat:

    def __init__(self):
        self.public_var = "Owner"
        self.__private_var = "Tenant"

    def Co_Owner(self):
        print(self.__private_var)


object_ref = Flat()
object_ref.Co_Owner()
print(object_ref.public_var)
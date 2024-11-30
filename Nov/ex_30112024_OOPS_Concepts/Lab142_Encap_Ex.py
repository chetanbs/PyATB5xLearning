class Home:

    def __init__(self):
        self.public_var = "Father"
        self.__private_var = "Child"

    def Mother(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("Function is Private")

object_ref = Home()
object_ref.Mother()
#print(object_ref.__private_var)  # 'Home' object has no attribute '__private_var'.
print(object_ref.public_var)
#object_ref.__wife()  # 'Home' object has no attribute '__wife'



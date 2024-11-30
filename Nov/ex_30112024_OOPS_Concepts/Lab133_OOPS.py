# Local Variable - can be accessed directly
# Local variables always have a high preference as compared with global variable
# Instance Variable - can be accessed by the self keyword

a = 10  # Global Variable

class Person:
    b = 11    # Instance Variable - Belongs to class

    def print_info(self):
        c = 20  # Local Variable
        print(c)
        print(self.b)
        #a = "Hello"
        global a
        print(a)

obj_ref = Person()
obj_ref.print_info()
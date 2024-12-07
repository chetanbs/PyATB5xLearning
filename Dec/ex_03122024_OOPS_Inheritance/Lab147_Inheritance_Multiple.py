# Multiple Inheritance

class Father:

    def home(self):
        return "This is from Father"

    def father_money(self):
        return 10

class Mother():

    def home(self):
        return "This is from Mother"

    def mother_money(self):
        return 5


class Son(Mother, Father):    # Multiple Inheritance - First Come First Serve

    def print_info(self):
        print("Son")


s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home())
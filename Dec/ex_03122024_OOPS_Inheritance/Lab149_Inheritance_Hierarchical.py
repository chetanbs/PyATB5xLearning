# Hierarchical Inheritance Concept

class Father:

    def BHK1(self):
        print("1BHK")


class Child1(Father):

    def BHK2(self):
        print("2BHK")

class Child2(Father):

    def BHK3(self):
        print("3BHK")

class Child3(Father):

    def no_house(self):
        print("No House")


child = Child1()
child.BHK1()
child.BHK2()

c = Child2()
c.BHK1()
c.BHK3()
# c.BHK2()  # This belongs to Child1 class

cc = Child3()
cc.BHK1()  # Child can access its father property


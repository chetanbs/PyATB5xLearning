# Single Inheritance

class Parent:
    gold = "2Kg"

    def BHK2(self):
        print("2BHK House")


class Child(Parent):  # Single Inheritance
    diamond = "Diamond"

    def BHK3(self):
        print("3BHK House")

child_object = Child()
print(child_object.gold)
child_object.BHK2()


father_object_ref = Parent()
father_object_ref.BHK2()
# father_object_ref.BHK3() # Not able to access
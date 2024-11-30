class Person:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name

obj = Person("Code")
obj_ref = Person("Learn")

print(obj.name)
print(obj_ref.name)

print("Who is walking", obj.walk())
print("Who is walking", obj_ref.walk())
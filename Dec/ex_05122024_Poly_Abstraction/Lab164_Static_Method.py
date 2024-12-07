# Static Method
# Static Method is a method that belongs to a class rather than an instance of the class
# Static variables in Python are class-level variables shared by all instances of a class
# Defined within a class but outside any method
# Static method which can be called by ClassName (no object creation) @staticmethod
# No Static -> require the object creation


class O:

    @staticmethod
    def sum(a, b):
        return a + b

    def sub(self, a, b):
        return a - b

obj = O()
result = obj.sub(4,2)
print(result)

print(O.sum(4,4))
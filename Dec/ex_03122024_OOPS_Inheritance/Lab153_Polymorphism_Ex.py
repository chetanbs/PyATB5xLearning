# Method Overloading concept
# Example

class MathUtils:

# Method overloading is not supported by default

    def add(self, a=10, b=10):
        return a + b

    #def add(self, a, b, c):
    #    return a + b + c

    #def add(self, a=0, b=0, c=0, d=0):
    #    return a + b + c + d

math = MathUtils()
print(math.add(1,2))
#op2 = math.add(1,2,3)
#op3 = math.add(2,4,6,8)

# need to declare the values


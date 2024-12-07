# Hybrid Inheritance
# Multiple types of inheritance
# Such as Single, Multiple, Multi-level

class A:

    def methodA(self):
        return "Method A"


class B(A):

    def methodB(self):
        return "Method B"


class C(A):

    def methodC(self):
        return "Method C"


class D(B, C):  # Multiple, Multilevel - MRO(Method Resolution Order)

    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())